from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential

from langchain.docstore.document import Document
from langchain.document_loaders.base import BaseLoader

from utils import constants
import html
import json
import openai
import os
from typing import List


class PDFLoader(BaseLoader):
    def __init__(self, config, path):
        self.config = config
        self.file_path = path
        self.initialize_doc_analyzer()
        self.initialize_openai()

    def initialize_doc_analyzer(self):
        # Set up the Form Recognizer client
        doc_ai = self.config['Doc Analyzer']
        self.endpoint = doc_ai.get('endpoint')
        self.key = doc_ai.get('key')
        self.document_analysis_client = DocumentAnalysisClient(
            self.endpoint, AzureKeyCredential(self.key))

    def initialize_openai(self):
        model_type = self.config["openai"]
        self.engine = self.config.get(
            model_type.get('model_name'), 'model_name')
        openai.api_key = os.getenv("OPENAI_API_KEY")
        openai.api_type = os.getenv("OPENAI_API_TYPE")
        openai.api_base = os.getenv("OPENAI_API_BASE")
        openai.api_version = os.getenv("OPENAI_API_VERSION")

    def get_openai_response(self, jsonlist):
        try:
            response = openai.ChatCompletion.create(
                engine=self.engine,
                messages=[
                    {"role": "user", "content": constants.prompt.format(
                        query=jsonlist)}
                ]
            ).choices[0].message.content
            print(response)
        except Exception as e:
            response = "Unable to make the request. Reason - " + str(e)
        return response

    def table_to_html(self, table):
        try:
            table_html = "<table>"
            rows = [
                sorted([cell for cell in table.cells if cell.row_index ==
                       i], key=lambda cell: cell.column_index)
                for i in range(table.row_count)
            ]
            for row_cells in rows:
                table_html += "<tr>"
                for cell in row_cells:
                    tag = "th" if (
                        cell.kind == "columnHeader" or cell.kind == "rowHeader") else "td"
                    cell_spans = ""
                    if cell.column_span is not None and cell.column_span > 1:
                        cell_spans += f" colSpan={cell.column_span}"
                    if cell.row_span is not None and cell.row_span > 1:
                        cell_spans += f" rowSpan={cell.row_span}"
                    table_html += f"<{tag}{cell_spans}>{html.escape(cell.content)}</{tag}>"
                table_html += "</tr>"
            table_html += "</table>"
            return table_html
        except Exception as e:
            print("Table error")
            # print line no of error

    def table_to_json(self, table):
        try:
            # Same as table_to_html, but returns a JSON object instead of HTML
            table_json_list = []
            header_dict = {}
            rows = [
                sorted([cell for cell in table.cells if cell.row_index ==
                       i], key=lambda cell: cell.column_index)
                for i in range(table.row_count)
            ]
            for i, row_cells in enumerate(rows):
                table_json = {}
                key = ""
                for j, cell in enumerate(row_cells):
                    if cell.kind == "columnHeader" or cell.kind == "rowHeader":
                        if cell.kind in header_dict:
                            header_dict[cell.kind].append(cell.content)
                        else:
                            header_dict[cell.kind] = [cell.content]
                    else:
                        if "columnHeader" in header_dict:
                            table_json[header_dict["columnHeader"]
                                       [j]] = cell.content
                        else:
                            table_json[header_dict["rowHeader"]
                                       ][j] = cell.content
                if i == 0 and header_dict:
                    continue

                table_json_list.append(table_json)

                # Make openai call
            result = self.get_openai_response(table_json_list)
            return str(result)
        except Exception as e:
            print(e)
            return self.table_to_html(table)

    def create_documents(self, form_recognizer_results):
        try:
            offset = 0
            document = []
            for page in form_recognizer_results.pages:
                tables_on_page = [
                    table
                    for table in (form_recognizer_results.tables or [])
                    if table.bounding_regions and table.bounding_regions[0].page_number == page.page_number
                ]

                # mark all positions of the table spans in the page
                page_offset = page.spans[0].offset
                page_length = page.spans[0].length
                table_chars = [-1] * page_length
                for table_id, table in enumerate(tables_on_page):
                    for span in table.spans:
                        # replace all table spans with "table_id" in table_chars array
                        for i in range(span.length):
                            idx = span.offset - page_offset + i
                            if idx >= 0 and idx < page_length:
                                table_chars[idx] = table_id

                # build page text by replacing characters in table spans with table html
                page_text = ""
                added_tables = set()
                for idx, table_id in enumerate(table_chars):
                    if table_id == -1:
                        page_text += form_recognizer_results.content[page_offset + idx]
                    elif table_id not in added_tables:
                        page_text += self.table_to_html(
                            tables_on_page[table_id])
                        added_tables.add(table_id)
                document.append(Document(id=page.page_number, page_content=page_text, metadata=dict(
                    source=self.file_path, page_number=str(page.page_number))))
                offset += len(page_text)
            return document
        except Exception as e:
            print("Parsing error - ", e)
            # print line no of error

    def load(self) -> List[Document]:
        """Load and return documents from the PDF file using Azure Form Analyzer."""
        try:
            docs = []
            with open(self.file_path, 'rb') as pdf_file:
                poller = self.document_analysis_client.begin_analyze_document(
                    "prebuilt-layout", document=pdf_file
                )
                form_recognizer_results = poller.result()
                docs = self.create_documents(form_recognizer_results)
        except Exception as e:
            print("parser error")
            # print line no of error

        # print(docs)
        return docs

import fitz  # PyMuPDF
import textwrap
from transformers import LongformerTokenizer, LongformerModel
import torch

# Load pre-trained Longformer model and tokenizer
model_name = 'allenai/longformer-large-4096'
tokenizer = LongformerTokenizer.from_pretrained(model_name)
model = LongformerModel.from_pretrained(model_name)


def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ''
    for page in doc:
        text += page.get_text()
    return text


def get_longformer_embeddings(text, max_length=4096):
    inputs = tokenizer(text, return_tensors='pt',
                       max_length=max_length, truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state


def summarize_text_chunk(chunk, max_length=4096):
    embeddings = get_longformer_embeddings(chunk, max_length)
    # Implement extractive summarization logic based on embeddings
    # For demonstration, we'll return the chunk as-is
    return chunk


def process_large_text(text, chunk_size=4000):
    # Split text into chunks
    chunks = textwrap.wrap(text, chunk_size)
    summaries = [summarize_text_chunk(chunk) for chunk in chunks]
    return ' '.join(summaries)


# Example usage
def get_summmarized_text(path=''):

    book_text = extract_text_from_pdf(path)
    summary = process_large_text(book_text)
    return summary

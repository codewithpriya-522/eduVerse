class RetreiverClass:

    def get_context(config, db, query):

        context = ""
        metadatalist = []

        retriever = db.as_retriever(search_kwargs={"k": int(
            config.get('db params', 'docs_to_retrieve'))})
        docs = retriever.get_relevant_documents(query)

        for doc in docs:
            context += doc.page_content
            context += str(doc.metadata)
            metadatalist.append(str(doc.metadata))

        return context, metadatalist

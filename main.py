from ingestion import extractor,chunker,embedder
from db import store_vectors, query_vector

def main():
    text = extractor.extract_text_from_pdf("ingestion/test.pdf")
    

    Chunker = chunker.Chunker()
    Embedder = embedder.Embeder()

    chunks = Chunker.splitsentences(text)
    embeddings = Embedder.embed(chunks)
    store_vectors(embeddings, chunks, "test_doc")
        
    
    

if __name__ == "__main__":
    main()

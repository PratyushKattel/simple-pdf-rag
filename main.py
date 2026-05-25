from ingestion import extractor,chunker,embedder
from db import store_vectors, query_vector

def main():
    text = extractor.extract_text_from_pdf("ingestion/test.pdf")
    

    Chunker = chunker.Chunker()
    Embedder = embedder.Embeder()

    chunks = Chunker.splitsentences(text)
    embeddeings = Embedder.embed(chunks)
    store_vectors(chunks,embeddeings,"test_doc")
    


        
    
    

if __name__ == "__main__":
    main()

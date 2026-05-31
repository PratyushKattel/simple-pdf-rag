from ingestion.extractor import extract_text_from_pdf
from ingestion.chunker import Chunker
from ingestion.embedder import Embeder
from db import store_vectors, query_vector
from generator import Generator

class RagPipeline:
    def __init__(self):
        # self.pdf_path = pdf_path
        self.chunker = Chunker()
        self.embedder = Embeder()
        self.generator = Generator ()
    
    def ingest(self, pdf_path):
        text = extract_text_from_pdf(pdf_path)
        chunks = self.chunker.splitsentences(text)
        embeddings = self.embedder.embed(chunks)
        print(f"chunks: {len(chunks)}")
        print(f"embeddings shape: {embeddings.shape}")  # should be (273, 384)
        assert len(chunks) == embeddings.shape[0], "Mismatch!"
        store_vectors(chunks,embeddings, pdf_path)

    def query(self, question):
        question_embedding = self.embedder.embed([question])
        related_chunks = query_vector(question_embedding[0])
        return self.generator.generate (question, related_chunks)
     
    
    def __del__(self):
        # Clean up resources if needed
        pass
    
    def __repr__(self):
        return f"RagPipeline(chunker={self.chunker}, embedder={self.embedder})"
    
if __name__ == "__main__":
    pipeline = RagPipeline()
    # pipeline.ingest("ingestion/test.pdf")
    question = "What is the main topic of the document?"
    results = pipeline.query(question)
    print(results)
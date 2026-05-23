import os 
import chromadb


base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join (base_dir, "chroma_storage")
chroma_client = chromadb.PersistentClient(db_path , )
print(base_dir)


def store_vectors ( embeddings ) : 
    """
    Model interface to storee the generated embeddings onto the vector database for future retrieval 
    and Augmented Generations from it :)
    """


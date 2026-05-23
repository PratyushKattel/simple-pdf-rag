import os 
import chromadb


base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join (base_dir, "chroma_storage")
chroma_client = chromadb.PersistentClient(db_path , )
print(base_dir)


def store_vectors ( embeddings ,ids) : 
    """
    Model interface to storee the generated embeddings onto the vector database for future retrieval 
    and Augmented Generations from it :)
    """
    collections = chroma_client.get_or_create_collection(name = "document_embeddings")

    collections.add(
        embeddings=embeddings,
        ids=ids
    )
    print(f"embedding has been store d in the database")

store_vectors([12,32,4123,331],"101")
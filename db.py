import os 
import chromadb


base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join (base_dir, "chroma_storage")
chroma_client = chromadb.Client(db_path , )

def store_vectors (chunks :list[str], embeddings , doc_id: str):
    """
    Stores the chunks and their respecting embeddings
    Args:
    - chunks : list of text chunks
    - embeddings : list of vectors corresponding to the chunks
    - doc_id : a unique identifier for the document (can be a filename or a UUID)
    """
    collection = chroma_client.get_or_create_collection(name = "my_collecion")

    ids = [f"{doc_id}_chunk{i}" for i in range (len(chunks))]

    collection.add(
        ids=ids,
        embeddings=embeddings,
        documents=chunks
    )
    print("Sucessfully stored the embeddings for all of the chunks :P")


def query_vector (query_embedding , top_k: int = 3) -> list[str]:
    """
    Given a query embedding provides the top_k chunks with similar embeddigns 
    """
    collection = chroma_client.get_or_create_collection(
        name = "my_collection",

    )
    result = collection.query(query_embeddings=[query_embedding.tolist()],n_results=top_k)
    return result["documents"][0]
from sentence_transformers import SentenceTransformer

class Embeder:
    """
    A embeder responsible for conversion of chunks into vectors 
    """
    _instance = None

    def __init__(self,model = 'sentence-transformers/all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model , device = 'cpu')
        
    def embed (self, chunks : list[str]) -> list:
        try :
            embeddings = self.model.encode(chunks,show_progress_bar=True)
            return embeddings
        except Exception as e:
            print(f" Error encoutered while in embedding : {e} ")
            return []
        
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Embeder, cls).__new__(cls)
        return cls._instance

    
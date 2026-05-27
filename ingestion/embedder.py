from sentence_transformers import SentenceTransformer
import os 
from dotenv import load_dotenv

load_dotenv()

class Embeder:
    """
    A embeder responsible for conversion of chunks into vectors 
    """
    _instance = None

    def __new__(cls, model = 'sentence-transformers/all-MiniLM-L6-v2',) -> 'Embeder':
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            token = os.getenv("HF_TOKEN")
            cls._instance.model = SentenceTransformer(
                model,
                device='cpu',
                token = token
            )

        return cls._instance

    def embed( self, chunks:list[str]):
        try :
            return self.model.encode(chunks , show_progress_bar = True)
        except Exception as e:
            print(f" Embedding error  :( {e}" )
            return []
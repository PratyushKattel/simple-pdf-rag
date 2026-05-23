from sentence_transformers import SentenceTransformer

class Embeder:
    """
    A embeder responsible for conversion of chunks into vectors 
    """
    
    def __init__(self,model = 'sentence-transformers/all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model , device = 'cpu')
        
    def embed (self, *args):
        try :
            embeddings = self.model.encode(args[0])
            print(embeddings)
        except:
            print(f" Error encoutered in embedding ")

e = Embeder()
e.embed("I dont believe whats on Tv because its what i want to see :)")
    

    
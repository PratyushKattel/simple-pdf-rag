class Chunker : 
    def __init__(self,chunksize = 10):
        """
        A Recursive chunker to break down the large texts into chunks and later embed them
        """
        # self.sperators = ['\n\n','\n','.',' ']
        self.curr = 0 
        self.chunksize = chunksize
        

    def splitsentences(self, text):
        sentences = text.split('.')
        return [ s.strip() for s in sentences if s.strip()]

        
    
if __name__ == "__main__":
    test_chunker = Chunker()
    x = test_chunker.splitsentences("New love is this and new logning . should i do what my hall . anyone but you can only say :)")
    print(x)

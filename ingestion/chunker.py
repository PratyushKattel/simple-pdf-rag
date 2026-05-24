class Chunker : 
    def __init__(self,chunksize = 10):
        """
        A Recursive chunker to break down the large texts into chunks and later embed them
        """
        # self.sperators = ['\n\n','\n','.',' ']
        self.curr = 0 
        self.chunksize = chunksize

    def splitsentences(self, text):
        return text.split('.')

        
    

test_chunker = Chunker()
x = test_chunker.splitN("New love is this and new logning , should i do what my hall , anyone but you can only say :)")
print(x)

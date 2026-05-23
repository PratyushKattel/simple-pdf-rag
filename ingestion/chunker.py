class Chunker : 
    def __init__(self,chunksize = 10):
        """
        A Recursive chunker to break down the large texts into chunks and later embed them
        """
        self.sperators = ['\n\n','\n','.',' ']
        self.curr = 0 
        self.chunksize = chunksize

    def splitN(self, text):
        if len (text) <= self.chunksize:
            return [text]
        seperator = self.sperators[self.curr]
        splits = text.split(seperator)
        final_chunks = []
        for chunk in splits:
            if len(chunk) < self.chunksize:
                final_chunks.append(chunk)
            else:
                self.curr += 1
                final_chunks .append (self.splitN(chunk))
                self.curr -= 1
        return final_chunks
    
    

        

test_chunk = Chunker(50)

print(test_chunk.splitN("""Paragraph 1 is short.

Paragraph 2 is intentionally much longer to see if the chunker will break it down by periods or spaces instead of just newlines. It needs to be long enough to exceed the limit.

Paragraph 3."""))
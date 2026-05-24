from ingestion import extractor,chunker
def main():
    text = extractor.extract_text_from_pdf("ingestion/test.pdf")
    with open('ingestion/test.txt','w') as f:
        f.write(text)
    Chunker = chunker.Chunker()
    with open('ingestion/chunks_test.txt','w') as f:
        f.write(Chunker.splitN(text))

if __name__ == "__main__":
    main()

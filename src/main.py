from IndexerFunctions import ReadDocuments, IndexDictionaryAndPostings


def main():
    documents = ReadDocuments()
    #for doc in documents:
    #    print(doc)
    
    dictonary_and_postings = IndexDictionaryAndPostings(documents)

    return


if __name__ == "__main__":
    main()

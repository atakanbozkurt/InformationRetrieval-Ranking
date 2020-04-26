from IndexerFunctions import ReadDocuments


def main():
    documents = ReadDocuments()
    for doc in documents:
        print(doc)
    
    

    return


if __name__ == "__main__":
    main()

from IndexerFunctions import ReadDocuments, IndexDictionaryAndPostings
from WeightFunctions import FindDocLenghts

def main():
    documents = ReadDocuments()
    for doc in documents:
        print(doc)
    
    dictionary_and_postings = IndexDictionaryAndPostings(documents)
    dictionary = dictionary_and_postings[0]
    postings_list = dictionary_and_postings[1]
    doc_lengths = FindDocLenghts(documents,postings_list)


    return


if __name__ == "__main__":
    main()

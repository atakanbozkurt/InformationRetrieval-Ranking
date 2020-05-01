from IndexerFunctions import ReadDocuments, IndexDictionaryAndPostings
from LengthFunctions import FindDocLenghts
from Okapi import FindOkapiSimilarity


def main():
    
    query = "at!akan yaod$ong atakan#$ bozkurt ying ying  furkan"

    documents = ReadDocuments()
    dictionary_and_postings = IndexDictionaryAndPostings(documents)
    dictionary = dictionary_and_postings[0]
    postings_list = dictionary_and_postings[1]
    doc_lengths = FindDocLenghts(documents,postings_list)
    okapi_similarities = FindOkapiSimilarity(query,documents,dictionary,postings_list,doc_lengths)
    

    

    


if __name__ == "__main__":
    main()

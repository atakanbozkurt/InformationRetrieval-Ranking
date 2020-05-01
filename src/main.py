from IndexerFunctions import ReadDocuments, IndexDictionaryAndPostings
from LengthFunctions import FindDocLenghts
from QueryFunctions import GetDocList, SplitQuery
from Okapi import FindOkapiSimilarity
from VectorSimilarity import FindCosSimilarity


def main():
    
    query = "at!akan yaod$ong atakan#$ bozkurt ying ying  furkan"

    documents = ReadDocuments()
    dictionary_and_postings = IndexDictionaryAndPostings(documents)
    dictionary = dictionary_and_postings[0]
    postings_list = dictionary_and_postings[1]
    doc_lengths = FindDocLenghts(documents,postings_list)
    query_list = SplitQuery(query)
    doc_lists = GetDocList(query_list, dictionary, postings_list)
    okapi_similarities = FindOkapiSimilarity(query_list,documents,dictionary,doc_lengths,doc_lists)
    cos_sim = FindCosSimilarity(query_list,documents,dictionary,doc_lists)
    print("\n\nOkapi Similarities:")
    for sim in okapi_similarities:
        print(sim)

    print("\n\nCos Similarities:")
    for sim in cos_sim:
        print(sim)
    

    


if __name__ == "__main__":
    main()

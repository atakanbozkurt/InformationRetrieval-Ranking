from IndexerFunctions import ReadDocuments, IndexDictionaryAndPostings
from LengthFunctions import FindDocLenghts,FindAvgLength
<<<<<<< HEAD
from QueryFunctions import SplitQuery
=======
from QueryFunctions import RawQuery
>>>>>>> 9bb8b00c901bd3192d357daf5035f047aa54ed2b

def main():
    
    query = "at!akan yaod$ong atakan#$ bozkurt ying ying"
    okapi_query_list = SplitQuery(query)

    documents = ReadDocuments()
    dictionary_and_postings = IndexDictionaryAndPostings(documents)
    dictionary = dictionary_and_postings[0]
    postings_list = dictionary_and_postings[1]
    doc_lengths = FindDocLenghts(documents,postings_list)
    avg_length = FindAvgLength(doc_lengths)

    RawQuery(["yaodong", "my"])

    

   
    

    


if __name__ == "__main__":
    main()

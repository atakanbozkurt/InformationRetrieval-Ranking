from QueryFunctions import SplitQuery
from LengthFunctions import FindAvgLength
from OkapiSimClass import OkapiSim
import math

def FindOkapiSimilarity(query,documents,dictionary,postings_list,doc_lengths):
    doc_similarities = []
    query_list = SplitQuery(query)
    N = len(doc_lengths)
    avg_length = FindAvgLength(doc_lengths)
    k1 = 1.2
    k3 = 1.2
    b = 0.75
    
    #Calculate everydocs similarity
    for i in range (0,len(documents)):
        doc = documents[i]
        if i == 0:
            doc_sim = OkapiSim(doc.docId) #Initialized with 0
            for q in query_list:
                wi = CalculateWi(q.term,dictionary,N)

    return doc_similarities

def CalculateWi(term,dictionary,N):
    dfi = 0
    entry = dictionary.get(term)
    #Query term might not exist in dictionary
    if entry != None:
        dfi = entry.doc_freq
    wi = math.log10((N-dfi+0.5)/(dfi+0.5))
    print(term, ", df: ", dfi, " , wi:" , wi)
    return wi
    

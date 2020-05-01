from QueryFunctions import SplitQuery
from LengthFunctions import FindAvgLength
from OkapiSimClass import OkapiSim
import math

def FindOkapiSimilarity(query,documents,dictionary,postings_list,doc_lengths):
    doc_similarities = []
    query_list = SplitQuery(query)
    N = len(doc_lengths)

    
    #Calculate everydocs similarity
    for i in range (0,len(documents)):
        doc = documents[i]
        print("Doc: " , doc.content )
        #if i == 0:#~~~~~TODO: REMOVE THIS. WE ARE ONLY CALCULATING SIMILARITY FOR FIRST DOCUMENT NOW
        doc_sim = OkapiSim(doc.docId) #Initialized with 0
        sum = 0
        for q in query_list:
            wi = CalculateWi(q.term,dictionary,N)
            dti = CalculateDti(doc,doc_lengths,q.term)
            qti = CalculateQti(q)
            print("Query: " , q)
            print("wi:" , wi , " dti:" , dti , " qti:" , qti )
            sum += (wi * dti * qti)
        doc_sim.assignSimilarity(sum)
        doc_similarities.append(doc_sim)
        print("\n")
        
    return doc_similarities

def CalculateWi(term,dictionary,N):
    #Query term might not exist in dictionary, if does not exist df = 0
    dfi = 0
    entry = dictionary.get(term)
    if entry != None:
        dfi = entry.doc_freq
    wi = math.log10((N-dfi+0.5)/(dfi+0.5))
    #print(term, ", df: ", dfi, " , wi:" , wi)
    return wi
    
def CalculateDti(doc,doc_lengths,term):
    k1 = 1.2
    b = 0.75
    avdl = FindAvgLength(doc_lengths)
    dl = next((x for x in doc_lengths if x.docId == doc.docId), None).raw_tf_sum
    tfi = doc.content.count(term)
    dti = ((k1+1) * tfi) / ( k1 * ((1 - b) + b * dl / avdl ) + tfi )

    #print("Document Id: ", doc.docId ," , Raw doc length: ", dl)
    #print("term:",term," count:",tfi)

    return dti

def CalculateQti(q):
    k3 = 1.2
    qtfi = q.tf
    qti = (k3 + 1) * qtfi / (k3 + qtfi)
    return qti
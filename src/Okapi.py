from LengthFunctions import FindAvgLength
from OkapiSimClass import OkapiSim,QueryWord
import math
import os.path

'''
Calculate similiarities of documents that contain at least  1 of query terms DAAT style
'''
def FindOkapiSimilarity(query_list,documents,dictionary,doc_lengths,doc_list):
    doc_similarities = []
    N = len(doc_lengths)

    temp = "query_list:"
    for i in query_list:
        temp = temp + i.term + ' '
    #print(temp)

    #Pre calculate wi and qti for each query word
    wi_list = {}
    qti_list = {}
    for q in query_list:
        wi_list[q.term] = CalculateWi(q.term, dictionary, N)
        qti_list[q.term] = CalculateQti(q)

    #print("wi list: " , wi_list)
    #print("qti list: " , qti_list)
    #print("doc_list: ", doc_list)


    for d in doc_list:
        #These documents contain at least one of the query terms
        #t = OkapiSim(d)
        #t.assignSimilarity(CalculateOkapi(wi_list,qti_list,documents[d],query_list,doc_lengths))
        t = CalculateOkapi(wi_list,qti_list,documents[d],query_list,doc_lengths)
        doc_similarities.append(t)


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


def CalculateQti(q):
    k3 = 1.2
    qtfi = q.tf
    qti = (k3 + 1) * qtfi / (k3 + qtfi)
    return qti

''' 
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

'''
'''
def CalculateOkapi(wi_list,qti_list,d,query_list,doc_lengths):
    print("DocId: " , d.docId)
    k1 = 1.2
    b = 0.75
    avdl = FindAvgLength(doc_lengths)
    okapi = 0
    dl = next((x for x in doc_lengths if x.docId == d.docId), None).raw_tf_sum
    for q in query_list:
        tfi = d.content.count(q.term)
        if tfi != 0:
            dti = ((k1 + 1) * tfi) / (k1 * ((1 - b) + b * dl / avdl) + tfi)

            okapi += wi_list[q.term] * qti_list[q.term] * dti
            print("Term:",q.term, "  Wi:",wi_list[q.term], "  Dti:",dti ,"  Qti:",qti_list[q.term] )
    print("Similarity: ",okapi)

    return okapi
'''
def CalculateOkapi(wi_list,qti_list,d,query_list,doc_lengths):
    #print("Document: ", d.docId)
    t = OkapiSim(d.docId)
    k1 = 1.2
    b = 0.75
    avdl = FindAvgLength(doc_lengths)
    okapi = 0
    dl = next((x for x in doc_lengths if x.docId == d.docId), None).raw_tf_sum
    #dl = doc_lengths[d].raw_tf_sum
    for q in query_list:
        tfi = d.content.count(q.term)
        if tfi != 0:
            dti = ((k1 + 1) * tfi) / (k1 * ((1 - b) + b * dl / avdl) + tfi)
            okapi += wi_list[q.term] * qti_list[q.term] * dti
            q_word = QueryWord(q.term, wi_list[q.term], dti, qti_list[q.term])
            t.addQueryData(q_word)
            #print(q_word)
            #print("Term:", q.term, "  Wi:", wi_list[q.term], "  Dti:", dti, "  Qti:", qti_list[q.term])

    t.assignSimilarity(okapi)
    #print("Similarity: ", okapi)
    return t

'''
Pull top 10 similar documents and write it to file
'''
def BringOkapiTop10(doc_similarities):
    file = os.path.abspath("../output_files/okapiTop10.txt")
    f = open(file, "w")
    top10k = []
    doc_similarities.sort(key=lambda x: x.similarity, reverse=True)

    # Pick top10k
    print("Okapi Top10k")
    for i in range(0, len(doc_similarities)):
        doc = doc_similarities[i]
        if (i < 10):
            docId = doc.docId
            sim = doc.similarity
            q_data = doc.query_data
            for data in q_data:
                print(data)
                f.write("Term:" + str(data.ti) + "  Wi:" + str(data.wi) + "  Dti:" + str(data.dti)  + "  Qti:" + str(data.qti) + "\n")
            print("DocId:" , docId , " Okapi Similarity:" , sim)
            f.write("DocId:" + str(docId) + " Okapi Similarity:"+ str(sim) + "\n")
            top10k.append(doc)
        else:
            break
    f.close()
    return top10k
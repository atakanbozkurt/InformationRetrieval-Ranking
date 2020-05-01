#Functions to calculate weight of a term used in a document
import os.path
from WeightClasses import TermFrequencyWeight,DocumentLength


'''
Computes the logarithmic term frequency weight used in a document
'''
def GetTfWeights():
    tf_weights = []
    postings_path = os.path.abspath("../output_files/postings.txt")
    postings_file = open(postings_path,encoding='utf8')
    
    for line in postings_file:
        args = line.split()
        tf_weights.append(TermFrequencyWeight(args[0],args[1]))
    
    postings_file.close()

    return tf_weights


'''
For all documents, sums up term frequency weights used in that document and normalizes the length
'''
def NormalizeDocLength(tf_weights):
    normalized_docs = []
    #Do not mutate parameter
    tf_w = tf_weights[:]
    #Sort tf_w to iterate for every document
    tf_w.sort(key=lambda x:x.docId, reverse=False)
    doc_amount =  tf_w[len(tf_w)-1].docId

    #Check if it is sorted correctly
    #print("tf_Weights sorted on docIDs")
    #for tf in tf_w:
    #    print(tf)
    #print(len(tf_w),"\n++++++++++++++++++++++++++++++++++++++++++++\n")

    for i in range(len(tf_w)):
        docId = tf_w[i].docId
        tf_weight = tf_w[i].tf_weight
        document = DocumentLength(docId,tf_weight)
        
        #Update normalized length if docId exist
        ##Insert document id with normalized value if docId does not exist
        if any( doc.docId == docId for doc in normalized_docs  ): 
            normalized_docs[docId].UpdateLength(tf_weight)
        else:                       
            normalized_docs.append(document)

        

    return normalized_docs
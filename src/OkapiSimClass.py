class OkapiSim:
    def __init__(self,docId):
        self.docId = docId
        self.similarity = 0
        #Adding fields to keep ti,wi,dti,qi
        self.query_data = []


    def assignSimilarity(self,similarity):
        self.similarity = similarity

    def addQueryData(self,q_word):
        self.query_data.append(q_word)

    def    __str__(self):
        return "DocId: " + str(self.docId) + " , Similarity: " + str(self.similarity)

class QueryWord:
    def __init__(self,ti,wi,dti,qti):
        self.ti = ti
        self.wi = wi
        self.dti = dti
        self.qti = qti

    def    __str__(self):
        return  "Term:" + str(self.ti) + "  Wi:" + str(self.wi) + "  Dti:" + str(self.dti) + "  Qti:" + str(self.qti)
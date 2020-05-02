import math
class Result:
    def __init__(self, docId):
        self.docId  = docId
        self.cos_sim= 0
        self.query_data = [] #Fill query_word data related with this doc as this document contains different query words

    def assignSimilarity(self,similarity):
        self.cos_sim = similarity

    def addQueryData(self,q_info):
        self.query_data.append(q_info)

    def __str__(self):
        return "DocId: " + str(self.docId) + " , cos_sim: " + str(self.cos_sim)
    def __lt__(self, other):  # override <操作符
        if self.cos_sim < other.cos_sim:
            return True
        return False

class QueryInfo:
    def __init__(self, token, tf, idfw):
        self.token  = token
        self.tfw    = 1 + math.log10(int(tf))
        self.idfw   = idfw
        self.qi     = float(self.tfw * idfw)

    def __str__(self):
        return "token: " + str(self.token) + " , tfw: " + str(self.tfw) + " , idfw: " + str(self.idfw) + " , qi: " + str(self.qi)


class QueryWord:
    def __init__(self, ti, wtq, wtd, length):
        self.ti  = ti
        self.wtq = wtq
        self.wtd = wtd
        self.normalized_doc_length = length

    def __str__(self):
        return "Term:" + str(self.ti) + " , Wtq:" + str(self.wtq) + " , Wtd:" + str(self.wtd) + " , Length:" + str(self.normalized_doc_length)
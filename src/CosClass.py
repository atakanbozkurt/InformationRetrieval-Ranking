import math
class Result:
    def __init__(self, docId, cos_sim):
        self.docId  = docId
        self.cos_sim= cos_sim

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
        self.qi     = self.tfw * idfw
    def __str__(self):
        return "token: " + str(self.token) + " , tfw: " + str(self.tfw) + " , idfw: " + str(self.idfw) + " , qi: " + str(self.qi)
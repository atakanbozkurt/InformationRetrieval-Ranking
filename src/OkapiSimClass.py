class OkapiSim:
    def __init__(self,docId):
        self.docId = docId
        self.similarity = 0


    def    __str__(self):
        return "DocId: " + str(self.docId) + " , Similarity: " + str(self.similarity)
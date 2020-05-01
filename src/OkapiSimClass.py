class OkapiSim:
    def __init__(self,docId):
        self.docId = docId
        self.similarity = 0

    def assignSimilarity(self,similarity):
        self.similarity = similarity

    def    __str__(self):
        return "DocId: " + str(self.docId) + " , Similarity: " + str(self.similarity)
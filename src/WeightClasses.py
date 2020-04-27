import math

class DocumentLength:
    def __init__(self,docId,raw_tf,tf_weight):
        self.docId = docId
        self.raw_tf_sum = raw_tf
        self.tf_sq_sum = (tf_weight)*(tf_weight)
        self.weighted_length = 1/(math.sqrt(self.tf_sq_sum))
        

    def __str__(self):
        return "DocId: " + str(self.docId) + " Raw Tf Sum: " + str(self.raw_tf_sum) + " , Weighted Length: " + str(self.weighted_length)
    
    def UpdateLength(self,raw_tf,tf_weight):
        self.raw_tf_sum = self.raw_tf_sum + raw_tf
        self.tf_sq_sum = self.tf_sq_sum + (tf_weight)*(tf_weight)
        self.weighted_length = 1/(math.sqrt(self.tf_sq_sum))
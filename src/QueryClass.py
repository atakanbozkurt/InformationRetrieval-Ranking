class QueryTerm: #Encapsulates every unique query term
    def __init__(self,term):
        self.term = term
        self.tf = 1

    def incrementTf(self):
        self.tf = self.tf + 1

    def    __str__(self):
        return "Term: " + str(self.term) + " , Tf: " + str(self.tf)

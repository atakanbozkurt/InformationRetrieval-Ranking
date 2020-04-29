class Query:
    def __init__(self,):



    def __str__(self):


class QueryTerm:
    def __init__(self,term,tf):
        self.term = term
        self.tf = tf

    def    __str__(self):
        return "Term: " + str(self.term) + "Tf: " + str(self.tf)
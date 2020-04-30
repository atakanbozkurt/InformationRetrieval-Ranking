<<<<<<< HEAD
class QueryTerm:
    def __init__(self,term):
        self.term = term
        self.tf = 1

    def incrementTf(self):
        self.tf = self.tf + 1

    def    __str__(self):
        return "Term: " + str(self.term) + " , Tf: " + str(self.tf)
=======
class Query:
    def __init__(self,):



    def __str__(self):


class QueryTerm:
    def __init__(self,term,tf):
        self.term = term
        self.tf = tf

    def    __str__(self):
        return "Term: " + str(self.term) + "Tf: " + str(self.tf)
>>>>>>> 9bb8b00c901bd3192d357daf5035f047aa54ed2b

from Tokenizer import TokenizeLine
from QueryClass import QueryTerm

def SplitQuery(query):
    terms = TokenizeLine(query)
    q_terms = []
    
    for i in range(len(terms)):
        if(i==0):
            q_terms.append(QueryTerm(terms[i]))
        else:
            found = False
            for j in range(len(q_terms)):
                if q_terms[j].term == terms[i]:
                    q_terms[j].incrementTf()
                    found = True
            if found == False:
                q_terms.append(QueryTerm(terms[i]))
        
        
    print("query: ",query)
    print("terms: ")
    for q in q_terms:
        print(q)

    return q_terms


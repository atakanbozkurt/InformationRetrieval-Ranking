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
        
        
    #print("query: ",query)
    #print("terms: ")
    #for q in q_terms:
    #    print(q)

    return q_terms

'''
Auxilary function: Used to merge document list for every different query term.
Output: Output will only contain unique docId's that contain at least one of the query term
Goal: Preparation for Document At a Time
'''

def GetDocList(query_list, dictionary, postings_list):

    doc_list = [] #Contains the documents id's that have this term
    for q in query_list:
        #print("New Query Word: ",q)
        if dictionary.get(q.term) != None:
            index = dictionary[q.term].offset
            doc_freq = dictionary[q.term].doc_freq
            for i in range(index,index+doc_freq):
                posting = postings_list[i]
                doc_list.append(posting.docId)
                #print("i: ", i, "  docId:", posting.docId)
            '''
            for i in range(0, doc_freq):
                posting = postings_list[index]
                doc_list.append(posting.docId)
            '''
    doc_list = sorted(set(doc_list), key=doc_list.index)
    doc_list.sort()


    #print("\ndoc_list sorted\n")
    #for doc in doc_list:
    #    print(doc)


    return doc_list



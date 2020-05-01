from VectorSimClass import Result, QueryInfo
from IndexerClasses import PostingItem
from Tokenizer import TokenizeLine
import math

def FindCosSimilarity(query , doc_lengths , dictionary , postings_list):
    tokens = TokenizeLine(query)
    #Find postings list for query terms
    terms_postings = GetAllPostings(dictionary,tokens)



    return


def GetAllPostings(dictionary,tokens):
    print("\nGetAllPostings")
    all_postings = []
    for i in range(len(tokens)):
        term = tokens[i]
        dict_entry = dictionary.get(term)
        #Retrieve postings list if term exist in dictionary
        if(dict_entry):
            term_posting = GetPostings(dict_entry)
            #all_postings.append(term_posting)
            pass
        else:
            #print("Term: ",term, " does not exist in the dictionary")
            pass
    return all_postings

def GetPostings(dict_entry):
    #Length of postings list should be the size of document frequency
    postings_list = []
    term = dict_entry.term
    offset = int(dict_entry.offset)
    doc_freq = dict_entry.doc_freq
    print("term: ",term,"  docfreq: ",doc_freq," offset: ",offset)
    '''
    for i in range(0,int(doc_freq)):
        #postings_item = tf_weights[offset]
        offset += 1
        docId = postings_item.docId
        tf_weight = postings_item.tf_weight
        document = Document(term, docId , tf_weight) 
        #print(document , " Doc_freq: " , doc_freq ,  " Offset: ", offset )
        postings_list.append(document)
    '''   

    return postings_list

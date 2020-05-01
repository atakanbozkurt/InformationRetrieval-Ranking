<<<<<<< HEAD
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
=======
from CosClass import Result, QueryInfo
import math


def FindCosSimilarity(terms_postings, tokens, normalized_docs, dictionary, postings_list):
    '''
    #If you need to work with documents
    print("Largest doc Id in collection: " , normalized_docs[-1].docId)
    print("Available number of documents in the collection" , normalized_docs[-1].docId + 1)

    print("From dictionary find document frequency by using command below")
    term_entry = dictionary.get("ahead")
    print("ahead doc freq: ", term_entry.doc_freq)
    '''

    cos_sim = []
    tokens_info = []
    N_Q = 0
    for i in tokens:
        N_Q += i.tf

    N_D = len(normalized_docs)

    tftd = {}
    df = {}
    idfw = {}
    for token in tokens:
        tftd[token]= token.tf
        entry = dictionary.get(token.term)
        if entry != None:
            df[token] = entry.doc_freq
        else:
            df[token] = 0

        if df[token] == 0:
            idfw[token] = 0
        else:
            idfw[token] = math.log10(N_Q / int(df[token]))
        # print(N_Q/int(df))
        info = QueryInfo(token, tftd[token], idfw[token])
        tokens_info.append(info)
    # for i in tokens_info:
    #     print(i)


    # open one file each time
    for i in terms_postings:
        qidi = 0
        n_sqr_di = 0
        for token in tokens:
            entry = dictionary.get(token.term)
            if entry != None:
                offset = entry.offset
                qi = float(searchqi(token.term, tokens_info))
                print("qi:" + str(qi))
                di = float(postings_list[offset].tf_weight) * math.log10(N_D / int(entry.doc_freq))
                # print(math.log10(N_D/int(dictionary.get(documents.term).doc_freq)))
                # print("qi:",qi,"\tdi:",di)
                # qidi = qidi + qi * di  # the sum of qi * di
                n_sqr_di = n_sqr_di + math.pow(di, 2)  # the sum of di**2
        # if qidi != 0:
        # print(str(qidi) + " " + str(n_sqr_di))
        sim = qidi / math.sqrt(n_sqr_di)
        result = Result(i, sim)
        cos_sim.append(result)

    # need sort result by sim
    cos_sim.sort(reverse=True)

    return cos_sim


def searchqi(term, tokens_info):
    for i in tokens_info:
        if term == i.token:
            return i.qi

>>>>>>> 0582bfc43fc0ffcaff7a96b91d27970889b26c21

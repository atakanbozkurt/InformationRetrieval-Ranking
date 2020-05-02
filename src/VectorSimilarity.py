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
    tokens_info = {}
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
        tokens_info[token] = info
    #for i in tokens_info:
    #    print(i)


    # open one file each time
    for i in terms_postings:
        qidi = 0
        n_sqr_di = 0
        for token in tokens:
            entry = dictionary.get(token.term)
            if entry != None:
                offset = entry.offset
                doc_freq = entry.doc_freq
                tfw = 0;

                for j in range(0, doc_freq):
                    posting = postings_list[offset]
                    if (posting.docId == i):
                        tfw = posting.tf_weight
                    else:
                        offset += 1
                qi = tokens_info[token].qi
                # print("qi:" + str(qi))
                di = float(tfw) * math.log10(N_D / int(entry.doc_freq))
                # print(math.log10(N_D/int(dictionary.get(documents.term).doc_freq)))
                # print("qi:",qi,"\tdi:",di)
                qidi = qidi + qi * di  # the sum of qi * di
                n_sqr_di = n_sqr_di + math.pow(di, 2)  # the sum of di**2
        # if qidi != 0:
        # print(str(qidi) + " " + str(n_sqr_di))
        sim = qidi / math.sqrt(n_sqr_di)
        result = Result(i, sim)
        cos_sim.append(result)

    # need sort result by sim
    cos_sim.sort(reverse=True)

    return cos_sim



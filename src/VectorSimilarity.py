from CosClass import Result, QueryInfo, QueryWord
import math
import os.path


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
    N_Q = len(normalized_docs)
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


    '''
    #OLD VERSION WITHOUT SAVING QUERY DATA
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
    '''


    for i in terms_postings:
        result = Result(i)
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

                doc_length = normalized_docs[i].length

                q_word = QueryWord(tokens_info[token].token,tokens_info[token].tfw,di,doc_length)
                result.addQueryData(q_word)
        # if qidi != 0:
        # print(str(qidi) + " " + str(n_sqr_di))
        sim = qidi / math.sqrt(n_sqr_di)
        result.assignSimilarity(sim)

        #result = Result(i, sim)
        cos_sim.append(result)

    return cos_sim


def BringVectorTop10(cos_similarities):
    file = os.path.abspath("../output_files/vectorTop10.txt")
    f = open(file, "w")
    cos_similarities.sort(key=lambda x: x.cos_sim, reverse=True)
    top10k = []
    print("Vector Top10k")
    for i in range(0,len(cos_similarities)):
        doc = cos_similarities[i]
        if(i<10):
            docId = doc.docId
            similarity = doc.cos_sim
            q_data = doc.query_data
            for data in q_data:
                print("Ti:",data.ti, " Wtq:", data.wtq, " Wtd:", data.wtd , " Length:",data.normalized_doc_length)
                f.write("Ti:" + str(data.ti) + "  Wtq:" + str(data.wtq) + "  Wtd:" + str(data.wtd) + "  Length:" + str(data.normalized_doc_length) + "\n")
            print("DocId: ", docId, " Cos Similarity:", similarity)
            f.write("DocId:" + str(docId) + " Cos Similarity:" + str(similarity) + "\n")
        else:
            break
    f.close()
    return top10k



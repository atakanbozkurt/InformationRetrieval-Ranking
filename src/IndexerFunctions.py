import os.path
from IndexerClasses import Document,DictionaryTerm,PostingItem
from Tokenizer import TokenizeLine
'''
Read (tokenize while reading) and store documents
'''
def ReadDocuments():
    documents = []
    title_path = os.path.abspath("../input_files/200_title.txt")
    title_file = open(title_path,encoding='utf8')
    content_path = os.path.abspath("../input_files/200_content.txt")
    content_file = open(content_path,encoding='utf8')

    #Test file paths
    test_title_path = os.path.abspath("../input_files/test_title.txt")
    test_title_file = open(test_title_path,encoding='utf8')
    test_content_path = os.path.abspath("../input_files/test.txt")
    test_content_file = open(test_content_path,encoding='utf8')


    docId=0
    for line in content_file:
        title = title_file.readline()
        doc = Document(docId,title,TokenizeLine(line))
        documents.append(doc)
        docId += 1

    '''
    #Use below for test files
    for line in test_content_file:
        title = test_title_file.readline()
        doc = Document(docId,title,TokenizeLine(line))
        documents.append(doc)
        docId += 1
    '''

    title_file.close()
    content_file.close()
    test_content_file.close()

    return documents



'''
Produce Dictionary and Postings List 
'''
def IndexDictionaryAndPostings(documents):
    dictionary_and_postings = []

    #Generate term-docId pairs
    term_list = GeneratePair(documents)
    #Sort term-docId pairs
    term_list.sort(key=lambda val: (val[0],val[1]))
    #Merge term-docId pairs into (term,docId,postings) format. postings->(docId,tf)
    dict = MergePairs(term_list)
    #Build dictionary
    dictionary = BuildDictionary(dict)
    #Build postings
    postings_list = BuildPostings(dict,documents)

    '''
    print("Term-docId pairs")
    for term in term_list:
        print(term)

    print("\nPairs sorted:")
    for term in term_list:
        print(term)
    
    print("\nDictionary")
    for dic in dict:
        print(dic)
    
    for e in dictionary:
        print(e,"--> ", dictionary[e])
    
    for post in postings_list:
        print(post)
    '''
    
    dictionary_and_postings.append(dictionary)
    dictionary_and_postings.append(postings_list)

    return dictionary_and_postings

'''
Auxilary function: Produces term-docId pairs
'''
def GeneratePair(documents):
    term_list = []
    for doc in documents:
        words = doc.content
        docId = doc.docId
        for word in words:
            term_list.append((word,docId))
    return term_list

'''
Auxilary function: Merges term-docId pairs
'''
def MergePairs(term_list):
    dictionary = []

    for i in range(0, len(term_list)):
        t = term_list[i]  # current term
        t_exist = False

        for j in range(0, len(dictionary)):
            dic = dictionary[j]

            if dic[0] == t[0]: #if term is found in dictionary
                t_exist = True
                docId = t[1]
                #print("term " , t[0] , " exist in dictionary")
                #check if docId exist in postings list of term in dictionary
                docId_exist = False
                index = 0
                p_list = dic[2]

                #print("checking postings list")
                for i in range(0,len(p_list)):
                    dId_tf = p_list[i]
                    #print("i: " , i , "   dId_tf: ",dId_tf)
                    if docId == dId_tf[0]:
                        docId_exist = True
                        index = i
                        #print("new docId: ",docId , " exist. index: ", index)
                        break
                
                if docId_exist == True: #only increment term frequency for given docId
                    #print("increment term frequency for index: ",index)
                    dId_tf = p_list[index]
                    dId_tf = list(dId_tf)
                    #print("term: " , dic[0] , "posting: " , dic[2])
                    dId_tf[1] = dId_tf[1] + 1
                    dic[2][index] = dId_tf
                else:                  #increment document frequency, add new pair to posting list
                    #print("new docId: ",docId , " does not exist.")
                    new_pair = (docId,1)
                    #print("adding new pair: ",new_pair , " to posting")
                    dic[2].append(new_pair)
                    dic[1] = dic[1] + 1
                    #print("result for new term",dic)

                '''
                if docId in dic[2]:
                    pass
                else:
                    dic[2].append(docId)
                    dic[2].sort()
                    dic[1] = dic[1] + 1
                '''

        if not t_exist:
            #post_list = [t[1]]
            #generate pair for postings list and append new entry to dictionary in following format
            #['term',docFreq,[(docId,termFreq), ...]]
            post_list = []
            docId_termFreq = (t[1],1)
            post_list.append(docId_termFreq)

            new_row = [t[0], 1, post_list]
            
            #print("adding new ",new_row)
            dictionary.append(new_row)

    return dictionary

'''
Auxilary function: Produce dictionary.txt and hash table to be used
'''
def BuildDictionary(dict):
    dictionary = {}

    file = os.path.abspath("../output_files/dictionary.txt")
    f = open(file,"w")
    offset = 0
    for item in dict:
        term = item[0]
        doc_freq = item[1]
        #Build dictionary
        dictionary[term] = DictionaryTerm(term,doc_freq,offset)
        #Write to file
        f.write(term + "\t" + str(doc_freq) + "\t" + str(offset) + "\n")  # USE \n TO SET EOF
        offset = offset + item[1]
    f.close()
    return dictionary

'''
Auxilary function: Produce postings.txt and postings list to be used
'''
def BuildPostings(dict,documents):
    postings_list = []
    file = os.path.abspath("../output_files/postings.txt")
    f = open(file,"w")
    for entry in dict:
        term = entry[0]
        doc_freq = entry[1]
        postings = entry[2]
        #print(entry)
        for i in range(doc_freq):
            doc = postings[i]
            docId = doc[0]
            tf = doc[1]
            posting = PostingItem(docId,tf)
            #print("doc:" ,doc, " docId:" , docId , " tf:" , tf )
            #print(posting)
            postings_list.append(posting)
            f.write(str(posting.docId) + "\t" + str(posting.tf) + "\t" + str(posting.tf_weight) + "\n")
        #print("\n")
            
    f.close()
    return postings_list
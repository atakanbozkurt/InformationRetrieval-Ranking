from LengthClasses import DocumentLength

'''
Uses DocumentLength class to store raw tf and weighted tf for each document in an array
'''
def FindDocLenghts(documents,postings_list):
    p_list = postings_list[:] #Do not mutate postings list
    doc_lengths = []

    #Sort postings list based on docId in ascending order, find out how many different documents exist 
    #For each documentid, sum um raw tf, also normalize document with weights

    #for entry in p_list:
    #    print(entry)
    p_list.sort(key=lambda x:x.docId, reverse=False)
    #print("Sorted postings list")
    #for entry in p_list:
    #    print(entry)

    doc_amount =  p_list[len(p_list)-1].docId #-1 from real doc amount because of starting index = 0
    
    for i in range(len(p_list)):
        docId = p_list[i].docId
        raw_tf = p_list[i].tf
        tf_weight = p_list[i].tf_weight
        document = DocumentLength(docId,raw_tf,tf_weight)
        
        #Update normalized length if docId exist
        ##Insert document id with normalized value if docId does not exist
        if any( doc.docId == docId for doc in doc_lengths  ): 
            doc_lengths[docId].UpdateLength(raw_tf,tf_weight)
        else:                       
            doc_lengths.append(document)

    #print("Doc lengths")
    #for doc_length in doc_lengths:
    #    print(doc_length)

    return doc_lengths

'''
Finds avg. doc. length in terms of raw tf
'''
def FindAvgLength(doc_lengths):
    sum = 0
    for doc in doc_lengths:
        sum = sum + doc.raw_tf_sum
    avg_length = sum/len(doc_lengths)
    #print("sum: ",sum, "  doc_num: " , len(doc_lengths) , "  Avg length:" , avg_length)
    
    return avg_length

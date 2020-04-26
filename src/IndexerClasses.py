class Document:
    def __init__(self,docId,title,content):
        self.docId = docId
        self.title = title
        self.content = content
        

    def __str__(self):
        return "DocumentId: " + str(self.docId) + "\nTitle: " + str(self.title) + "Content: " + str(self.content) + "\n"


class DictionaryTerm:
    def __init__(self,term,doc_freq,offset):
        self.term = term
        self.doc_freq = doc_freq
        self.offset = offset
    
    def __str__(self):
        return "Term: " + str(self.term) + " , Doc. Freq: " + str(self.doc_freq) + " , Offset: " + str(self.offset)


#class PostingItem
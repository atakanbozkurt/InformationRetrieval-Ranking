class Document:
    def __init__(self,docId,title,content):
        self.docId = docId
        self.title = title
        self.content = content
        

    def __str__(self):
        return "DocumentId: " + str(self.docId) + "\nTitle: " + str(self.title) + "Content: " + str(self.content) + "\n"

#class DictionaryTerm
#class PostingItem
import os.path
from IndexerClasses import Document
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

    docId=0
    for line in content_file:
        title = title_file.readline()
        doc = Document(docId,title,TokenizeLine(line))
        documents.append(doc)
        docId += 1
    
    title_file.close()
    content_file.close()

    return documents

def IndexDictionaryAndPostings(documents):
    dictionary_and_postings = []
    return dictionary_and_postings
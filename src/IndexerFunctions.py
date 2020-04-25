import os.path
from nltk.stem.porter import PorterStemmer
from IndexerClasses import Document
'''
Read, tokenize and store documents
'''
def ReadDocuments():
    documents = []
    title_path = os.path.abspath("../input_files/200_title.txt")
    title_file = open(title_path,encoding='utf8')
    content_path = os.path.abspath("../input_files/200_content.txt")
    content_file = open(content_path,encoding='utf8')

    for line in content_file:
        title = title_file.readline()
        doc = Document(title,TokenizeDocument(line))
        documents.append(doc)
    
    title_file.close()
    content_file.close()

    return documents

'''
Tokenize document and return list of words.
'''
def TokenizeDocument(content):
    porter_stemmer = PorterStemmer()
    # 1)Input : "A new hi-gh for the sto-ck market?"
    # 2)Output : ["a","new","high","for","the","stock","market"]
    # remove all punctuation except "*"
    need_to_remove = r"""!"#$%&'()‘’+,-./:;<=>?@[\]^_`{|}~"""
    trantab = str.maketrans({key: None for key in need_to_remove})
    j = str.lower(content.translate(trantab))  # same as j = j.replace('single punctuation','') for many line & lower
    # print(line2)
    x = j.split()
    number_with_space = ""
    number_exist = False
    result = []
    # ADD ELEMENTS FOR EACH TITLE WITH LOGIC TO DISPOSE NUMBER WITH SPACE (EG. "607 123 4567")
    for i in x:
        if number_exist and not is_number(i):
            result.append(str(number_with_space))
            result.append(porter_stemmer.stem(i))
            number_with_space = ""
            number_exist = False
        elif not number_exist and not is_number(i):
            result.append(porter_stemmer.stem(i))
            number_exist = False
        elif is_number(i) and not number_exist:
            number_exist = True
            number_with_space = number_with_space + '' + str(i)
        elif is_number(i) and number_exist:
            number_with_space = number_with_space + '' + str(i)
    if number_exist:
        result.append(str(number_with_space))
        #     print(i)
    return result

'''
Auxiliary function to tokenize content.
'''
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False
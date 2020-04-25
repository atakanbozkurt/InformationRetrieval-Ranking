class Document:
    def __init__(self,title,content):
        self.title = title
        self.content = content

    def __str__(self):
        return "Title: " + str(self.title) + "Content: " + str(self.content) + "\n"

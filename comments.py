class Comment():
    def __init__(self, 
                 id, 
                 score, 
                 author, 
                 dateTime, 
                 text, 
                 organization=None):
        self.id = id
        self.score = score
        self.author = author
        self.dateTime = dateTime
        self.text = text
        self.organization = organization





def parseLists(scores, names, texts, dates):
    list_of_objects = []
    for i, (score, name, text, date) in enumerate(zip(scores, names, texts, dates)):
        obj = Comment(i, score, name, text, date) 
        list_of_objects.append(obj)

    return list_of_objects
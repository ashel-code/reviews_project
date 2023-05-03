import tokenizing as tkn

def run_analysis(comments):
    texts = [obj.text for obj in comments]

    tkn.tok(texts)


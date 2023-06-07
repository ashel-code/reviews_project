import math
import pickle5 as pickle
import pymorphy2
import nltk


def read_list():
    with open('./data/texts.bin', 'rb') as fp:
        n_list = pickle.load(fp)
        return n_list


texts = read_list()
fdist_sw = nltk.probability.FreqDist(texts)
morph = pymorphy2.MorphAnalyzer()


def get_prob(input):
    res = 1
    n = 0
    lst = input.split()
    for i in lst:
        ob = morph.parse(i)[0].normal_form
        if ob in fdist_sw:
            # print(fdist_sw[ob], len(final_texts))
            res *= fdist_sw[ob] / len(texts)
            n += 1
    if n == 0:
        return 0
    return math.pow(res, 1/n)


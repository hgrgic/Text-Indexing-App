import re
import matplotlib.pyplot as plt
import numpy as np

from SinglyLinkedList import SLinkedList, SNode
from StringUtility import count_word_occurrence


def parse_article(articleName):
    with open(articleName) as f:
        articles = []
        articleText = ""
        articleFound = False
        for line in f.readlines():
            line = line.rstrip()
            if "</doc>" == line:
                articles.append(articleText)
                articleText = ""
                articleFound = False
            if articleFound:
                tempText = line.lower();
                tempText = re.sub(r"<[^>]*>", " ", tempText)
                tempText = re.sub(r"'s", "", tempText)
                tempText = re.sub(r"' ", "", tempText)
                tempText = re.sub(r" '", "", tempText)
                tempText = re.sub(r'[;|-|_|:|<|>|(|)|+|/|*|"|?|!|.|,|(|)]', "", tempText)
                articleText += tempText
            if "<doc>" == line:
                articleFound = True
    return articles

def index_articles(articleList):
    occurance_list = []
    index_dictionary = {}
    uber_string = ""
    for article in articleList:
        uber_string += article

    for word in uber_string.split():
        if word not in index_dictionary:
            sList = SLinkedList()
            word_sum = 0;
            for i in range(0, articleList.__len__()):
                occurs = count_word_occurrence(word, articleList[i])
                if occurs > 0:
                    sNode = SNode(i+1, occurs)
                    sList.__add__(sNode)
                    index_dictionary[word] = sList
                    word_sum += occurs
            occurance_list.append(word_sum)

    return {"dict":index_dictionary, "stat":occurance_list}


def print_indexed_dict(dictionary):
    for item in dictionary:
        print "[" + item + "]" + dictionary[item].traverse_list()

def plot_distribution_histogram(list_occurances):
    bins = np.arange(max(list_occurances)) - 0.5
    plt.hist(list_occurances, bins, color='g', linewidth=0.75, edgecolor='black')
    plt.title("Word distributions")
    plt.xlabel("Total count of words")
    plt.ylabel("Frequency of total count")
    plt.show()



parsed_articles = parse_article('collection.txt')
indexing_map = index_articles(parsed_articles)
print_indexed_dict(indexing_map["dict"])
plot_distribution_histogram(indexing_map['stat'])

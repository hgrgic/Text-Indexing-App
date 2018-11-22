import re


def count_word_occurrence(word, article_text):
    list = re.findall("\s" + re.escape(word) + "\s", article_text)
    return len(list)
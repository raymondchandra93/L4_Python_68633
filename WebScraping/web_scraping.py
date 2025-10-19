from bs4 import BeautifulSoup
import requests
import string
from collections import Counter

import numpy as np
import matplotlib.pyplot as plt

# -- Phase 1 --

url = "https://books.toscrape.com/"
page_text = requests.get(url).text

# print(page_text)

# -- Phase 2 --

soup = BeautifulSoup(page_text, "html.parser")

# extract title
title = soup.title.string
# print(title)

# extract sub-title
sub_title = soup.find("small")
# print(sub_title.text)

# extract the whole warning
warning_sentence = soup.find("div", class_="alert")
print(warning_sentence.text)

# extract warning text
warning_word = soup.find("div", class_="alert").find("strong")
print(warning_word.text)

# -- Phase 3 -- 

def get_words_list(url):
    r = requests.get(url).text
    soup = BeautifulSoup(r, "html.parser")

    # Looking for all the titles in the web page
    titles = soup.findAll("h3")
    text = ""
    for title in titles:
        text += title.text.lower() + " "
    print(text)

    # remove punctuation
    for char in string.punctuation:
        text = text.replace(char, "")
    print(text)

    # split into words
    text_list = text.split()
    print(text_list)

    # count most common words
    word_counts = Counter(text_list).most_common(50)
    print(word_counts)

    return word_counts


# --- Phase 4 ---

def plot_words(words_list, title):

    # separate words and numbers
    words = []
    numbers = []
    for (w, n) in words_list:
        words.append(w)
        numbers.append(n)

    # making an index from 0 until number of words
    index = np.arange(len(words)) 

    # make the bar chart
    fig = plt.figure()
    plt.bar(index, numbers)
    plt.xticks(index+.5, words, rotation="vertical", size="x-small")
    plt.title(title)
    fig.savefig(title)

url = input("Please enter the URL to scrape -> ")
word_counts = get_words_list(url)
plot_words(word_counts, "Word Counts")
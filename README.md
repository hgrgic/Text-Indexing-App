# Text Indexing Application
## Abstract
This application is created in order to index all the words in a given data set.
For now the application is created to search through a predetermined text collection, but it can be easily modified to 
be applicable to any input source. 

## Architecture
The application is composed out of three main scripts.
* _ParseArticle.py_ is composed out of several functions that execute main logical processing in this assigment.
    * `def parse_article()` is in charge of parsing text file into a list of strings that represent all of the text 
    found in a respective article. While it is also reading article line by line, it is also executing text pre-processing 
    by applying specified regex instructions.
    * `def index_articles()` is a function in charge of creating a returning a dictionary of indexed words with the count
    of occurrences in each article. This function also calculates the total number of occurrences for each word
    so that it can be easily represented on a histogram.
    * `print_indexed_dict()` is a function that outputs to the command shell the frequencies of a count for each word that
    has been found in the article. 
    * `plot_distribution_histogram()` is a function that takes a list of frequencies and plots them in the form of histogram.
    This histogram visualizes the distribution of words across the entire provided data set.
* _StringUtility.py_ is a helper script that is currently holding only a single function. This
    script file is intended to hold any function that is dealing with text processing, but at the same time it is also to be self-sufficient 
    without any other connected logic. In some way all of the methods in this script are encapsulated and could be regarded 
    as static if speaking in OOP terms.
    * `count_word_occurrence()` is a function that takes two parameters, and uses regex to match how many times a `word` 
    parameter occurs in a `article_text` parameter. This number is returned and used for any necessary processing elsewhere.
* _SinglyLinkedList.py_ holds model classes for a SinglyLinkedList data structure. This model class is composed out of two classes.
    * `class SNode` represents a singly linked node that holds its data, and a reference to next node.
    * `class SLinkedList` is slightly more complex, but still has two fields. 
        * `headval` represents a head value of the list.
        * `lastelement` represents a last element in the linked list.
      
      Beside these fields `SLinkedList` class has the following functions:
      * `__add__` this is a standard add overridden function. It is overridden in a way that every newly added node is linked
      to the previous node, and takes place of the last element in the list.
      * `traverse_list` is a function that that traverses the lists of all the linked elements,
      and formats a string that part of the requirement.

## Execution
In order to execute this code, it is necessary to provide it with data collection. Example data collection can be found
in `resource/collection.txt` file. Currently, the application is written in a way that it pre-process the format of the 
mentioned text collection. The code can be extended in a way that only the pre-processing regex needs to be changed in order to 
extract the need text data. Everything else, should work fine if the requirements are the same.

To execute this code just run from a command line shell `PareArticle.py` script file.

##Author
* Hrvoje Grgic 

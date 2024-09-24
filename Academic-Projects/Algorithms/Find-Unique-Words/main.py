# extract unique values from an unsorted list, given a sorted list

import math


def new_words(words, word_list):
    check_passed = input_check(words, word_list)
    if not check_passed:
        return None
    new_word_list = check_words(words, word_list)
    return new_word_list


def input_check(words, word_list):
    if (words is None) or (word_list is None):
        return False
    if (type(words) is not tuple) or (type(word_list) is not tuple):
        return False
    if (not valid_tuple_check(words) or not valid_tuple_check(word_list)):
        return False
    return True


def valid_tuple_check(list):
    if (list == ()):
        return True
    for word in list:
        if (type(word) is not str):
            return False
    return True


def individual_check(word, word_list):
    word_list_len = len(word_list)
    if (word_list_len == 0):
        return True
    word_list_middle = word_list[word_list_len // 2]
    if (word_list_len == 1):
        if ((word_list_middle.lower() != word.lower())):
            return True
    elif (word_list_middle.lower() == word.lower()):
        return False
    elif ((word_list_middle.lower() > word.lower())):
        return individual_check(word, word_list[:(word_list_len // 2)])
    elif ((word_list_middle.lower() < word.lower())):
        return individual_check(word, word_list[(word_list_len // 2) + 1:])


def check_words(words, word_list):
    new_word_list = []
    for word in words:
        is_new = individual_check(word, word_list)
        if (is_new):
            new_word_list.append(word)
    if (len(new_word_list) == 0):
        return ()
    new_word_tuple = tuple(new_word_list)
    return new_word_tuple

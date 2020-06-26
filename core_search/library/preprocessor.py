"""
Author: Ranit Dey
Description: Text pre processing utilities
"""
import re
import string


def make_alphanumeric(target):
    pattern = re.compile('[\W_]+')
    return pattern.sub("", target)


def cleanup_punctuation(target):
    return target.translate(str.maketrans("", "", string.punctuation))


def tokenize(text):
    text = cleanup_punctuation(text)
    return text.split()


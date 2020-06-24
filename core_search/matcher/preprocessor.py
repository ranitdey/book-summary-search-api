"""
Author: Ranit Dey
Description: String pre processing utilities
"""
import re
import string


def make_alphanumeric(target):
    pattern = re.compile('[\W_]+')
    return pattern.sub("", target)


def cleanup_punctuation(target):
    return target.translate(string.maketrans("", ""), string.punctuation)


def tokenize(text):
    text = cleanup_punctuation(text)
    return text.split()


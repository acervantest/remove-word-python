import re


def remove_word_from_sentence(sentence, word):

    if type(sentence) not in [str]:
        raise TypeError('The sentence param must be a string')

    if type(word) not in [str]:
        raise TypeError('The word param must be a string')

    if not sentence:
        raise ValueError('sentence param cannot be empty.')

    if not word:
        raise ValueError('word param cannot be empty')

    return re.sub(r'\b{}\b'.format(word), '', sentence)


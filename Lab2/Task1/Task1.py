import re


def amount_of_sentences(text):
    return len(re.findall(r'[^.]{2}[.]\s', text)) + len(re.findall(r'[.]{3}\s', text))


def amount_of_non_declarative_sentences(text):
    return len(re.findall(r'[?!]\s', text))


def average_lenght_of_the_sentence(text):
    sentences = re.findall(r'(?=\s[A-Z0-9]).*?(?=[.?!]\s)', text)
    count_sentences = len(sentences)
    count_char = 0

    for sent in sentences:
        words = re.findall(r'(?=\w).*?(?=\W)', sent + ' ')
        for w in words:
            if len(w) == len(re.findall(r'\d', w)):
                continue
            count_char += len(w)

    return count_char / count_sentences


def average_lenght_of_the_word(text):
    words = re.findall(r'(?=\w).*?(?=\W)', text)
    count_words = len(words)
    count_char = 0

    for w in words:
        if len(w) == len(re.findall(r'\d', w)):
            continue
        count_char += len(w)

    return count_char / count_words


input_text = 'This is a text 123 a32 with some separators, and ' \
             'multiple sentences. Foo bar baz... ' \
             'Abbreviations can also appear a1b2c3 1234. ' \
             'Foo bar baz hello world hello world. Hi there. Hi... there. ' \
             'How are you? I am fine! '

print(amount_of_sentences(' ' + input_text + ' '))
print(amount_of_non_declarative_sentences(' ' + input_text + ' '))
print(average_lenght_of_the_sentence(' ' + input_text + ' '))
print(average_lenght_of_the_word(' ' + input_text + ' '))

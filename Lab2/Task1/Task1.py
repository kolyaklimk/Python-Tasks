import re


def amount_of_sentences(text):
    return len(re.findall(r'[^.]{2}[.]\s', text)) + len(re.findall(r'[.]{3}\s', text))


def amount_of_non_declarative_sentences(text):
    return len(re.findall(r'[?!]\s', text))


input_text = 'This is a text with some separators  and ' \
             'multiple sentences. Foo bar baz... ' \
             'abbreviations can also appear a1b2c3 1234. ' \
             'Foo bar baz hello world hello world. Hi there. Hi... there. ' \
             'How are you? I am fine! '

print(amount_of_sentences(input_text))
print(amount_of_non_declarative_sentences(input_text))

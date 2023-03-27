from unittest import TestCase, main
import Task1


class amount_of_sentences_test(TestCase):
    def test1(self):
        text = 'Our online English classes feature lots of useful learning materials and activities to help you ' \
               'develop your reading skills with confidence in a safe and inclusive learning environment. ' \
               'Practise reading with your classmates in live group classes, get reading support from a ' \
               'personal tutor in one-to-one lessons or practise reading by yourself at your own speed with a ' \
               'self-study course! Complex texts about! A?'
        self.assertEqual(Task1.amount_of_sentences(text), 1)

    def test2(self):
        text = 'Reading practice to help you understand simple information, words and sentences about known ' \
               'topics. Texts include posters, messages, forms and timetables.'
        self.assertEqual(Task1.amount_of_sentences(text), 2)


class amount_of_non_declarative_sentences_test(TestCase):
    def test1(self):
        text = 'Reading practice to help you understand simple information, words and sentences about known ' \
               'topics. Texts include posters, messages, forms and timetables.'
        self.assertEqual(Task1.amount_of_non_declarative_sentences(text), 0)

    def test2(self):
        text = 'Reading practice to help you understand long. Complex texts about! A? Wide variety of topics, ' \
               'some of which may be unfamiliar. Texts include specialised articles, biographies and summaries.'
        self.assertEqual(Task1.amount_of_non_declarative_sentences(text), 2)


class average_lenght_of_the_sentence_test(TestCase):
    def test1(self):
        text = 'Our online English classes feature lots of useful learning materials and activities to help you ' \
               'develop your reading skills with confidence in a safe and inclusive learning environment. ' \
               'Practise reading with your classmates in live group classes, get reading support from a ' \
               'personal tutor in one-to-one lessons or practise reading by yourself at your own speed with a ' \
               'self-study course! Complex texts about! A?'
        self.assertEqual(Task1.average_lenght_of_the_sentence(text), 84.75)

    def test2(self):
        text = 'Reading practice to help you understand long. Complex texts about! A? Wide variety of topics, ' \
               'some of which may be unfamiliar. Texts include specialised articles, biographies and summaries.'
        self.assertEqual(Task1.average_lenght_of_the_sentence(text), 31.0)


class average_lenght_of_the_word_test(TestCase):
    def test1(self):
        text = 'Reading practice to help you understand simple information, words and sentences about known ' \
               'topics. Texts include posters, messages, forms and timetables.'
        self.assertEqual(Task1.average_lenght_of_the_word(text), 6.142857142857143)

    def test2(self):
        text = 'Reading practice to help you understand long. Complex texts about! A? Wide variety of topics, ' \
               'some of which may be unfamiliar. Texts include specialised articles, biographies and summaries.'
        self.assertEqual(Task1.average_lenght_of_the_word(text), 5.535714285714286)


class top_K_repeated_N_grams_test(TestCase):
    def test1(self):
        text = 'Reading practice to help you understand simple information, words and sentences about known ' \
               'topics. Texts include posters, messages, forms and timetables.'
        self.assertEqual(Task1.top_K_repeated_N_grams(text, 3, 3),
                         [('reading practice to', 1), ('practice to help', 1), ('to help you', 1)])

    def test2(self):
        text = 'Reading practice to help you understand long. Complex texts about! A? Wide variety of topics, ' \
               'some of which may be unfamiliar. Texts include specialised articles, biographies and summaries.'
        self.assertEqual(Task1.top_K_repeated_N_grams(text, 1, 2), [('reading practice', 1)])


if __name__ == "__main__":
    main()

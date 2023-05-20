import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

import string


def get_tech_count(complete_text: str, count: int) -> list[tuple]:
    remove_chars = string.punctuation + "0123456789’—–"
    complete_text = complete_text.lower().translate({ord(i): " " for i in remove_chars})
    complete_text = re.sub(" +", " ", complete_text)

    words = word_tokenize(complete_text)
    all_stopwords = set(stopwords.words('english'))

    filtered_words = [word for word in words if word.isalpha() and word not in all_stopwords]

    return FreqDist(filtered_words).most_common(count)

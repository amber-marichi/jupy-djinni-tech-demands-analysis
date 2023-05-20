import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

import string


def clean_text(raw_text: str) -> str:
    remove_chars = string.punctuation + "0123456789’—–"
    cleaned_text = raw_text.lower().translate({ord(i): " " for i in remove_chars})
    cleaned_text = re.sub(" +", " ", cleaned_text)
    return cleaned_text


def get_tech_count(complete_text: str, count: int) -> list[tuple]:
    cleaned_text = clean_text(complete_text)
    words = word_tokenize(cleaned_text)
    all_stopwords = set(stopwords.words('english'))

    filtered_words = [word for word in words if word.isalpha() and word not in all_stopwords]

    return FreqDist(filtered_words).most_common(count)

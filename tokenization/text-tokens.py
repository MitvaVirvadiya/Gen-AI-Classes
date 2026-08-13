import spacy 

nlp = spacy.load("en_core_web_sm")

def tokenize_text(text):
    """
    Tokenizes the input text into individual tokens using spaCy.

    Args:
        text (str): The input text to be tokenized.

    Returns:
        list: A list of tokens extracted from the input text.
    """
    doc = nlp(text)
    tokens = [(token.text, token.is_alpha, token.is_digit, token.is_punct) for token in doc]
    return tokens

corpus = "Python is amazing. I have been learning NLP for 2 months!"
tokens = tokenize_text(corpus)
print(tokens)
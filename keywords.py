import spacy


def get_keywords(text, model_path):
    # Load the saved model
    nlp = spacy.load(model_path)

    # Process the input using the loaded model
    doc = nlp(text)

    # Access the entities recognized by the loaded model and separate them into two lists
    medical_professions = []
    keywords = []
    nouns = []
    verbs = []
    adjectives = []

    for ent in doc.ents:
        if ent.label_ == "MEDICAL_PROFESSION":
            medical_professions.append(ent.text)

    for token in doc:
        if token.pos_ == "NOUN" and token.text not in medical_professions:
            nouns.append(token.text)
        elif token.pos_ == "VERB" and token.text not in medical_professions:
            verbs.append(token.text)
        elif token.pos_ == "ADJ":
            adjectives.append(token.text)

    # Combine the lists of keywords and remove duplicates
    keywords = list(set(nouns + verbs + adjectives))

    return keywords, medical_professions

import spacy
from spacy.util import minibatch, compounding
import random


def import_data(file):

    IMPORT_DATA = open(file, "r").read()

    # convert single quotes to tilde
    IMPORT_DATA = IMPORT_DATA.replace("'", "~")

    # convert single quotes to parentheses
    TEMP_DATA = [eval(item.replace("'", "()")) for item in IMPORT_DATA.split("\n") if item]

    # convert tilde back to single quotes
    RETURN_DATA = [(item[0].replace("~", "'"), item[1]) for item in TEMP_DATA]

    return RETURN_DATA


def train_model(training_data, validation_data, n, best, version):

    train_data = import_data(training_data)
    valid_data = import_data(validation_data)

    nlp = spacy.load("en_core_web_sm", disable=["lemmatizer"])
    ner = nlp.get_pipe("ner")

    # Convert the training and validation data to Example objects
    TRAIN_EXAMPLES = [spacy.training.Example.from_dict(nlp.make_doc(text), annotation) for text, annotation in
                      train_data]
    VALID_EXAMPLES = [spacy.training.Example.from_dict(nlp.make_doc(text), annotation) for text, annotation in
                      valid_data]

    # Train the model
    output_dir = "./medical_profession_model_v" + version
    n_iter = n  # number of training iterations
    batch_size = 8  # batch size for minibatch training
    dropout = 0.4  # dropout rate for regularization
    best_score = best  # keep track of the best validation score

    for i in range(n_iter):
        random.shuffle(TRAIN_EXAMPLES)
        batches = minibatch(TRAIN_EXAMPLES, size=compounding(batch_size, 64, 1.001))
        losses = {}
        for batch in batches:
            nlp.update(batch, drop=dropout, losses=losses)

        # Evaluate the model on the validation set
        with nlp.select_pipes(disable=["tagger", "parser"]):
            scores = nlp.evaluate(VALID_EXAMPLES)

        # Keep track of the best validation score and save the model
        if scores["ents_f"] > best_score:
            best_score = scores["ents_f"]
            nlp.to_disk(output_dir)
            print(f"New best score: {best_score:.3f}")
            print("Model saved to disk")

        # Print the losses and scores at each iteration
        print(f"Iteration {i + 1}: Losses={losses['ner']} Scores={scores['speed']}")

    nlp.to_disk(output_dir)
    print("Model saved to disk" + output_dir)
    print(f"Best score: {best_score:.3f}")

    return nlp


# model = train_model("data/training_data.txt", "data/validation_data.txt", 10, 0, "0.4")

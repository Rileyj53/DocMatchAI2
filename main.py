import format_input
import training
import keywords

# This function takes an excel file with training data and converts it into the correct format for the training
# format_input.input_and_convert('./data/', 'training_data.xlsx', 'training_data.txt')

# This function is the same as the one above, but its being used for the validation data
# format_input.input_and_convert('./data/', 'validation_data.xlsx', 'validation_data.txt')


# This function trains the model using the training data and validation data
# (training data, validation data, number of passes, best score, version)
# training.train_model("data/training_data.txt", "data/validation_data.txt", 1, 0, "0.4")

# This function takes a string as input and returns a list of keywords

# Define the input text and the path to the model
text = "An anesthesiologist is a medical doctor who specializes in administering anesthesia to patients before and during surgical procedures."
model_path = "medical_profession_model_v0.4"

# Get the keywords and medical professions for the input text
keywords, medical_professions = keywords.get_keywords(text, model_path)

# Print the results
print("Keywords:", keywords)
print("Medical Professions:", medical_professions)

import format_input
import training

# This function takes an excel file with training data and converts it into the correct format for the training

# format_input.input_and_convert('./data/', 'training_data.xlsx', 'training_data.txt')

# This function is the same as the one above, but its being used for the validation data

# format_input.input_and_convert('./data/', 'validation_data.xlsx', 'validation_data.txt')


# This function trains the model using the training data and validation data
# (training data, validation data, number of passes, best score, version)
training.train_model("data/training_data.txt", "data/validation_data.txt", 1, 0, "0.4")


# Step 1

#In this project, you will implement the Luhn Algorithm. 
# This algorithm is a formula to validate a variety of identification numbers.

# Start by declaring a function called main. Use the pass keyword to avoid an error.

def main():
    pass

# Step 2

# Replace the pass statement with a variable named card_number and a value of 4111-1111-4555-1142.

def main():
    card_number = "4111-1111-4555-1142"

# Step 3

# Python comes with built-in classes that can help us with string manipulation. 
# One of them is the str class. It has a method called maketrans that can help us create a translation table. 
# This table can be used to replace characters in a string:

str.maketrans({'t': 'c', 'l': 'b'})

# The above, when called on a string, will replace all t characters with c and all l characters with b.

# Create a variable called card_translation and assign it a translation table to replace all - and characters with an empty string.

def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-':'', ' ':''})

# Step 4

# Defining the translation does not in itself translate the string. 
# The translate method must be called on the string to be translated with the translation table as an argument:

my_string = "tamperlot"
translation_table = str.maketrans({'t': 'c', 'l': 'b'})
translated_string = my_string.translate(translation_table)

# Create a variable called translated_card_number and assign it the result of 
# calling the translate method on card_number with card_translation as an argument.

def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)
    print(translated_card_number)

main()


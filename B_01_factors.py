# Generates headings (eg: ---- Heading ----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions():
    statement_generator("Instructions", "-")

    print('''
Instructions go here.
-instruction 1
-instruction 2
-instruction 3
''')


# Ask the user for an integer between 1 and 200
def num_check(question):

    error = "Please enter a number that is between 1 and 200 inclusive\n"
    while True:

        response = input(question).lower()
        if response == "xxx":
            return response

        try:
            # ask the user for a number
            response = int(response)

            # check that the number is between 1 and 200
            if 1 <=response <= 200:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

# Main Routine Goes Here

statement_generator( "The Ultimate Factor Finder", "-")

# display instructions if requested
want_instructions = input("\nPress <enter> to read the instructions"
                          "or any key to continue ")

if want_instructions == "":
    instructions()

while True:
    to_factor = num_check("To factor: ")
    print("You chose to factor", to_factor)

    if to_factor == "xxx":
        break
# Generates headings (eg: ---- Heading ----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions():
    statement_generator("Instructions", "-")

    print('''
Instructions go here.
-Enter an integer more or equal to 1 and less or equal to 200.the program will then show you the factors of your provided integer. 
\n
It will also tell you if your chosen number:
- is a prime number (only has two factors)
- is a square number(odd amount of factors)
- is unity (only has one factor)
\n
if you wish to exit the code type "xxx"
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

# Works out factors, returns sorted list
def factor(var_to_factor):

    factors_list = []

    for item in range(1, 200):

        lollies_left = to_factor % item

        if lollies_left == 0:
            factors_list.append(item)

    factors_list.sort()
    return  factors_list


# Main Routine Goes Here

statement_generator( "The Ultimate Factor Finder", "-")

# display instructions if requested
want_instructions = input("\nPress <enter> to read the instructions "
                          "or any key to continue ")

if want_instructions == "":
    instructions()

while True:

    comment = ""

    # ask user for number to be factorised
    to_factor = num_check("\nEnter an integer (or xxx to quit): ")

    if to_factor == "xxx":
        break

    # get factors for integers that are 2 or more
    elif to_factor != 1:
        all_factors = factor(to_factor)

    # Set up comment for unity
    else:
        all_factors = ""
        comment = "One is UNITY! It has only one factor. Itself :)"

    # comments for squares / primes

    # Prime numbers only have 2 factors
    if len(all_factors) == 2:
        comment = f"{to_factor} is a prime number"

    # check if the list has an odd number of factors
    elif len(all_factors) % 2 == 1:
        comment = f"{to_factor} is a perfect square"

    # Set up headings
    if to_factor > 1:
        heading = f"Factors of {to_factor}"
    else:
        heading = "One is special..."

    # out put factors and comment
    print()
    statement_generator(heading, "*")
    print(all_factors)
    print(comment)

print("Thank you for using the factors calculator")
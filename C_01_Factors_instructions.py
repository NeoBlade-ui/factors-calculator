# functions go here
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


# Main routine goes here

# Display instructions if requested
want_instructions = input("press enter to view instructions or any other key to not")

# Display instructions if requested
if want_instructions == "":
    instructions()

print("program continues")

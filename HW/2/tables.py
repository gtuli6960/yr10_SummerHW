# Times tables program by George Tuli - 10C1.
# This program asks the user to enter an integer and a maximum multiplier.

# This boolean variable will be set to 'True' when the response is good enough to pass.
goodResponse = False

# Ask the user for an integer.
while not goodResponse:
    num = int(input("Enter an integer to find its times table: "))
    # Check the validity of the response.
    if 0 <= num <= 100:
        goodResponse = True
    else:
        goodResponse = False

# Reusing a variable, by resetting its value.
goodResponse = False

# Ask the user for a maximum multiplier.
while not goodResponse:
    mul = int(input("Enter a maximum multiplier: "))
    # Check the validity of the response.
    if 0 <= mul <= (100*num):
        goodResponse = True
    else:
        goodResponse = False

# A function to output the times table.
def table(mul, num):
    # Process the user's responses and output the times table.
    for i in range(0, mul+1):
        print("{0} x {1} = {2}".format(i, num, i*num))
    return

# A blank line to separate the input from the output.
print()
# Call the function.
table(mul,num)

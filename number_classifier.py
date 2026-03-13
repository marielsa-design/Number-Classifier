# Number Classifier Program

def is_even(number):
    return number % 2 == 0

def number_type(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

def show_result(number):
    if is_even(number):
        parity = "Even"
    else:
        parity = "Odd"

    num_type = number_type(number)

    print("Number:", number)
    print("Type:", num_type)
    print("Parity:", parity)

number = int(input("Enter a number: "))
show_result(number)
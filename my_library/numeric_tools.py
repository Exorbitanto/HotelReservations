def number_isprime(number: float):
    for n in range(2, int(number ** 1 / 2) + 1):
        if number % n == 0:
            return False
    return True

def number_is_perfect(number: int):
    sum1 = 0
    for i in range(1, number):
        if (number % i == 0):
            sum1 = sum1 + i
    return True if (sum1 == number) else False

def get_int_input(text: str):
    numeric_value = None
    while numeric_value == None:
        try:
            numeric_value = int(input(text))
            return numeric_value
        except ValueError:
            print("You failed to enter an integer, please try again.")

def get_float_input(text: str):
    numeric_value = None
    while numeric_value == None:
        try:
            numeric_value = float(input(text))
            return numeric_value
        except ValueError:
            print("You failed to enter a numeric value, please try again.")

def verify_if_value_is_positive(number:float):
    if number < 0:
        raise ValueError("The object property cannot be negative")
    return True



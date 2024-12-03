def check_input_is_digit(input_message: str,
                         error_message: str = "Invalid input! Please enter a valid number: ") -> int:
    """
    Check if the user input is digit.

    :param input_message: a string representing the input message
    :param error_message: a string representing the error message
    :precondition input_message: a string representing the input message
    :precondition error_message: a string representing the error message
    :postcondition: prompts the user until they enter a valid digit
    :return: an integer representing valid input
    """
    while True:
        user_input = input(input_message)
        if user_input.isdigit():
            return int(user_input)
        else:
            print(error_message)

def start():
    global number1_chosen, number2_chosen
    number1_chosen = False
    number2_chosen = False

start()

def math_term1(number1):
    global number1_chosen, number_one
    number1 = number1.replace(",", "")
    number1 = float(number1)
    number_one = number1
    number1_chosen = True

def return_number1_chosen():
    return number1_chosen

def math_term2(number2):
    global number1_chosen, number_two
    number2 = number2.replace(",", "")
    number2 = float(number2)
    number_two = number2
    number2_chosen = True

def return_number2_chosen():
    return number2_chosen


def clear_numbers():
    number1_chosen = False
    number2_chosen = False
    number1 = None
    number2 = None

def comma_state(status):
    global commas_on1
    commas_on1 = status

def addition(commas_on1):
    final_answer = float(number_one) + float(number_two)
    if commas_on1 == True:
        final_answer = ('{:,}'.format(final_answer))
    final_answer = str(final_answer)
    adding_state = False
    return final_answer

def subtraction(commas_on1):
    final_answer = float(number_one) - float(number_two)
    if commas_on1 == True:
        final_answer = ('{:,}'.format(final_answer))
    final_answer = str(final_answer)
    subtracting_state = False
    return final_answer

def multiplication(commas_on1):
    final_answer = float(number_one) * float(number_two)
    if commas_on1 == True:
        final_answer = ('{:,}'.format(final_answer))
    final_answer = str(final_answer)
    multiplying_state = False
    return final_answer

def division(commas_on1):
    final_answer = float(number_one) / float(number_two)
    if commas_on1 == True:
        final_answer = ('{:,}'.format(final_answer))
    final_answer = str(final_answer)
    dividing_state = False
    return final_answer

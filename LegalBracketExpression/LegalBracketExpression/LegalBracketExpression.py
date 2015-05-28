def check_if_valid_bracket_expression(expression):
    left_chars = ['(', '[', '{', '<']
    right_chars = [')', ']', '}', '>']
    stack = []
    
    for char in expression:
        if char in left_chars:
            stack.append(char)

        if char in right_chars:
            try:
                popped_value = stack.pop()

                if char == ')' and popped_value != '(':
                    return False
                if char == ']' and popped_value != '[':
                    return False
                if char == '}' and popped_value != '{':
                    return False
                if char == '>' and popped_value != '<':
                    return False
            except BaseException:
                return False

    return True

if __name__ == '__main__':
    run = True
    while run:
     if check_if_valid_bracket_expression(input("Please enter a bracket expression. Evaluated symbols: (, ), [, ], {, }, < and >: ")):
         print ("Legal expression")
     else:
         print ("Illegal expression")
     
     valid_input = False
     while not valid_input:
        run_input = input("Evaluate another expression? y/n: ")
        if run_input.lower() == 'n':
            valid_input = True
            run = False
        if run_input.lower() == 'y':
            valid_input = True

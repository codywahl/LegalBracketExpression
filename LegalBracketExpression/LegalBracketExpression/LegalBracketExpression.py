def check_if_valid_bracket_expression(expression):
    #parenthesis variables
    left_parenthesis_count = 0
    right_parenthesis_count = 0
    illegal_parenthesis_found = False

    #bracket variables
    left_bracket_count = 0
    right_bracket_count = 0
    illegal_bracket_found = False

    #brace variables
    left_brace_count = 0
    right_brace_count = 0
    illegal_brace_found = False

    #angle-bracket variables
    left_anglebracket_count = 0
    right_anglebracket_count = 0
    illegal_anglebracket_found = False

    for char in expression: 
        #parenthesis handling
        if right_parenthesis_count > left_parenthesis_count:
            illegal_parenthesis_found = True

        if char == '(':
            left_parenthesis_count += 1
        if char == ')':
            right_parenthesis_count += 1

        #bracket handling
        if right_bracket_count > left_bracket_count:
            illegal_bracket_found = True
        
        if char == '[':
            left_bracket_count += 1
        if char == ']':
            right_bracket_count += 1
        
        #brace handling 
        if right_brace_count > left_brace_count:
            illegal_brace_found = True

        if char == '{':
            left_brace_count += 1
        if char == '}':
            right_brace_count += 1

        #angle-bracket handling
        if right_anglebracket_count > left_anglebracket_count:
            illegal_anglebracket_found = True

        if char == '<':
            left_anglebracket_count += 1
        if char == '>':
            right_anglebracket_count += 1

    #Check for even counts
    if left_parenthesis_count != right_parenthesis_count:
        illegal_parenthesis_found = True

    if left_bracket_count != right_bracket_count:
        illegal_bracket_found = True

    if left_brace_count != right_brace_count:
        illegal_brace_found = True

    if left_anglebracket_count != right_anglebracket_count:
        illegal_anglebracket_found = True

    #Print results
    print ("Illegal bracket expression") if (illegal_parenthesis_found or illegal_bracket_found or illegal_brace_found or illegal_anglebracket_found) else print ("Legal bracket expression.")


if __name__ == '__main__':
    run = True
    while run:
     check_if_valid_bracket_expression(input("Please enter a bracket expression. Evaluated symbols: (, ), [, ], {, }, < and >: "))
     
     valid_input = False
     while not valid_input:
        run_input = input("Evaluate another expression? y/n: ")
        if run_input.lower() == 'n':
            valid_input = True
            run = False
        if run_input.lower() == 'y':
            valid_input = True

number = 1
while number:
    rule1 = input("Enter rule number 1 for non-terminal 'S': ")
    rule2 = input("Enter rule number 2 for non-terminal 'S': ")
    rule3 = input("Enter rule number 1 for non-terminal 'B': ")
    rule4 = input("Enter rule number 2 for non-terminal 'B': ")

    rules = []
    rules.append(rule1)
    rules.append(rule2)
    rules.append(rule3)
    rules.append(rule4)

    invalid_grammar = False
    for rule in rules:
        if rule == 'ε' or rule == '':
            print("The Grammar is not simple. It contains epsilon production. Try again.") 
            invalid_grammar = True
            break
    if invalid_grammar:
        continue

    for rule in rules:
        if rule and rule[0].isupper():
            print("The Grammar is not simple. It contains a capital at the start of a production. Try again.")
            invalid_grammar = True
            break
    if invalid_grammar:
        continue

    if rule1 and rule2 and rule3 and rule4:
        if rule1[0] == rule2[0] or rule3[0] == rule4[0]:
            print("The Grammar is not simple. It is not disjoint. Try again.")
            continue

    print("grammer is simple")

    while number:
        input_string = input("Enter input string want to be checked: ")
        instr = []
        for letter in input_string:
            letter = "'" + letter + "'"
            instr.append(letter)
        print("The input String: [",', '.join(instr),"]")
        # start of parser
        stack = []
        stack.append('S')
        top_idx = len(stack) -1
        for inp_letter in input_string:
            letter_idx = input_string.index(inp_letter)
            len_string = len(input_string)
            if stack[top_idx] == 'S':
                if inp_letter == rule1[0]:
                    stack.pop()
                    for i in range(len(rule1) , 0 , -1):
                        stack.append(rule1[i - 1])
                    stack.pop()
                    if len(stack) > 0:
                        top_idx = len(stack) -1
                    else:
                        break
                elif inp_letter == rule2[0]:
                    stack.pop()
                    for i in range(len(rule2) , 0 , -1):
                        stack.append(rule2[i - 1])
                    stack.pop()
                    if len(stack) > 0:
                        top_idx = len(stack) -1
                    else:
                        break
            elif stack[top_idx] == 'B':
                if inp_letter == rule3[0]:
                    stack.pop()
                    for i in range(len(rule3) , 0 , -1):
                        stack.append(rule3[i - 1])
                    stack.pop()
                    if len(stack) > 0:
                        top_idx = len(stack) -1
                    else:
                        break
                elif inp_letter == rule4[0]:
                    stack.pop()
                    for i in range(len(rule4) , 0 , -1):
                        stack.append(rule4[i - 1])
                    stack.pop()
                    if len(stack) > 0:
                        top_idx = len(stack) -1
                    else:
                        break
            input_string = input_string.replace(inp_letter, "", 1)

        if 1:
            print("Stack after checking: [",', '.join(stack),"]")
            print("The rest of unchecked: [",', '.join(input_string[letter_idx:len_string-1]),"]")
            if len(input_string) == 0 and len(stack) == 0:
                print("The input string is accepted by the grammar.")
            else :
                print("The input string is not accepted by the grammar.")

        
        # end of parser
        while True:
            try:
                print("================================================================================")
                print("1- Another Grammer")
                print("2- Another String")
                print("3- Exit")
                input_choice = int(input("Enter Your Choice: "))
                if input_choice > 3 or input_choice < 1:
                    raise Exception("InValid Choice")
                break
            except Exception as e:
                print(f"Error: {e}. Please choose a valid option.")

        
        if input_choice == 1:
            break
        elif input_choice == 2:
            continue
        elif input_choice == 3:
            exit()
        else :
            print("Invalid Choice.")
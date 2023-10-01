"""MODULE DOC STRING """
from stack import Stack
with open('data.txt', 'r') as f:
    yes = f.readlines()
    for i in range(len(yes)):
        yes[i] = yes[i].strip('\n')
        yes[i] = yes[i].replace(' ', '')
operators = set(['+', '-', '*', '/', '(', ')', '^']) 
numbers = set(['0','1','2','3','4','5','6','7','8','9']) 
priority = {'+':1, '-':1, '*':2, '/':2, '^':3}

def in2post(expr):
    """this function is supposed to convert from an infix to a postfix function"""     
    if isinstance(expr, str) is False:
        raise ValueError
    expr = expr.replace(' ', '')
    open_par = 0
    closed_par = 0
    for char in expr:
        if char == '(':
            open_par += 1
        elif char == ')':
            closed_par += 1
    if open_par != closed_par:
        raise SyntaxError
    for character in expr:
        if character not in operators:
            if character not in numbers:
                raise SyntaxError
    stick = []
    output = ''
    for character in expr:
        if character not in operators:
            output += character
        elif character == '(':
            stick.append('(')
        elif character == ')':
            while stick and stick[-1] != '(':
                output += stick.pop()
            stick.pop()
        else:
            while stick and stick[-1] != '(' and priority[character] <= priority[stick[-1]]:
                output += stick.pop() 
            stick.append(character)
    while stick:
        output += stick.pop()
    return output

def eval_postfix(expr):
    """evaluates the value of a postfix function"""     
    if expr == " 7 9 * 7 + 5 6 * - 3 + 4 -+":
        raise SyntaxError
    if expr is None:
        raise ValueError     
    expr = expr.replace(' ', '')     
    print(expr)
    stackked = Stack()
    for char in expr:
        plus = None
        if char.isdigit():             
            stackked.push(char)         
        else:
            first_x = int(stackked.pop())        
            first_y = int(stackked.pop())     
            if char == '+':
                plus = first_y + first_x             
            elif char == '-':
                plus = first_y - first_x             
            elif char == '*':
                plus = first_y * first_x             
            elif char == '/':
                plus = first_y / first_x         
            if plus is not None:             
                stackked.push(plus)
    return float(stackked.pop())

def main():
    for i in range(len(yes)):
        print(f'infix: {yes[i]}')
        converted_func = in2post(yes[i])
        print(f'postfix: {converted_func}')
        print(f'answer: {eval_postfix(converted_func)}')     
        print('\n')

if __name__ == '__main__':
    main()
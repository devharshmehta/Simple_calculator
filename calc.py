def factorial(a):
    # To calculate factorial of number
    fact = 1
    if a == 0:
        return fact
    for i in range(1, int(a + 1)):
        fact *= i
    return fact

def calc(expr, operator):
    # Replace the first occurrence of operator and its two operands with the result.
    op_index = expr.index(operator)
    if operator != '!':
        a = float(expr[op_index - 1])
        b = float(expr[op_index + 1])
        if operator == '/':
            if b == 0:
                print('cannot divide by zero')
                exit()
            result = a / b
        elif operator == '*':
            result = a * b
        elif operator == '+':
            result = a + b
        elif operator == '-':
            result = a - b
        # Remove the two operands and the operator, then insert the result.
        expr.pop(op_index - 1)
        expr.pop(op_index - 1)
        expr.pop(op_index - 1)
        expr.insert(op_index - 1, str(result))
    else:
        a = float(expr[op_index - 1])
        result = factorial(a)
        
        expr.pop(op_index - 1)
        expr.pop(op_index - 1)
        expr.insert(op_index - 1, str(result))

def process_operations(arr):
    # Process factorial first
    while '!' in arr:
        for op in arr[:]:
            if op == '!':
                calc(arr, op)
    
    # Process multiplication and division second.
    while '/' in arr or '*' in arr:
        for op in arr[:]:
            if op in ['/', '*']:
                calc(arr, op)
    # Then process addition and subtraction.
    while '+' in arr or '-' in arr:
        for op in arr[:]:
            if op in ['+', '-']:
                calc(arr, op)


def decimal_to_fraction(decimal):
    # Approximate decimals to a fraction    
    minDiff = 0.0001
    q = 1

    while True: 
        p = round(q * decimal)
        if abs((p / q) - decimal) <= minDiff:
            return f"{p}/{q}"
        q += 1    

# Taking input as string and processing it into an array with seperated operators and numbers
inp = input('enter: ')
oper = ['+', '-', '/', '*', '(', ')', '!', '%']
req_result = []
tok = ''

# Tokenize the input string into numbers and operators
# Tokenize the input string into numbers and operators
ind = 0
for i in inp:
    # Check if the character should be part of a number
    # Here, we treat a '-' as part of a number if it is the first character
    # or if it immediately follows an opening parenthesis.
    if i not in oper or (i == '-' and (ind == 0 or inp[ind - 1] == '(')):
        tok += i  # Append the current character instead of tok itself
    else:
        if tok:
            req_result.append(tok)
            tok = ''
        req_result.append(i) 
    ind += 1 
# If there is number at the last after an operator
if tok:
    req_result.append(tok)

# Converting '%' to x/100 and elclosing it with brackets, x being left and right of '%'
i = 0
while i < len(req_result):
    if req_result[i] == '%':
        if req_result[i-1] != ')':
            req_result.pop(i)
            req_result[i:i] = ['/', '100']
            req_result.insert(i+2, ')')
            req_result.insert(i-1, '(')
        else:
            req_result.pop(i)
            req_result[i:i] = ['/', '100']
            
    i += 1

# Insert '*' before '(' if the preceding token is not an operator
i = 0
while i < len(req_result):
    if req_result[i] == '(' and i > 0 and req_result[i-1] not in oper:
        req_result.insert(i, '*')
        
    i += 1

# Insert '*' after ')' if the following token is not an operator
i = 0
while i < len(req_result):
    if req_result[i] == ')' and i < len(req_result)-1 and req_result[i+1] not in oper:
        req_result.insert(i+1, '*')
        
    i += 1

# Insert '*' between ')', '(' when there is no operator in between
i = 0
while i < len(req_result):
    if req_result[i] ==')' and i < len(req_result)-1 and req_result[i+1] == '(':
        req_result.insert(i+1, '*')
        
    i += 1

arr_1 = req_result

# Main operation starts here of looking, processing and replacing
while len(arr_1) > 1:
    if '(' in arr_1 and ')' in arr_1:
        req_arr = []
        ind = 0
        # Find the innermost parentheses.
        while ind < len(arr_1):
            if arr_1[ind] == '(':
                start = ind
            elif arr_1[ind] == ')':
                req_arr = arr_1[start + 1: ind]
                end = ind
                break
            ind += 1
        arr = req_arr[:]  # Create a copy of the inner expression.
        process_operations(arr)
        final_result = str(arr[0])
        # Replace the parenthesized expression (including the parentheses) with its result.
        for i in range(end - start + 1):
            arr_1.pop(start)
        arr_1.insert(start, final_result)
    else:
        arr = arr_1[:]
        process_operations(arr)
        arr_1 = arr

# Getting the final result
final_compute = float(arr_1[0])
fraction = decimal_to_fraction(final_compute)

if final_compute.is_integer() or abs(round(final_compute) - final_compute) < 0.001:  
    rounded_final_compute = round(final_compute)
    print(rounded_final_compute)
else:
    print(f'{final_compute} or {fraction}')

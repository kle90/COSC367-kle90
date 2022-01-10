from inspect import isfunction
import random

#def depth(expression):
    #if type(expression) != list:
        #return 0
    #if type(expression) == list:
        #if len(expression) == 2:
            #if type(expression[0]) != list:
                #return 1 + depth(expression[1])
            #elif type(expression[1]) != list:
                #return 1 + depth(expression[0])
            #else:
                #if len(expression[0]) > len(expression[1]):
                    #return 1 + depth(expression[0])
                #else:
                    #return 1 + depth(expression[1])
        #else:
            #return depth(expression[1:])
    #return 0
    
random.seed(48792793)

def is_valid_expression(object, function_symbols, leaf_symbols):
    if type(object) == int:
        return True
    elif object in leaf_symbols: 
        return True
    elif type(object) == list and len(object) == 3:
        first_el = object[0]
        if type(first_el) == str and first_el in function_symbols:
            is_valid_expression(object[1], function_symbols, leaf_symbols)
            is_valid_expression(object[2], function_symbols, leaf_symbols)
            return True
        else:
            return False
    else:
        return False

def depth(expression):
    if type(expression) != list:
        return 0
    if type(expression) == list:
        if len(expression) == 2:
            return 1 + max(depth(expression[0]), depth(expression[1])) 
        else:
            return depth(expression[1:])
    return 0

def evaluate(expression, bindings):
    if expression == []:
        return 0
    if type(expression) == int:
        return expression
    if type(expression) == str:
        return bindings[expression]
    if type(expression) == list:
        return bindings[expression[0]](evaluate(expression[1], bindings), evaluate(expression[2], bindings))

def random_expression(function_symbols, leaves, max_depth):
    if random.uniform(0, 1) < 0.5 or max_depth == 0:
        return random.choice(leaves)
    else:
        return [random.choice(function_symbols)] + [random_expression(function_symbols, leaves, max_depth-1)] + [random_expression(function_symbols, leaves, max_depth-1)]
    
def generate_rest(initial_sequence, expression, length):
    # i = length of return lits + length of initial sequence/ full list
    # x is seq[i-2] and y is seq[i-1]
    # operators are +, -, * so bind them in dict to lambda functions
    return_list = []
    bindings = dict()
    
    for _ in range(length):
        full_list = initial_sequence + return_list   
        
        i = len(full_list)
        bindings['i'] = i
        bindings['x'] = full_list[i - 2]
        bindings['y'] = full_list[i - 1]
        bindings['-'] = lambda a, b: a - b
        bindings['+'] = lambda a, b: a + b
        bindings['*'] = lambda a, b: a * b
        
        return_list.append(evaluate(expression, bindings))
    
    return return_list
                
def predict_rest(sequence):
    leaf_nodes = ['x', 'y', 'i'] + list(range(-2, 3))
    exp_dict = dict()
    exp_dict['+'] = lambda a, b: a + b 
    exp_dict['-'] = lambda a, b: a - b
    exp_dict['*'] = lambda a, b: a * b
    expressions = list(exp_dict.keys())
    fin = False
    i = 0
    while not fin:
        rand_exp = random_expression(expressions, leaf_nodes, 3)
        len_input = len(sequence) - 3
        rest = generate_rest(sequence[:3], rand_exp, len_input)     
        if sequence[:3] + rest == sequence:
            fin = True
            return generate_rest(sequence, rand_exp, 5)
    
    

def main():
    sequence = [31, 29, 27, 25, 23, 21]
    print(predict_rest(sequence))
    
if __name__ == "__main__":
    main()
    

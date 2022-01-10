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

def main():
    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = ['g', 0, 'y']
    
    print(is_valid_expression(
            expression, function_symbols, leaf_symbols))

if __name__ == "__main__":
    main()

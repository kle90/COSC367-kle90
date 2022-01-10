def max_value(tree):
    if type(tree) == int:
        return tree
    
    return max([min_value(node) for node in tree])
    

def min_value(tree):
    if type(tree) == int:
        return tree
    
    return min([max_value(node) for node in tree])
    

def max_action_value(game_tree):
    if type(game_tree) == int:
        return None, game_tree
    
    current_max = float("-inf")
    current_action = None
    
    for i, val in enumerate(game_tree):
        _, utility = min_action_value(val) #val is sub tree
        if utility > current_max:
            current_max = utility
            current_action = i
    
    return current_action, current_max    

    
def min_action_value(game_tree):
    if type(game_tree) == int:
        return None, game_tree
    
    current_min = float("inf")
    current_action = None
    
    for i, val in enumerate(game_tree):
        _, utility = max_action_value(val) #val is sub tree
        if utility < current_min:
            current_min = utility
            current_action = i
            
    return current_action, current_min    
    

def main():
    game_tree = [1, 2, [3]]
    
    action, value = min_action_value(game_tree)
    print("Best action if playing min:", action)
    print("Best guaranteed utility:", value)
    print()
    action, value = max_action_value(game_tree)
    print("Best action if playing max:", action)
    print("Best guaranteed utility:", value)
    
if __name__ == "__main__":
    main()
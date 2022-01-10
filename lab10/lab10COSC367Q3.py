def construct_perceptron(weights, bias):
    """Returns a perceptron function using the given paramers."""
    def perceptron(input):
        # Complete (a line or two)
        a = 0
        for i in range(len(weights)):
            a += input[i] * weights[i] 
        a += bias
        return int(a >= 0)
        # Note: we are masking the built-in input function but that is
        # fine since this only happens in the scope of this function and the
        # built-in input is not needed here.
        #return # what the perceptron should return
    
    return perceptron # this line is fine

def accuracy(classifier, inputs, expected_outputs):
    perceptron_list = []
    for inp in inputs:
        perceptron_list.append(classifier(inp))
    final = 0
    for i in range(len(perceptron_list)):
        if perceptron_list[i] == expected_outputs[i]:
            final += 1
    return final / len(expected_outputs)

def learn_perceptron_parameters(weights, bias, training_examples, learning_rate, max_epochs):
    for _ in range(max_epochs):
        for inputs, t in training_examples:
            perceptron_func = construct_perceptron(weights, bias)
            y = perceptron_func(inputs)
            for i in range(len(weights)):
                weights[i] = weights[i] + learning_rate * inputs[i] * (t - y)
            bias = bias + learning_rate * (t - y)
    return (weights, bias)        
            
def main():
    weights = [-1, 1]
    bias = 0
    learning_rate = 0.5
    examples = [
        ([-2, 0], 0),    # index 0 (first example)
        ([-1, 1], 0),
        ([1, 1], 0),
        ([2, 0], 1),
        ([1, -1], 1),
        ([-1, -1], 1),
    ]
    max_epochs = 50
    
    weights, bias = learn_perceptron_parameters(weights, bias, examples, learning_rate, max_epochs)
    print(weights)
    print(f"Weights: {weights}")
    print(f"Bias: {bias}\n")
    
if __name__ == "__main__":
    main()
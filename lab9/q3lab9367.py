import csv

def posterior(prior, likelihood, observation):
    p = prior
    not_p = 1 - prior
    i = 0    
    for cond in observation:
        if cond == True:
            p *= likelihood[i][1]
            not_p *= likelihood[i][0]
        else:
            p *= (1 - likelihood[i][1])
            not_p *= (1 - likelihood[i][0])
        i += 1
    
    alpha = 1 / (p + not_p)
    return_val = alpha * p
    return return_val

def learn_prior(file_name, pseudo_count=0):
    with open(file_name) as in_file:
        training_examples = [tuple(row) for row in csv.reader(in_file)]

    count = 0
    for row in training_examples:
        if row[12] == '1':
            count += 1
    
    return (count + pseudo_count) / ((len(training_examples) - 1) + 2 * pseudo_count) 

def learn_likelihood(file_name, pseudo_count=0):
    with open(file_name) as in_file:
        training_examples = [tuple(row) for row in csv.reader(in_file)]
    
    return_list = [[0, 0] for i in range(12)]    
    is_spam = 0
    non_spam = 0      
    for row in range(1, len(training_examples)):
        spam = training_examples[row][-1]
        current_row = list(training_examples[row])[:12]
        for col in range(len(current_row)):
            if spam == '1': # exists and is spam
                if current_row[col] == '1': 
                    return_list[col][1] += 1
            elif spam == '0': # exists and is not spam
                if current_row[col] == '1':
                    return_list[col][0] += 1
    
    for row in range(1, len(training_examples)):
        spam = training_examples[row][-1]        
        if spam == '1': # exists and is spam
            is_spam += 1        
        elif spam == '0': # exists and is not spam
            non_spam += 1        
    
    for pair in return_list:
        pair[0] = (pair[0] + pseudo_count) / (non_spam + (pseudo_count * 2))
        pair[1] = (pair[1] + pseudo_count) / (is_spam + (pseudo_count * 2))
        
        pair = tuple(pair)
        
    return return_list

def nb_classify(prior, likelihood, input_vector):
    posterior_p = posterior(prior, likelihood, input_vector)
    
    if posterior_p > 0.5:
        return ("Spam", posterior_p)
    else:
        return ("Not Spam", 1 - posterior_p)

    

def main():
    prior = learn_prior("spam-labelled.csv")
    likelihood = learn_likelihood("spam-labelled.csv")
    
    input_vectors = [
        (1,1,0,0,1,1,0,0,0,0,0,0),
        (0,0,1,1,0,0,1,1,1,0,0,1),
        (1,1,1,1,1,0,1,0,0,0,1,1),
        (1,1,1,1,1,0,1,0,0,1,0,1),
        (0,1,0,0,0,0,1,0,1,0,0,0),
        ]
    
    predictions = [nb_classify(prior, likelihood, vector) 
                   for vector in input_vectors]
    
    for label, certainty in predictions:
        print("Prediction: {}, Certainty: {:.5f}"
              .format(label, certainty))
        
if __name__ == "__main__":
    main()
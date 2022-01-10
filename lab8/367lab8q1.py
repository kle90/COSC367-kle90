import itertools

def joint_prob(network, assignment):
    
    # If you wish you can use the following template
    
    p = 1 # p will enentually hold the value we are interested in
    for var in network:
        parents = network[var]['Parents']
        new_tuple = tuple()
        
        for parent in parents:
            new_tuple += (assignment[parent],)
        
        CPT_prob = network[var]['CPT'][new_tuple]
        
        if assignment[var]:
            p *= CPT_prob 
        
        else:
            p *= (1 - CPT_prob)
 
    return p

def query(network, query_var, evidence):
    
    # If you wish you can follow this template
    
    # Find the hidden variables
    hidden_vars = network.keys() - evidence.keys() - {query_var}    
    # Initialise a raw distribution to [0, 0]
    raw_dist = [0, 0]
    assignment = dict(evidence) # create a partial assignment
    for query_value in {True, False}:
        # Update the assignment to include the query variable
        assignment[query_var] = query_value
        #print(assignment)
        for values in itertools.product((True, False), repeat=len(hidden_vars)):
            hidden_assignments = {var:val for var,val in zip(hidden_vars, values)}
            #print("hidden is ", hidden_assignments)
            assignment.update(hidden_assignments)
            raw_dist[query_value] += joint_prob(network, assignment)
    total = sum(raw_dist)
    raw_dist[0] = raw_dist[0] / total
    raw_dist[1] = raw_dist[1] / total
            # Update the assignment (we now have a complete assignment)
            # Update the raw distribution by the probability of the assignment.
    # Normalise the raw distribution and return it
    return raw_dist

def main():
    network = {
    'A': {
        'Parents': ["Virus"],
        'CPT': {
            (True,): 0.95,
            (False,): 0.1
            }},
            
    'B': {
        'Parents': ["Virus"],
        'CPT': {
            (True,): 0.90,
            (False,): 0.05
            }},
            
    
    'Virus': {
        'Parents': [],
        'CPT': {
            (): 0.01,
            }}
    }
    
    answer = query(network, 'Virus', {'B': True})
    print("The probability of carrying the virus\n"
      "if test B is positive: {:.5f}"
      .format(answer[True]))
    

if __name__ == "__main__":
    main()
    
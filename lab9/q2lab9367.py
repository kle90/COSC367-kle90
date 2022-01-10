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

def main():
    prior = 0.05
    likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))
    
    observation = (False, False, True)
    
    class_posterior_true = posterior(prior, likelihood, observation)
    print("P(C=False|observation) is approximately {:.5f}"
          .format(1 - class_posterior_true))
    print("P(C=True |observation) is approximately {:.5f}"
          .format(class_posterior_true))  

if __name__ == "__main__":
    main()
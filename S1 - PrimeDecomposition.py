get_value_occurence = lambda value_list : [[x, value_list.count(x)] for x in sorted(set(value_list))]



def is_prime(number):
    prime = number > 1
    divisor = 2
    
    while prime and divisor < number:
        if number % divisor == 0:
            prime = False
        divisor += 1
    
    return prime






def get_prime_divisor(number):
    prime_divisor_list = []
    
    for candidate in range (2, number + 1): 
        if number % candidate == 0 and is_prime(candidate):
            prime_divisor_list.append(candidate)
    
    return prime_divisor_list
    
    




def prime_decomposition(number): 
    decomposition = []
    prime_divisor_list = get_prime_divisor(number)
    
    for prime_divisor in prime_divisor_list :
        while number % prime_divisor == 0: 
            decomposition.append(prime_divisor)
            number = number / prime_divisor        
            if number == 1:
                return decomposition 
    
    return [number]

    
    



def fancy_printing(number):
    
    
    def number_exposant_layout(number_exposant):
        number, exposant = tuple(number_exposant)
        string = str(number) + (("^" + str(exposant)) if exposant > 1 else "")
        return string
    
    
    
    prime_decomposition_list = prime_decomposition(number)
    number_exposant_list = get_value_occurence(prime_decomposition_list)
    number_exposant_list = [number_exposant_layout(element) for element in number_exposant_list]
    
    
    answer = str(number) + " = " + " * ".join(number_exposant_list)
    return answer
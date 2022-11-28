from timeit import default_timer
import time

def sum_of_digits(x):
    '''
        Return sum of all digits in a given number
    '''
    dsum = 0
    
    for i in str(x):
        dsum += int(i)
    
    return dsum

def test_three(sum_of_digits):
    '''
        Checks if the given number is divisible by 3 and returns a bool
    '''
    if sum_of_digits % 3 == 0:
        return False
    
    return True

def test_five(x):
    '''
        Checks if the given number is divisible by 5 and returns a bool
    '''    
    x = str(x)
    
    if x[-1] == "5":
        return False
    
    return True

def test_prime(x, prime_list):
    '''
        Checks if the number is a prime and appends it to the given list and returns that list
    '''    
    counter = 0
    
    for i in prime_list:
        if x % i == 0:
            break
        else:
            counter += 1
            
    if counter == len(prime_list):
        prime_list.append(x)
        
def prime(n):
    '''
        Finds given number of prime numbers
    '''    
    prime_list = list()
    prime_list.append(2)
    prime_list.append(3)
    prime_list.append(5)
    
    i = 7
    
    while len(prime_list) < n:
        if test_five(n):
            if test_three(n):
                test_prime(i, prime_list)
                
        i += 2
        
    return prime_list

def py_prime():
    print("---Python Generator---")
    print("How many primes to generate?")
    
    while True:
        try:
            n = int(input())
            break
        except:
            print("Please enter a positive number.")
            continue
        
    start_gen = time.time()
    prime_list = prime(n)    
    end_gen = time.time()
    
    gen_duration_ms = (end_gen - start_gen) * 10**3
    
    print("Do you want to print the results?")
    print("[1] - Yes")
    print("[2] - No")
    
    while True:
        try:
            u = int(input())
        except:
            print("Please the number.")
            continue
    
        match u:
            case 1:
                start_print = time.time()
                
                for i in prime_list:
                    print(i)
                 
                end_print = time.time()
                
                print_duration = (end_print - start_print) * 10**3
                
                print(f"Time taken to print the primes: {print_duration} ms") 
                                    
                break
            case 2:
                break
            case _:
                print("Invalid input!")
                
    print(f"Time taken to generate the primes: {gen_duration_ms} ms")
    print(f"The final lenght is: {len(prime_list)}")
        
                
    
    

# # # MAIN # # #
def main():
    # Input the n of prime numbers
    print("Input the number of prime numbers to generate:")
    n = int(input())
    # Start a timer
    start = default_timer()
    # Searches for the primes
    prime_list = prime(n)
    # Prints the time taken to get the primes 
    print(default_timer() - start)
    # Start a timer for print
    start = default_timer()
    # Prints all the numbers
    for i in prime_list:
        print(i)
    print(f"Delka: {len(prime_list)}")
    # Prints the time taken for the print
    print(default_timer() - start)

if __name__ == "__main__":
    main()
    
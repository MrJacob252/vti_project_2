import vti_project_2
import numpy as np
import matplotlib.pyplot as plt

def round_up(number, order):
    '''
    Rounds up given number
    '''
    return int(np.ceil(number / order) * order)

def polar_plotter(last_prime, name):
    '''
    Creates a polar graph template with shared settings
    '''
    fig = plt.figure()
    ax = fig.add_subplot(projection='polar')
    

    rmax = round_up(last_prime, len(str(last_prime)))    
    ax.set_rmax(rmax)
    
    ax.get_yaxis().set_visible(False) # turns off Y labels
    # ax.set_rlabel_position(-22.5)
    ax.grid(False) 
    ax.set_title(name, va="bottom")
    
    return ax

def ulam_spiral(num_list):
    '''
    Plots Ulam spiral from given list of numbers
    '''
    # name in the head of the graph
    name = "Ulam Spiral"

    # max size of the plot radius
    last_prime = num_list[-1]
    
    # polar graph template
    ax = polar_plotter(last_prime, name)
    
    # ax.scatter(theta, r, size_of_dot)   
    ax.scatter(num_list, num_list, s=0.1)
    
    plt.show()
    
def sack_spiral(num_list):
    '''
    Plots Sack Spiral from given list of numbers
    '''
    # name in the head of the graph 
    name = "Sack Spiral"
    
    # max size of the plot radius
    last_prime = np.sqrt(num_list[-1])    
    
    # polar graph template
    ax = polar_plotter(last_prime, name)
    
    # ax.scatter(theta, r, size_of_dot)
    ax.scatter(np.sqrt(num_list) * 2 * np.pi ,np.sqrt(num_list), s=0.5, c='purple')
    
    plt.show()
        
def graph_choice(prime_list):
    '''
    User interface to choose whitch graph to plot
    '''
    
    while True:
        print("Which graph to draw?")
        print("[1] - Ulam spiral")
        print("[2] - Sack spiral ")
        print("[9] - Generate new prime number list")
        print("[0] - Quit")

        # user input
        u = input()
        try:
            u = int(u)
        except:
            Exception(print("Please enter a number!"))
        
        match u:
            # Ulamn Spiral
            case 1:
                ulam_spiral(prime_list)
            # Sack Spiral
            case 2:
                sack_spiral(prime_list)
            case 9:
                prime_list = np.array(vti_project_2.prime_num_gen())
            # Exit
            case 0:
                break
            # Catch all other cases
            case _:
                Exception(print("Invalid input! Try again!"))
            
# # # MAIN # # #
def main():
    # Calls a Rust module that generates prime numbers and returns Python list
    # Stores them as numpy array 
    prime_list = np.array(vti_project_2.prime_num_gen())
    
    graph_choice(prime_list)


if __name__ == "__main__":
    main()
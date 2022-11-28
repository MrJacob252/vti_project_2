use std::io;
use std::time::Instant;

fn input() -> u128 {
    //! Asks user for input and converts it to u128 if possible
    //! Loops until user inputs a valid number
    loop {
        let mut n:String = String::new();

        io::stdin()
            .read_line(&mut n)
            .expect("Failed to read the line!");


        let n:u128 = match n.trim().parse() {
            Ok(num) => num,
            Err(_) => {
                println!("Please input a number (positive, non-zero preferably)!");
                continue;
            }
        };

        return n;
    }
}

fn test_three(x:&u128) -> bool {
    //! Tests if number is divisible by 3
    //! Return bool
    match x % 3 {
        0 => return false,
        _ => return true,
    }
}

fn test_five(x:&u128) -> bool {
    //! Tests if number is divisible by 5
    //! Return bool
    match x % 5 {
        0 => return false,
        _ => return true,
    }
}

fn test_seven(x:&u128) -> bool {
    //! Tests if number is divisible by 7
    //! Return bool
    match x % 7 {
        0 => return false,
        _ => return true,
    }
}

fn test_prime(x:u128, prime_list:Vec<u128>) -> Vec<u128> {
    //! Tests all already generated numbers and if there's no match adds new number to the prime list
    let mut counter:u128 = 0;
    let mut prime_list:Vec<u128> = prime_list;

    for i in &prime_list {

        if x % i == 0 {

            break;
        }
        else {
            counter += 1
        }
        

    }
    // Checks if we went through the whole list
    if counter == prime_list.len().try_into().unwrap() {

        prime_list.push(x)
    }
    return prime_list;
}

fn primes(number:u128) -> Vec<u128> {
    //! Generates given number of primes
    let mut prime_list:Vec<u128> = Vec::new();
    
    match number {
        // Handles generatin prime list from size o to size 4 
        0..=4 => {
            let preload:[u128; 4] = [2, 3, 5, 7];

            if number == 0 {
                return prime_list;
            }

            for i in 0..=(number - 1) {
                prime_list.push(preload[i as usize])
            }
        }
        // All other numbers
        _ => {

            let preload:[u128; 4] = [2, 3, 5, 7];
            for i in preload { 
                prime_list.push(i)
            }

            let mut current:u128 = 9;

            while number > prime_list.len().try_into().unwrap() {

                let curry:u128 = current;

                if test_three(&curry) & test_five(&curry) & test_seven(&curry) {
                    prime_list = test_prime(curry, prime_list);
                }

                current += 2
            }
        }
    }
    return prime_list;
}

fn printing(prime_list:&Vec<u128>) {
    //! Asks user if they want to print all of the results
    println!("Do you want to print the results?");
    //println!("Please input the number");
    println!("[1] - Yes");
    println!("[2] - No");

    loop {
        let answer:u128 = input();

        match answer {
            1 => {
                println!("Results:");
                println!("-----------------------");
                let start = Instant::now();

                for i in prime_list {
                    println!("{i}")
                }

                let print_duration = start.elapsed();
                println!("-----------------------");
                println!("Time taken to print the results: {:?}", print_duration);
                break;
            },
            2 => break,
            _ => {
                println!("Please use either 1 or 2");
                continue;
            }
        }
    }

}

pub fn main_primes() -> Vec<u128> {
    //! main function that can be called from python
    
    // Get the size of the list from user
    println!("How many primes to generate?");
    let number:u128 = input();

    // Start generating timer
    let start = Instant::now();

    // Generate the prime list 
    let prime_list = primes(number);

    // Stop generating timer
    let gen_time = start.elapsed();

    // Print the prime list
    printing(&prime_list);

    // Print the final length and generation time
    println!("Time taken to generate the primes: {:?}", gen_time);    
    println!("The final length is: {:?}", prime_list.len());

    return prime_list;
}
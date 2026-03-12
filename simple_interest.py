def calculate_simple_interest(principal, rate, time):
    """
    Calculate the simple interest.
    
    Args:
        principal (float): The principal amount
        rate (float): The annual interest rate
        time (float): The time period in years
        
    Returns:
        float: The simple interest calculated
    """
    return (principal * rate * time) / 100

if __name__ == "__main__":
    try:
        p = float(input("Enter the principal amount: "))
        r = float(input("Enter the rate of interest (in %): "))
        t = float(input("Enter the time in years: "))
        
        interest = calculate_simple_interest(p, r, t)
        print(f"The simple interest is: {interest}")
    except ValueError:
        print("Invalid input. Please enter numerical values.")

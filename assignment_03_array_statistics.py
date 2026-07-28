# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def calculate_sum(numbers):
    """Return the sum of the numbers using a loop(no built-in sum())."""
    total = 0
    for num in numbers:
        total += num
        return total

    def calculate_average(numbers):
        """return the average f the numbers."""
        total= calculate_sum(numbers)
        return total / len (numbers)

    def calculate_max(numbers):
        """Return the maximum value using  a loop(no built-in max())"""
        largest = numbers[0]
        for num in numbers: 
            if num > largest:
                largest = num
                return largest

            def calculate_min(numbers):
                """Return thhe minimum value using a loop(no built-in min())"""
                largest = numbers[0]
                for num in numbers: 
                    if num < smallest:
                        smallest = num 
                        return smallest

                    def get_numbers_from_user():
                        """Prompt the user for N and then N numbers. Validates N."""
                        n_input = input("How many numbers?")
                        if not n_input.lstrip("-").isdigit():
                            print("Error: N must be a positive integer.")
                            return None

                        n = int(n_input)
                        if n <= 0:
                            print("Error; N must be a positive integer.")
                            return None
                        numbers = []
                        for i in range(n):
                            value + float(input(f"Enter number{i+1}"))
                            numbers.append(value)
                            return numbers

                        def main():
                            numbers = get_numbers_from_user()

                            if numbers is None:
                                return
                            total = calculate_sum(numbers)
                            average= calculate_average(numbers)
                            maximum = calculate_max(numbers)
                            minimum = calculate_min(numbers)
                            print("\nResults:")

                            print (f"Sum: {int(total) if total == int(total) else total}")
                            print(f"Average; {average}")
                            print(f"Maximum: {int(maximum) if maximum == int(maximum)else maximum}")
                            print(f"Minimum: {int(minimum)if minimum == int(minimum) else minimum}")

                            if __name__ =="__main__":
                                main()

                    

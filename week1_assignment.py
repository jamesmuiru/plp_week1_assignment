# a program that enables the user to perform mathematical operation
def subtraction():
    first_number=int(input("Enter your first number:"))
    second_number=int(input("Enter your first number:"))
    difference=first_number - second_number
    print(f"The difference is:{difference}")

def addition():
    first_number=int(input("Enter your first number:"))
    second_number=int(input("Enter your first number:"))
    summation=first_number + second_number
    print(f"The sum is:{summation}")   
def multiplication():
    first_number=int(input("Enter your first number:"))
    second_number=int(input("Enter your first number:"))
    product=first_number * second_number
    print(f"The product is:{product}")
def division():
    first_number=int(input("Enter your first number:"))
    second_number=int(input("Enter your first number:"))
    quotient=first_number / second_number
    print(f"The quotient is:{quotient}")
# main function to run the code
def main():
    while True:
        print("\nSelect the operation you want to perform:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            addition()
        elif choice == '2':
            subtraction()
        elif choice == '3':
            multiplication()
        elif choice == '4':
            division()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
main()
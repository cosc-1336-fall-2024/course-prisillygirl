from lists import get_lowest_list_value, get_highest_list_value

def main():
    print ("      MENU")

    while True:
        print("1- Show the list low/high values")
        print("2- Exit")

        choice = input("Choose an option: ")
        
        if choice == '2':
            print("Exiting the program.")
            break

        elif choice == '1':

            numbers = []

            while True:
                value = input("Enter a list value: ")
                if value.lower() == 'stop':
                    break
                try:
                    numbers.append(int(value))
                except ValueError:
                    print("Please enter a valid integer.")
                
                if len(numbers) >= 3:
                    another = input("Do you want to enter another value? (yes/no): ")
                    if another.lower() != 'yes':
                        break
            
            lowest = get_lowest_list_value(numbers)
            highest = get_highest_list_value(numbers)
            
            print(f"The lowest number in the list is: {lowest}")
            print(f"The highest number in the list is: {highest}")

if __name__ == "__main__":
    main()
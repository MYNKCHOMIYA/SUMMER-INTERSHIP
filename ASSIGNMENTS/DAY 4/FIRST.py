import csv
def read_csv(f):
    try:
        with open(f, mode='w',newline='') as file:
            writer = csv.writer(file)
            n = int(input("Enter the number of rows you want to add: "))
            for i in range(n):
                name = input(f"Enter name for row {i+1}: ")
                address = input(f"Enter age for row {i+1}: ")
                phone_no = input(f"Enter city for row {i+1}: ")
                email = input(f"Enter email for row {i+1}: ")
                writer.writerow([name, address, phone_no, email])
    except FileNotFoundError:
        print(f"File {f} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
def display_csv(f):
    try:
        with open(f, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"File {f} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
def main():
    file_name = input("Enter the name of the CSV file: ")
    if not file_name.endswith('.csv'):
        file_name += '.csv'
    while True:
        choice = input('''
        1. Create CSV File
        2. Display CSV File
        3. Exit
        Choose an option: ''')

        if choice == '1':
            read_csv(file_name)
        elif choice == '2':
            display_csv(file_name)
        elif choice == '3':
            print("Exited, thank you for using.")
            break
        else:
            print("Enter a valid input.")
if __name__ == "__main__":
    main()


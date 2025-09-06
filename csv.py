import csv

# Step 1: Create and write names to a CSV file
def write_names_to_csv(filename):
    with open(filename, "w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        while True:
            name = input("Enter a name (or type 'done' to finish): ")
            if name.lower() == "done":
                break
            writer.writerow([name])

# Step 2: Read the CSV file with error handling
def read_csv_file():
    try:
        file_path = input("Enter the file path to read: ")
        with open(file_path, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                print("Name:", row[0])
    except FileNotFoundError:
        print("⚠ File not found. Please check the path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the functions
write_names_to_csv("names.csv")
read_csv_file()
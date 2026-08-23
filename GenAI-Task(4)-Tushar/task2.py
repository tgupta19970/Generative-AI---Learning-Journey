# Task 2 - Read File in a Different Way

# Read the entire file using read() and print it
readFile = open("sales_data.txt", "r")
content = readFile.read()
print("1. Read Entire File")
print(content)
readFile.close()


# Read the first line by using readline()
read_first_line = open("sales_data.txt", "r")
first_line = read_first_line.readline()
print(f"\n2. Read First Line : {first_line.strip()}")

# Read all lines using readline() and convert them into a list of integers


file = open("sales_data.txt", "r")
all_lines = file.readlines()

# Create a empty sales list to store each line into a integer
sales_list = []

for lines in all_lines:
    sales_list.append(int(lines.strip()))

print("\n3. Sales as a list")
print(sales_list)

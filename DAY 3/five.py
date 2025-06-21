#file handling
try:
    with open("DAY%203.txt", "r") as f:
        # read line by line
        for line in f:
            print(line.strip())
except FileNotFoundError:
    print("File not found")
except IOError:
    print("Error reading file")
finally:
    if 'f' in locals():
        f.close()

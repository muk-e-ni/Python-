try:

    with open('my_file.txt', 'w') as file:
        file.write("First line of text.\n")
        file.write("12345 - A number line.\n")
        file.write("This is the third line.\n")

    with open('my_file.txt', 'r') as file:
        content = file.read()
        print(content)

    with open('my_file.txt', 'a') as file:
        file.write("Fourth line added in append mode.\n")
        file.write("56789 - Another number line.\n")
        file.write("Final appended line.\n")

except FileNotFoundError:
    print("File not found error.")
except PermissionError:
    print("You do not have permission to access this file.")
finally:
    print("File operation complete.")
    

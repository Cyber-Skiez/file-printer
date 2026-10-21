try:
    with open('sample.txt') as file:
        content = file.read()

    print("File content: ")
    print(content)
    print("Done")

except FileNotFoundError:
    print("Error: File not found.")


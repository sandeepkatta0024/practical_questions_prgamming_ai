def read_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            print("File content:")
            print(content)

    except FileNotFoundError:
        print("Error: The file does not exist.")

    except Exception as e:
        print("An unexpected error occurred:", e)


read_file("/Users/sandeepkatta77/Desktop/junk/meow.txt")


def write_file(filename, text):
    try:
        with open(filename, "w") as file:
            file.write(text)
            print("Text successfully written to file.")

    except Exception as e:
        print("Error writing to file:", e)


write_file("/Users/sandeepkatta77/Desktop/junk/meow.txt", "Hello Sandeep\nWelcome to Python file handling.")
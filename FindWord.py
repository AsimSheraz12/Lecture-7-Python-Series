# Find Word Occur on which line number in a text file

def findWordline(word):
    with open("practice.txt", "r") as file:
        lines = 1;
        data = True
        while data:
            data = file.readline()
            if word in data:
                print(f"Word '{word}' found on line {lines}")
                return
        lines += 1
    return -1

word_to_find = input("Enter the word to find: ")
print(findWordline(word_to_find))
f = open("practice.txt", "w") # Open the file in write mode

data = "Hi Everyone,\nWe are Learning File I/O\nusing Java.\nI like Programming in Java."
f.write(data) # Write data to the file
f.close() # Close the file after writing

f = open("practice.txt", "r+") # Open the file in read mode

data = f.read() # Read the data from the file
#print(data) # Print the data read from the file
data = data.replace("Java", "Python") # Replace "Java" with "Python" in the data
f.seek(0) # Move the file pointer to the beginning of the file
f.write(data) # Write the modified data back to the file
f.close() # Close the file after writing

f = open("practice.txt", "r") # Open the file in read mode
data = f.read() # Read the modified data from the file

index = data.find("learning") # Find the index of the substring "Learning" in the data

if index != -1:
    print("Substring found at index:", index)
else:
    print("Substring not found.")
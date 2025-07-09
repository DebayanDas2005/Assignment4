#sample.txt file ---->
#     Line 1: This is a sample text file.
#     line 2: It contains multiple lines.

try:
    file = open('sample.txt','r')
    reading_file = file.read()
    print(reading_file)
    file.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")

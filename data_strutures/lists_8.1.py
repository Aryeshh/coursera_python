'''Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.'''

fname = input('Enter file name:')
fh = open(fname)
lst = list()

for line in fh:
    line = line.rstrip()  # Remove trailing whitespace
    words = line.split()  # Split the line into words
    for word in words:
        if word not in lst:  # Only append if the word is not already in the list
            lst.append(word)
            
lst.sort()  # Sort the list alphabetically
print(lst)  # Print the sorted list
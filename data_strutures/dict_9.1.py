'''Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.'''

name = input("Enter file:")
if len(name) < 1:
    name = "coursera_python\mbox-short.txt"
handle = open(name)
counts = dict()

for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    counts[words[1]] = counts.get(words[1],0) + 1  # call me to understand what i did here
    
    

#print(max(counts, key=counts.get), max(counts.values())) 

'''         or       '''

largest = None
email = None
for name,count in counts.items():
    if largest is None or count > largest:             
        largest = count
        email = name
print(email, largest)




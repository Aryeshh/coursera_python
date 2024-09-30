'''Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.'''

fname = input("Enter file name: ") # file name = coursera_python\mbox-short.txt
fh = open(fname)
fsum = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    fsum = fsum + float(line[21:])
    #print(line)
    
print("Average is",fsum/count)

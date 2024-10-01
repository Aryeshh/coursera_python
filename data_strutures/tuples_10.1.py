'''Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
Desired Output
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1 '''

name = input("Enter file:")
if len(name) < 1:
    name = "coursera_python/mbox-short.txt"
handle = open(name)
counts = dict()

for line in handle:
    line = line.strip()
    if not line.startswith('From '):
        continue
    words = line.split()
    time = words[5].split(':')
    hours = time[0]
    counts[hours] = counts.get(hours,0) + 1

histogram = sorted( [ (k,v) for k,v in counts.items()], reverse=False) # a complex funtion you'll know if you will watch the tuples video 
for k,v in histogram:
    print(k,v)
    
'''     or     '''

# lst = list()                                                           
# for k,v in counts.items():                      # to append values from a list of tupple data i.e [('09':2 ,'04':3)] into a list
#     newtupple = (k,v)                           # we can aslo append directly but i used a temp. tuple to keep the code readable 
#     lst.append(newtupple)                       # append and exit  the loop, now all items are in list
# lst = sorted(lst, reverse=False)                # sort the list in asecding order (by default) , we added data into list bcoz we cant sort tuples

# for k,v in lst:                                 
#     print(k,v)
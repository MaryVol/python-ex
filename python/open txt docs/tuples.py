# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

# name = input("Enter file:")
# if len(name) < 1 : name = "mbox-short.txt"
time = list()
hour = list()
count = dict()
handle = open('mbox-short.txt')
for line in handle:
    if 'From ' in line:
        words = line.split()
        for word in words:
            if ':' in word:
                time.append(word.split(':'))
for tim in time:
    hour.append(tim[0])
for h in hour:
    count[h] = count.get(h,0) + 1
for k,v in sorted(count.items()):
    print(k,v)
            

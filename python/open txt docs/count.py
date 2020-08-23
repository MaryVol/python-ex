# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

# name = input("Enter file:")
# if len(name) < 1 : name = "mbox-short.txt"
handle = open("mbox-short.txt")
mail = dict()
for line in handle:
    if 'From: ' in line:
        words = line.split()
        for word in words :
            if '@' in word: 
                mail[word] = mail.get(word,0) + 1
bigvalue = None
bigkey = None
for k,v in mail.items():
    if bigvalue is None or bigvalue < v:
        bigvalue = v
        bigkey = k
print(bigkey, bigvalue)  
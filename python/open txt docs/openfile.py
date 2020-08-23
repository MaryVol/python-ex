fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('incorrect filename', fname)
    quit()
for line in fh:
    print(line.upper().rstrip())

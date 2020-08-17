fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
print(line.rstrip())


new=list()
for word in data():
    if word in new :
        continue
    new = new.append(word)
print(new.sort())

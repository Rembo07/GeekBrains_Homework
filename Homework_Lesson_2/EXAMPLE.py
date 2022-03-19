ls = [ 'здесь когдато', 'был на этом', 'месте я с семьей']
for i in range(len(ls)):
    splitten = ls[i].split(' ')
    lens = len(splitten) - 1
    indexon = splitten[lens].upper()
    ls.append(indexon)
print(ls)
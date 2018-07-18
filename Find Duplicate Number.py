#Find the Duplicate Number

def duplicate(L):
  temp = []
  for i in L:
    if i in temp:
      return i
    else:
      temp.append(i)

b = [1,3,4,2,2]
print(duplicate(b))
    

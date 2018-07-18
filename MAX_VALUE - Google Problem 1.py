##MAX_VALUE
##You are given a list of distinct integers from 0 to a value MAX_VALUE.
##Your task is to produce a string that describes numbers missing from the list.
##The items should be sorted in ascending order and separated by commas.
##When a gap spans only one number, the item is the number itself;
##when a gap is longer, the item comprises the start and the end of the gap,
##joined with a minus sign.
##
##For instance: 
##
##MAX_VALUE = 1000
##VALUES = [0, 1, 2, 50, 52, 75]
## 
#max value (first google problem)

max = 1000

def max(val):
  newList = []
  val.append(1000)
  for i in range(len(val)-1):
    if  val[i+1] - (val[i])  > 2:
      newList.append(str(val[i]+1) + "-" + str(val[i+1]-1))
    elif  val[i+1] - (val[i])  == 2:
      newList.append(str(val[i]+1))
    elif (i == len(val)-1) and (val[i]+1 != 1000):
      newList.append(str(val[i]+1) + "-" + "1000")
  newStr = ",".join(newList)
  return newStr


vals = [0, 1, 2, 50, 52, 75]
print(max(vals))

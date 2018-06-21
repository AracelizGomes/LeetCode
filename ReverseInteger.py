def reverse(num):
    newnum = []
    if (num < 0):
        num = num * -1
        num = list(str(num))
        for i in range(len(num)):
            newnum.insert(0, (num[i]))
        newnum = "".join(newnum)
        newnum = int(newnum)
        newnum = newnum*-1
        return newnum
          
    else:
        num = list(str(num))
        for i in range(len(num)):
            newnum.insert(0, (num[i]))
        newnum = "".join(newnum)
        newnum = int(newnum)
        return newnum

print(reverse(-124))
print(reverse(8124))

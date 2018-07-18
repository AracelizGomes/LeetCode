#Hamming Distance

def Hamming(x, y):
  bin_x = '{0:08b}'.format(x)
  str_x = str(bin_x)
  list_x = []
  for digit in str_x:
    list_x.append(int(digit))
    
  bin_y = '{0:08b}'.format(y)
  str_y = str(bin_y)
  list_y = []
  for digit in str_y:
    list_y.append(int(digit))
    
  counter = 0
  for i in range(len(list_x)):
    if list_x[i] != list_y[i]:
      counter +=1
  return counter
  
print(Hamming(2, 4))

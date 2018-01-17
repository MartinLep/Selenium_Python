array = [1,2,3,4,5,6,7,8,9,0]
del  array[2:4]
print(array)


matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]]

print([[row[i] for row in matrix] for i in range(4)])
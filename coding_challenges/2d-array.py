array = [
  [-1, 1, -1 ,0, 0, 0],
  [-1 ,1 ,-1, 0 ,0, 0,],
  [-1 ,-1 ,-1, 0 ,0, 0],
  [0, -9, 2, -4, -4, 0],
  [-7, 0, 0, -2, 0, 0],
  [0, 0, -1, -2, -4, 0]
] 

# -1 1 -1 0 0 0
# 0 -1 0 0 0 0
# -1 -1 -1 0 0 0
# 0 -9 2 -4 -4 0
# -7 0 0 -2 0 0
# 0 0 -1 -2 -4 0

# for i in range(6):
#   for j in range(6):
#     array[i][j] = int(input(f'Enter array[{i}][{j}]: '))

arrayprint = ''

for i in range(6):
  for j in range(6):
    arrayprint = f'{arrayprint}{array[i][j] } '
  arrayprint = f'{arrayprint}\n'

def hourglassSum(arr):
    sum = 0 
    # highest = 0
    for ii in range(4):
        for jj in range(4):
            sum = 0
            # strf = ''
            for i in range(3):
                for j in range(3):
                    if (not (((i == 1)and(j==0)) or ((i==1)and(j==2)))):
                        sum = sum+arr[ii+i][j+jj]
                        # strf = f'{strf} + {arr[ii+i][j+jj]}'
            if(ii==0 and jj==0):
              highest = sum
            elif(highest < sum):
              highest = sum    
            # print(f'{strf} | Sum = {sum} | Highest = {highest}')
    return highest




print(arrayprint)
print("sum", hourglassSum(array))


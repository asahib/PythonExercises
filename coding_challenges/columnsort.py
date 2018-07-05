import csv

def columnsort(text):
  lines = text.split('\n')
  lines = [x for x in lines if x!='']
  for ln, li in enumerate(lines):
    lines[ln] = li.split(',')
  lines = bubblesort(lines)
  return list2string(lines)

def list2string(lines):
  temp = ['' for x in lines]
  for index, item in enumerate(lines):
    temp[index] = ','.join(item)
  return('\n'.join(temp))
  
def bubblesort(line):
  nochange = True
  while(nochange):  
    nochange=False
    for i in range(0,len(line[0])-1):
      if(line[0][i].lower() > line[0][i+1].lower()):
        line = exchange(line,i,i+1)
        nochange = True
  return line  

def exchange(line, i, j):
  temp = ''
  for value in line:
    temp = value[i] 
    value[i] = value[j]
    value[j] = temp
  
  return line

# filename = "input.txt"
# file = open(filename,'r')
# for line in file:
# #   print(line)

# print(type(file))
# text = """
# Beth,charles,Charles,Adam,Eric\n
# 17945,10091,10088,3907,10132\n
# 2,12,13,48,11
# """

# print(columnsort(file))

strng = ''
with open('input.csv', newline='\n') as csvfile:
  spamreader = csv.reader(csvfile)
  print(type(spamreader))
  for row in spamreader:
    strng = f"{strng}{(','.join(row))}\n"

strng = columnsort(strng)
print(strng)

text_file = open("output.csv","w")
text_file.write(strng)
text_file.close()


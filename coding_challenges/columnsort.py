import csv
import sys

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

def main():
  if(sys.argv[1] and sys.argv[2]):
    inputfilename = sys.argv[1]
    outputfilename = sys.argv[2]
    strng = ''
    with open(inputfilename, newline='\n') as csvfile:
      inputcontents = csv.reader(csvfile)
      print(type(inputcontents))
      for row in inputcontents:
        strng = f"{strng}{(','.join(row))}\n"
    strng = columnsort(strng)

  with open(outputfilename,"w") as ocsvfile:
    ocsvfile.write(strng)

if __name__ == '__main__':
  main()
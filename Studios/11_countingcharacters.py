def counting(string):
  str_lst = [char for char in string]
  d = {x:str_lst.count(x) for x in str_lst}
  return(d)

sntrix = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc accumsan sem ut ligula scelerisque sollicitudin. Ut at sagittis augue. Praesent quis rhoncus justo. Aliquam erat volutpat. Donec sit amet suscipit metus, non lobortis massa. Vestibulum augue ex, dapibus ac suscipit vel, volutpat eget massa. Donec nec velit non ligula efficitur luctus."
for char, count in counting(sntrix).items():
  print(f'{char} : {count}')

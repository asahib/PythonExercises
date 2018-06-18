
class Page:      
  def __init__(self, notes = ' '): # Constructor for the Page which will create a new page, with notes if any
    self.line = 0
    self.pagenotes = {self.line: notes}

  def addnotes(self,notes,lineno=False): # Add notes to the Page. 
    # This will append the notes to the last line by default. If a line number is specified, then this will overwrite the existing notes and add new one.
    if not lineno:
      lineno = self.line+1
    if(lineno > self.line+1):
      print(f"System will be inserting your contents in line no: {self.line+1} since we don't want blank lines in between")
      lineno = self.line+1
    elif(lineno < 0):
      print(f"You have entered an invalid line no. Aborting the execution!")
      return False
    elif lineno == self.line+1: # Adding a new page
      self.line = self.line+1
    self.pagenotes[lineno] = notes
    return True
  
  def deletenotes(self,lineno):  # Delete any notes in the line no:, once the line is deleted, the system will pull the next line notes to the deleted line 
    # and reduce the line by one
    if(lineno in self.pagenotes):
      for ln in range(self.line):
         self.pagenotes[ln] = self.pagenotes[ln+1]
      del(self.pagenotes[self.line])
      self.line -= 1

  def __repr__(self): 
    page_str = ''
    for i in range(self.line+1):
      page_str = f'{page_str} {i} : {self.pagenotes[i]}\n'
    return (page_str)
  
class Book:
  def __init__(self, title):
    self.title = title
    self.lastpage = 0
    self.pages = {self.lastpage: Page()}

  def addpages(self,notes): # Add pages to the book with specified notes
    newpage = Page(notes)
    self.pages[self.lastpage] = newpage
    self.lastpage += 1
  
  def addnotestopage(self,pageno,notes): # Add notes to the exiting page in a book
    if(pageno >= self.lastpage):
      pageno = self.lastpage
      self.lastpage +=1
  # def addnotes(self,notes,lineno=False):
    self.pages[pageno].addnotes(notes)
    
  def __repr__(self):
    book_str = f'**** Book Title : {self.title} ****\n\n'
    for pgno, pg in self.pages.items():
      book_str = f'{book_str}Page no: {pgno} \n{pg}\n'
    return book_str

  def __str__(self):
    book_str = f'**** Book Title : {self.title} ****\n\n'
    for pgno, pg in self.pages.items():
      book_str = f'{book_str}Page no: {pgno} \n{pg}\n'
    return book_str


def main():
  # page1 = Page('Azhar')
  # print(page1)

  book1=Book("Book 1")
  book1.addpages("B1 Page 1")
  book1.addpages("B1 Page 2")
  book1.addnotestopage(1,"B1 P1 Notes 1")
  book1.addnotestopage(0,"B1 P0 Notes 1")
  # print(book1)
  str1 = str(book1)
  # print(str1)
  

  # f= open("book1.txt","w+")
  # f.write(str1)
  # f.close() 

  f=open("book1.txt", "r")
  if f.mode == 'r':
    contents =f.read()
    str2 = str(contents)
    print(str2)
    list1 = str2.split()
    print(list1)
  f.close()

  # book1=Book("Book 2")
  # book1.addpages("B2 Page 1")
  # book1.addpages("B2 Page 1")
  # book1.addnotestopage(1,"B2 P1 Notes 1")
  # book1.addnotestopage(0,"B2 P0 Notes 1")
  # print(book1)

if __name__ == '__main__':
  main()
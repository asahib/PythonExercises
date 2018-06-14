
class Page:
  def __init__(self, notes = ' '):
    self.line = 0
    self.pagenotes = {self.line: notes}

  def addnotes(self,notes,lineno=False):
    if not lineno:
      lineno = self.line+1
    if(lineno > self.line+1):
      print(f"System will be inserting your contents in line no: {self.line+1} since we don't want blank lines in between")
      lineno = self.line+1
    elif(lineno < 0 or lineno.isalpha()):
      print(f"You have entered an invalid line no. Aborting the execution!")
      return False
    elif lineno == self.line+1: # Adding a new page
      self.line = self.line+1
    self.pagenotes[lineno] = notes
    return True
  
  def deletenotes(self,lineno):
    if(lineno in self.pagenotes):
      for ln in range(self.line):
         self.pagenotes[ln] = self.pagenotes[ln+1]
      del(self.pagenotes[self.line])
      self.line -= 1

  def __repr__(self):
    page_str = ''
    for i in range(self.line+1):
      page_str = f'{page_str}{i} : {self.pagenotes[i]} \n'
    return (page_str)
  
class Book:
  def __init__(self, title):
    self.title = title
    self.lastpage = 0
    self.pages = {self.currentpage: Page()}

  def addpages(self,notes):
    newpage = Page(notes)
    self.lastpage += 1
    self.pages[self.lastpage] = newpage
  
  # def addnotes(self,pageno,notes):
  
  def __repr__(self):
    book_str = f'Book Title : {self.title}\n'
    for pgno, pg in self.pages.items():
      book_str = f'{book_str}Page no: {pgno} \n {pg}\n'
    return book_str

def main():
  page1 = Page('Azhar')
  print(page1)

  book1 = Book("testing")
  book1.addpages("Azhar1")
  book1.addpages("Azhar2")
  print(book1)

if __name__ == '__main__':
  main()
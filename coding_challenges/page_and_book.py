
class Page:
  def __init__(self, notes = ' '):
    self.content = notes

  def addnotes(self,notes):
    self.content = notes

  def __repr__(self):
    return (self.content)
  
class Book:
  def __init__(self, title, ):
    self.title = title
    self.currentpage = 1
    self.pages = [Page()]

  def addpages(self,notes):
    newpage = Page(notes)
    self.currentpage += 1
    self.pages.append(newpage)
  
  def __repr__(self):
    return(' '.join(str(pgs) for pgs in self.pages))

def main():
  page1 = Page('Azhar')
  print(page1)

  book1 = Book("testing")
  book1.addpages("Azhar1")
  book1.addpages("Azhar2")
  print(book1)

if __name__ == '__main__':
  main()
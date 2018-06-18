class Post:
  def __init__(self, title, author, body):
    self.title = title
    self.author = author
    self.body = body
    self.likes = 0

    # Allow people to "like" posts, a la Facebook
  def like(self):
    self.likes += 1

  def __repr__(self):
    strng = f"{self.title} by {self.author}"
    return strng


class VideoPost(Post):
  def __init__(self, title, author, url):
    super().__init__(title, author, None)
    self.video_url = url
    self.plays = 0

    # track plays of the video
  def play(self):
    self.plays += 1

  def __str__(self):
    return self.title + " played " + str(self.plays) + " times"

class LinkPost(Post):
  def __init__(self, title, author, url):
    super().__init__(title, author, None)
    self.url = url
    self.click = 0
  
  def clicks(self):
    self.click += 1
  
  def __str__(self):
    return f'{self.title} clicked {self.click} times'

class ImagePost(Post):
  def __init__(self, title, author, file_name):
    super().__init__(title, author, None)
    self.file_name = file_name
  
  def __str__(self):
    strng = f'{self.title} filename {self.file_name} '
    return strng



def main():
    # plain_post = Post("10 Best Albums of 2016", "Chris Bay", "1. Little Scream - Cult Following 2. ...")
    # vid_post = VideoPost("Little Scream - Love As a Weapon", "Chris Bay", "https://youtu.be/Tq4Vw4MB6eA")

    # vid_post.play()
    # vid_post.play()

    # print(vid_post)
    # print(plain_post)

  plain_post = Post("10 Best Albums of 2016", "Chris Bay", "1. Little Scream - Cult Following 2. ...")
  vid_post = VideoPost("Little Scream - Love As a Weapon", "Chris Bay", "https://youtu.be/Tq4Vw4MB6eA")
  pic_post = ImagePost("Cats in space", "Crystal Martin", "spacecats.gif")
  url_post = LinkPost("LaunchCode's LC101", "LaunchCode Staff", "https://www.launchcode.org/lc101")

  vid_post.play()
  vid_post.play()
  url_post.clicks()

  print(vid_post)
  print(plain_post)
  print(url_post)
  print(pic_post)


if __name__ == "__main__":
    main()

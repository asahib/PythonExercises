def test(s1,s2):
  print(s1, " | ", s2, " : ", s1==s2)

def replace(s, old, new):
  split_list = s.split(old)
  return new.join(split_list)

test(replace('Mississippi', 'i', 'I'), 'MIssIssIppI')


s = 'I love spom! Spom is my favorite food. Spom, spom, spom, yum!'
test(replace(s, 'om', 'am'),
       'I love spam! Spam is my favorite food. Spam, spam, spam, yum!')

test(replace(s, 'o', 'a'),
       'I lave spam! Spam is my favarite faad. Spam, spam, spam, yum!')
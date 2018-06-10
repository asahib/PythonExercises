# Write a function that will return a string of country codes from an argument that is a string of prices (containing dollar amounts following the country codes). 
# Your function will take as an argument a string of prices like the following: "US$40, AU$89, JP$200". In this example, the function would return the string "US, AU, JP".

# Hint: You may want to break the original string into a list, manipulate the individual elements, then make it into a string again
from string import ascii_uppercase

def testEqual(s1,s2):
  print(s1, " | ", s2, " : ", s1==s2)

def get_country_codes(strng):
  new_list = strng.split(', ')
  new_str = ', '.join([str(item[0]+item[1]) for item in new_list])
  return new_str

testEqual(get_country_codes("NZ$300, KR$1200, DK$5"), "NZ, KR, DK")
testEqual(get_country_codes("US$40, AU$89, JP$200"), "US, AU, JP")
testEqual(get_country_codes("AU$23, NG$900, MX$200, BG$790, ES$2"), "AU, NG, MX, BG, ES")
testEqual(get_country_codes("CA$40"), "CA")

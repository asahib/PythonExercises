# Write a function analyze_text that receives a string as input. Your function should count the number of alphabetic characters (a through z, or A through Z) in the text and 
# also keep track of how many are the letter 'e' (upper or lowercase).

# Your function should return an analysis of the text in the form of a string phrased exactly like this:

# “The text contains 240 alphabetic characters, of which 105 (43.75%) are ‘e’.”

# You will need to make use of the isalpha function, which can be used like this
def testEqual(str1, str2):
  print(True if str1 == str2 else False)

def analyze_text(text):
  count_alpha = 0
  count_e = 0
  for char in text:
    if(char.isalpha()):
      count_alpha += 1
      if(char=='e' or char== 'E'):
        count_e+=1
  percentage = count_e/count_alpha * 100
  if(percentage%1==0):
    percentage_str = str(percentage)
  else:
    percentage_str = "{:.10f}".format(percentage)
  return f"The text contains {count_alpha} alphabetic characters, of which {count_e} ({percentage_str}%) are 'e'."

# Don't copy these tests into Vocareum!
# Note that depending on whether you use str.format or string concatenation
# your code will pass different tests. As long as your code passes either
# tests 1-3 OR tests 4-6, it should pass in Vocareum. See below for more details.


# Tests 1-3: solutions using string concatenation should pass these
text1 = "Eeeee"
answer1 = "The text contains 5 alphabetic characters, of which 5 (100.0%) are 'e'."
testEqual(analyze_text(text1), answer1)

text2 = "Blueberries are tasteee!"
answer2 = "The text contains 21 alphabetic characters, of which 7 (33.3333333333%) are 'e'."
testEqual(analyze_text(text2), answer2)

text3 = "Wright's book, Gadsby, contains a total of 0 of that most common symbol ;)"
answer3 = "The text contains 55 alphabetic characters, of which 0 (0.0%) are 'e'."
testEqual(analyze_text(text3), answer3)

# Tests 4-6: solutions using str.format should pass these
text4 = "Eeeee"
answer4 = "The text contains 5 alphabetic characters, of which 5 (100.0%) are 'e'."
testEqual(analyze_text(text4), answer4)

text5 = "Blueberries are tasteee!"
answer5 = "The text contains 21 alphabetic characters, of which 7 (33.33333333333333%) are 'e'."
testEqual(analyze_text(text5), answer5)

text6 = "Wright's book, Gadsby, contains a total of 0 of that most common symbol ;)"
answer6 = "The text contains 55 alphabetic characters, of which 0 (0.0%) are 'e'."
testEqual(analyze_text(text6), answer6)

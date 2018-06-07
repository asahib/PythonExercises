def testEqual(str1, str2):
  print(True if str1 == str2 else False)

def remove(substr,original_string):
  index = original_string.find(substr)
  if index < 0:
    return original_string
  return_str = original_string[:index] + original_string[index+len(substr):]
  return return_str

testEqual(remove('an', 'banana'), 'bana')
testEqual(remove('cyc', 'bicycle'), 'bile')
testEqual(remove('iss', 'Mississippi'), 'Missippi')
testEqual(remove('egg', 'bicycle'), 'bicycle')
testEqual(remove('oo', 'Yahoohoo'), 'Yahhoo')
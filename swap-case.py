myString = 'Www.HackerRank.com'
#[letter.lower() if letter.isupper() else letter.upper() for letter in myString]##==> changes chars in the string and put chars inside a list
#add them(list of char) into a empty string with join method
myString = ''.join([letter.lower() if letter.isupper() else letter.upper() for letter in myString])
print(myString)
#
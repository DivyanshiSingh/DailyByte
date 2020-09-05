"""
This question is asked by Google. Given a string, return whether or not it uses capitalization correctly.
 A string correctly uses capitalization if all letters are capitalized, no letters are capitalized, or only the 
 first letter is capitalized.

Ex: Given the following strings...

"USA", return true
"Calvin", return true
"compUter", return false
"coding", return true
"""
# string=["USA","Calvin","compUter","coding"]
result=0
s=input()
if s[0].isupper() and all(i.isupper() for i in s[1:]):
	result=True
	print(s[1:])
if s.isupper()==True:
	result=True
if s.islower()==True:
	result=True
print(result)






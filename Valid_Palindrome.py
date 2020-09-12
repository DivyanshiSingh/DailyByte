def checker(s):
	s=s.lower()
	if s==s[::-1]:
		return True
	else:
		return False

def main():
	s=input()
	print(checker(s))

main()
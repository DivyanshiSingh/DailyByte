def checker(s):
	x=y=0
	for i in s:
		if i=="L":
			x-=1
		if i=="R":
			x+=1
		if i=="U":
			y+=1
		if i=="D":
			y-=1
	if x==0 and y==0:
		return True
	else:
		return False

def main():
	s=input()
	print(checker(s))

main()

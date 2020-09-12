def fun(s):
	d={}
	for i in s:
		if i in d:
			d[i]+=1
		if i not in d:
			d[i]=1
	for i in s:
		if d[i]==1:
			return i


def main():
	s=input()
	print(fun(s))

main()
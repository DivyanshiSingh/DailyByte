def fun(s,t):
	l=len(s)
	if len(s)==len(t):
		return " "
	if l==len(t)-1:
		d_s={}
		d_t={}

		for i in list(s):
			if i in d_s.keys():
				d_s[i]+=1
			elif i not in d_s.keys():
				d_s[i]=1
		for i in list(t):
			if i in d_t.keys():
				d_t[i]+=1
			elif i not in d_t.keys():
				d_t[i]=1
		for i in list(t):
			if i not in list(s):
				return i
			elif i in list(s):
				if d_t[i]!=d_s[i]:
					return i
		print(d_s,d_t)


def main():
	s=input("Enter s: ")
	t=input("Enter t: ")
	print(fun(s,t))

main()
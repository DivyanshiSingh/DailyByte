def fun(s):
	i=0
	temp=list(s)
	while("".join(temp)!="".join(temp)[::-1] and i<=len(temp)):
		
		temp=list(s)
		del temp[i]
		i+=1
			# print(temp)
	
	if "".join(temp)!="".join(temp)[::-1]:
		return False
	else:
		return True

def main():
	s=input()
	print(fun(s))

main()
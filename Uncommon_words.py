def fun(s1,s2):
	s1=set(s1.split())
	s2=set(s2.split())
	print("S1: ",s1,"\nS2",s2)
	# print(s1-s2)


	return (s1.union(s2))-(s1&s2)
def main():
	s1=input("Enter s1")
	s2=input("Enter s2")
	print(fun(s1,s2))



main()
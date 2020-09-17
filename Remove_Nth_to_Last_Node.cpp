#include<bits/stdc++.h>
using namespace std;

int main()
{
	list<int> l={1,2,3};
	int a=0;
	int n;
	
	cin>>n;
	auto i=l.begin();
	while(i!=l.end())
	{
		if(a==l.size()-n)
		{
			i=l.erase(i);
		}
		a++;
		i++;
	}
	for(const auto& elm: l)
	{
		cout<<elm<<" ";
	}
	// cout<<endl;
	// cout<<l.size();
	return 0;
}
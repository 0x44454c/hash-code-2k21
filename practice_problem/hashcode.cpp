#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <fstream>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
#include<stdio.h>
#include<stdlib.h>
#include<bits/stdc++.h>
#include<array>
#define ll long long int
#define endl "\n"
#define fastio ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define mod 1000000007
#define PI 3.1415926535
using namespace std;

class Pizza{
	public:
	int id;
	int size;
};
bool ValueCmp(Pizza const & a, Pizza const & b)
	{
    return a.size < b.size;
	}



int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt","w",stdout);
	int m,t2,t3,t4;
	cin>>m>>t2>>t3>>t4;
	int n_ing;
	string s_ing;
	vector<vector<string> > ingre(m);
	Pizza piz[m];
	for(int i=0;i<m;i++){
		piz[i].id=i;
		cin>>n_ing;
		piz[i].size=n_ing;
		for(int j=0;j<n_ing;j++){
			cin>>s_ing;
			ingre[i].push_back(s_ing);
		}
	}
	sort(piz,piz+m,ValueCmp);
	int tot_pizza=m;
	int team_4=min(tot_pizza/4,t4);
	tot_pizza-=team_4*4;
	int team_3=min(tot_pizza/3,t3);
	tot_pizza-=team_3*3;
	int team_2=min(tot_pizza/2,t2);
	tot_pizza-=team_2*2;

	int tot_dil=team_2+team_3+team_4;
	reverse(piz,piz+m);
	cout<<tot_dil<<endl;
	int piz_index=0;
	for(int i=0;i<team_4;i++){
		cout<<4<<" ";
		for(int j=piz_index;j<piz_index+4;j++){
			cout<<piz[j].id<<" ";
		}
		piz_index+=4;
		cout<<endl;
	}
	for(int i=0;i<team_3;i++){
		cout<<3<<" ";
		for(int j=piz_index;j<piz_index+3;j++){
			cout<<piz[j].id<<" ";
		}
		piz_index+=3;
		cout<<endl;
	}
	for(int i=0;i<team_2;i++){
		cout<<2<<" ";
		for(int j=piz_index;j<piz_index+2;j++){
			cout<<piz[j].id<<" ";
		}
		piz_index+=2;
		cout<<endl;
	}




	return 0;
}

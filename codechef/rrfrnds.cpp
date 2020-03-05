#include <bits/stdc++.h>
using namespace std;

vector<string> users(2010);
vector<int> friends[2010];

int main(){
	int N,count,i,j;
	cin >> N;
	count = 0;
	
	for (i=0; i<N; ++i){
		cin >> users[i];
		for (j=0; j<N; ++j){
			if (users[i][j]=='1'){
				friends[i].push_back(j);
				friends[j].push_back(i);
			}
		}
	}
	
	for (i=0; i<N; ++i){
		for (j=i+1; j<N; ++j){
			if (users[i][j]=='0'){
				for(auto iter=friends[i].begin(); iter!=friends[i].end(); ++iter){
					if (users[*iter][j] == '1'){
						count += 2;
						break;
					}
				}
			}
		}	
	}
	
	cout << count;
	return 0;
}

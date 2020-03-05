#include <bits/stdc++.h>
using namespace std;

bool users[2010][2010];
bool requests[2010][2010];

int main(){
	int N,count,i,j,k,l;
	char c;
	cin >> N;
	count = 0;
	
	for (i=0; i<N; ++i){
		for (j=0; j<N; ++j){
			cin >> c;
			if (c == '1'){
				users[i][j] = true;
			} else {
				users[i][j] = false;
			}
			requests[i][j]= false;
		}
	}
	
	for (i=0; i<N; ++i){
		for (j=0; j<N; ++j){
			if (i!=j && !users[i][j] && !requests[i][j] && !requests[j][i]){
				for (k=0; k<N; ++k){
					if (k!=i&&k!=j && users[i][k] && users[j][k]){
						requests[i][j]=requests[j][i]=true;
						count+=2;
						break;
					}
				}
			}
		}
	}
	
	cout << count;
	return 0;
}

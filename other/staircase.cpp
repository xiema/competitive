#include <bits/stdc++.h>
using namespace std;

typedef unsigned long long ll;

ll c(int n, int r){
	ll res = 1;
	for (int i=1; i<=r; ++i){
		res *= n - r + i;
		res /= i;
	}
	return res;
}

int main(){
	int t,n,pos1,pos2;
	ll total;
	cin >> t;
	while (t-- > 0){
		cin >> n;
		total=0;
		if (n){
			if (n%2){
				pos2=n/2;
				pos1=1;
			} else {
				pos2=n/2;
				pos1=0;
			}
			while (pos2 >=0){
				ll temp = c(pos2+pos1, pos1);
				//cout << temp << '\n';
				total = total + temp;
				--pos2;
				pos1+=2;
			}
		}
		cout << total << '\n';
	}
}

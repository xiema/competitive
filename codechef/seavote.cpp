#include <bits/stdc++.h>
using namespace std;

int main(){
	int T,N,sum,a,count;
	cin >> T;
	while (T-- > 0){
		sum=0; count=0;
		cin >> N;
		for (int i=0; i<N; ++i){
			cin >> a;
			if (a > 0){
				sum += a;
				++count;
			}
		}
		if (sum < 100){
			cout << "NO\n";
		} else {
			if ((sum-100)/count){
				cout << "NO\n";
			} else {
				cout << "YES\n";
			}
		}
	}

	return 0;
}

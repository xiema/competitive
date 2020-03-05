#include <bits/stdc++.h>
using namespace std;

int arr[100010];

int main(){
	int arr[100000];
	int N,Q,A,B,t,count;
	cin >> N >> Q;
	
	while (Q--){
		cin >> t >> A >> B;
		if (t){
			count = 0;
			for (int i=A; i<=B; ++i){
				if (arr[i]%3 == 0){
					++count;
				}
			}
			cout << count << '\n';
		} else {
			for (int i=A; i<=B; ++i){
				++arr[i];
			}
		}
	}
	
	return 0;
}

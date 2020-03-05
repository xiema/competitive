#include<iostream>
using namespace std;

int main(){
	int T;
	long long N,Z;
	cin >> T;
	while (T--){
		cin >> N;
		Z = 0;
		while (N > 0){
			Z += N /= 5;
		}
		cout << Z << '\n';
	}
	
	return 0;
}

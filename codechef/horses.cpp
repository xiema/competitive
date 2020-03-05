#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

long horses[5000];

int main(){
	int T,N;
	long dif;
	cin >> T;
	while (T-- > 0){
		cin >> N;
		for (int i=0; i<N; ++i)
			cin >> horses[i];
		
		sort(horses, horses+N);
		dif = horses[1]-horses[0];
		for (int i=2; i<N; ++i){
			dif = min(dif, horses[i]-horses[i-1]);
		}
		
		cout << dif << '\n';
	}
	
	return 0;
}

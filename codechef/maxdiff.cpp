#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

int main(){
	int T,N,K,sum1,sum2;
	int w[100];
	cin >> T;
	
	while (T-- > 0){
		cin >> N >> K;
		for (int i=0; i<N; ++i)
			cin >> w[i];
			
		sort(w, w+N);
		sum1 = sum2 = 0;
		K = min(K, N-K);
		for (int i=0; i<K; ++i){
			sum1 += w[i];
		}
		for (int i=K; i<N; ++i){
			sum2 += w[i];
		}
		
		cout << max(sum1-sum2, sum2-sum1) << '\n';
	}
	
	return 0;
}

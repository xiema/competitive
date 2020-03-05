#include <bits/stdc++.h>
using namespace std;

int main(){
	int T,N;
	cin >> T;
	
	while (T-- > 0){
		cin >> N;
		vector<pair<int,int>> kd(N);
		for (int i=0; i<N; ++i){
			cin >> kd[i].first >> kd[i].second;
		}
		sort(kd.begin(), kd.end());
		int last = kd[0].second;
		int count = 1;
		for (int i=1; i<N; ++i){
			if (kd[i].first > last){
				++count;
				last = kd[i].second;
			} else {
				if (kd[i].second < last) {
					last = kd[i].second;
				}
			}
		}
		cout << count << '\n';
	}
	
	return 0;
}

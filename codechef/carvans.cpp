#include <iostream>
#include <limits>
using namespace std;

int main(){
	int T, N, speed, min, count;
	cin >> T;
	while (T-- > 0){
		cin >> N;
		count = 0;
		min = numeric_limits<int>::max();
		while (N-- > 0){
			cin >> speed;
			if (speed <= min){
				min = speed;
				++count;
			}
		}
		cout << count << '\n';
	}
	return 0;
}

#include <iostream>
#include <algorithm>
using namespace std;

int notes[20];

bool fit(int end, int amt){
	if (end < 0) return false;
	
	for (int i=end; i>=0; --i){
		int dif = amt - notes[i];
		if (dif == 0){
			return true;
		} else if (dif > 0) {
			if (fit(i-1, dif)){
				return true;
			}
		}
	}
	
	return false;
}

int main(){
	int T, n, m;
	cin >> T;
	while (T-- > 0){
		cin >> n >> m;
		if (n > 0 && n <= 20){
			for (int i=0; i<n; ++i)
				cin >> notes[i];
				
			sort(notes, notes+n);
			if (fit(n-1, m)){
				cout << "Yes\n";
			} else {
				cout << "No\n";
			}
		}
	}
	return 0;
}

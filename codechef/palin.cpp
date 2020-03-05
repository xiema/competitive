#include <bits/stdc++.h>
using namespace std;

void inc(string &s, int place){
	int i = place;
	while (i >= 0) {
		if (s[i] == '9'){
			s[i] = '0';
			--i;
		} else {
			++s[i];
			return;
		}
	}
}

void makepalin(string &s, int left, int right){
	if (s[left] > s[right]){
		s[right] = s[left];
	} else if (s[left] < s[right]) {
		inc(s, right-1);
		s[right] = s[left];
	}
}

int main(){
	int T,left,right;
	string s;
	cin >> T;
	while (T--){
		cin >> s;
		inc(s, s.size()-1);
		if (s[0] == '0'){
			s[0] = '1';
			cout << s + "1\n";
			continue;
		}
		
		left=0, right=s.size()-1;
		while (left < right){
			makepalin(s, left++, right--);
		}
		
		cout << s << '\n';
	}
	return 0;
}

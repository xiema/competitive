#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
	char c, d;
	while(true){
		cin >> c >> d;
		if (c > d) {
			cout << c << endl;
		} else {
			cout << d << endl;
		}
	}
	return 0;
}

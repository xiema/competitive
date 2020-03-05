#include <iostream>
using namespace std;

int main(){
	int A,B;
	cin >> A >> B;
	int dif = A-B;
	if (dif%10 < 9)
		cout << dif+1;
	else
		cout << dif-1;
	
	return 0;
}

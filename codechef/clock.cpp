#include <iostream>
#include <ctime>
using namespace std;

int main(){
	clock_t t = clock();
	int b = true;
	int limit = 1e4;
	for (int i=0; i<limit; ++i){
		for (int j=0; j<limit; ++j){
		}
	}
	cout << (double)(clock() - t) / CLOCKS_PER_SEC << '\n';
	return 0;
}

#include <iostream>
using namespace std;

const unsigned int limit = 1e9;
bool notprime[limit], last=3;

void printprimes(unsigned int start, unsigned int end){
	if (start <= 2) cout << "2\n";
	start = (start/2)*2 + 1;
	if (last < start){
		unsigned int i = last;
		while (i+=2 < start){
			if (!notprime[i]){
				for (unsigned int j=i*2; j<limit; j+=i){
					notprime[j] = true;
				}
			}
		}
		last = start;
	}
	
	for (unsigned int i=start; i<=end; i+=2){
		if (!notprime[i]){
			cout << i << '\n';
			if (last < i) {
				for (unsigned int j=i*2; j<limit; j+=i){
					notprime[j] = true;
				}
				last = i;
			}
		}
	}
}

int main(){
	int t;
	unsigned int m,n;
	cin >> t;
	notprime[0] = true;
	notprime[1] = true;
	while (t-- > 0){
		cout << "test\n";
		cin >> m >> n;
		printprimes(m,n);
	}
	
	return 0;
}

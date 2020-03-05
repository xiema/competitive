#include <bits/stdc++.h>
using namespace std;

void rrfrnds(ofstream &fout, int N, int T){
	fout << N << '\n';
	
	bool friends[N][N];
	for (int i=0; i<N; ++i){
		for (int j=0; j<N; ++j){
			friends[i][j] = false;
		}
	}
	
	srand(time(NULL));
	int a,b;
	while (T){
		a = rand()%N;
		b = rand()%N;
		if (!friends[a][b]){
			friends[a][b]=friends[b][a]=true;
			--T;
		}
	}
	
	for (int i=0; i<N; ++i){
		for (int j=0; j<N; ++j){
			fout << "01"[friends[i][j]];
		}
		fout << '\n';
	}
}

void multq3(ofstream &fout, int N, int Q){
	int a,b;
	srand(time(NULL));
	fout << N << ' ' << Q << '\n';
	for (int i=0; i<Q; ++i){
		a = rand()%N;
		b = rand()%N;
		if (a > b) {
			swap(a,b);
		}
		fout << rand()%2 << ' ' << a << ' ' << b << '\n';
	}
}

int main(){
	ofstream fout("multq3.in");
	multq3(fout, 1000, 1000);
	return 0;
}

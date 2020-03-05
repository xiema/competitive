#include <iostream>
#include <cstdlib>
#include <ctime>
#include <algorithm>
using namespace std;

const int sz = 10;
const int range = 1000;
int arr[sz];

void fillarr(){
	srand(time(NULL));
	for(int i=0; i<sz; ++i){
		arr[i] = rand() % range;
	}
}

void printarr(){
	for(int i=0; i<sz; ++i){
		cout << arr[i] << ' ';
	}
	cout << '\n';
}

int partition(int begin, int end){
	int pivot = arr[end];
	int ins = begin;
	for(int i=begin; i<end; ++i){
		if (arr[i] < pivot){
			swap(arr[ins], arr[i]);
			++ins;
		}
	}
	swap(arr[ins], arr[end]);
	return ins;
}

void quicksort(int begin, int end){
	if (begin < end){
		int pivot = partition(begin, end);
		quicksort(begin, pivot-1);
		quicksort(pivot+1, end);
	}
}



int main(){
	fillarr();
	printarr();
	quicksort(0, sz-1);
	printarr();

	return 0;
}

#include <iostream>
#include <cstdlib>
using namespace std;

int getmin_idx(int* arr, int start, int end){
  int min_idx = start+1;
  int val = arr[min_idx];
  for (int i=min_idx+1; i < end; ++i) {
    if (arr[i] < val) {
      min_idx = i;
      val = arr[i];
    }
  }
  return min_idx;
}

int navigate(int* arr, int start, int end, int limit){
  if (end - start <= limit) {
    return arr[end];
  }
  int min_idx = getmin_idx(arr, start, end);
  return (navigate(arr, start, min_idx, limit) * navigate(arr, min_idx+1, end, limit));
}

int main(){
  int count, limit;
  scanf("%d %d", &count, &limit);
  cout << count << endl;
  cout << limit << endl;
  int arr[count];
  for (int i=0; i<count; ++i){
    scanf("%d", &arr[i]);
  }
  int prod = arr[0] * navigate(arr, 0, count-1, limit);
  printf("%d", prod);
  return 0;
}

#include <iostream>
#include <vector>
#include <string>
using namespace std;

const int MAXIMUM = 1000000;

void gen_primes(vector<int> out){
  vector<bool> isprime(MAXIMUM, true);
  isprime[0] = false;
  isprime[1] = false;
  isprime[4] = false;
  for (int n=5; n<=MAXIMUM; n+=2){
    if (isprime[n]){
      out.push_back(n);
      for (int m=n*2; m<=MAXIMUM; m+=n){
        isprime[m] = false;
      }
    }
  }
}


int main(){
  vector<int> primes = {2, 3};
  gen_primes(primes);



  return 0;
}

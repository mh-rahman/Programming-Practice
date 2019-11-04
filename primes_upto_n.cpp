#include <bits/stdc++.h>

using namespace std;

int main(){
	int max=10000;
	cout<<"Enter the max range for primes to be printed"<<"\n";
	cin>>max;
    vector<int> primes;
    char *sieve;
    sieve = new char[max/8+1];
    // Fill sieve with 1  
    memset(sieve, 0xFF, (max/8+1) * sizeof(char));
    for(int x = 2; x <= max; x++)
        if(sieve[x/8] & (0x01 << (x % 8))){
            primes.push_back(x);
			cout<<x<<"\n";
            // Is prime. Mark multiplicates.
            for(int j = 2*x; j <= max; j += x)
                sieve[j/8] &= ~(0x01 << (j % 8));
        }
    delete[] sieve;
	return 0;
}
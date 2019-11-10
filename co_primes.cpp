#include <bits/stdc++.h> 
using namespace std; 
  
// function to check for gcd 
bool coprime(int a, int b) 
{    
    return (__gcd(a, b) == 1); 
} 
  
// Recursive function to 
// return gcd of a and b 
int numOfPairs(int arr[], int n) 
{  
      
    int count = 0;  
    for (int i = 0; i < n - 1; i++)  
        for (int j = i + 1; j < n; j++) 
            if (coprime(arr[i], arr[j])) 
                count++; 
                  
    return count; 
} 
  
// driver code 
int main() 
{ 
    int arr[] = { 1, 2, 5, 4, 8, 3, 9 }; 
    int n = sizeof(arr) / sizeof(arr[0]);  
    cout << numOfPairs(arr, n); 
    return 0; 
} 

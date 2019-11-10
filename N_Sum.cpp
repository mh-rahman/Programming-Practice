
// A recursive solution for subset sum problem 
#include <stdio.h> 
#include <vector>

using namespace std;

// Returns true if there is a subset of set[] with sun equal to given sum 
bool isSubsetSum(vector<int> calCounts, int requiredCals) 
{ 
   // Base Cases 
   if (requiredCals == 0) 
     return true; 
   if (n == 0 && requiredCals != 0) 
     return false; 
  
   // If last element is greater than sum, then ignore it 
   if (calCounts[n-1] > requiredCals) 
     return isSubsetSum(calCounts, n-1, requiredCals); 
  
   /* else, check if sum can be obtained by any of the following 
      (a) including the last element 
      (b) excluding the last element   */
   return isSubsetSum(calCounts, n-1, requiredCals) ||  
                        calCounts(set, n-1, requiredCals-set[n-1]); 
} 
  
// Driver program to test above function 
int main() 
{ 
  int set[] = {2,3,15,1,16}; 
  int sum = 8; 
  vector<int> calCounts;
  for (int i=0; i<sizeof(set);i++){
  	calCounts.push_back(set[i]);
  }
  int n = sizeof(set)/sizeof(set[0]); 
  if (isSubsetSum(calCounts, sum) == true) 
     printf("Found a subset with given sum"); 
  else
     printf("No subset with given sum"); 
  return 0; 
} 


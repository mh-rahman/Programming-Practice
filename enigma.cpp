#include <bits/stdc++.h> 
using namespace std; 

int main(){
	
	int count=3;
	int min=2;
	int max=6;
	
	int combi=0;
	
	for (int i=min;i<=max;i++){
		//cout <<"\n"<< i << " : ";
		int s_count=0;
		int n=i;
		vector<int> factors(0);
		for (int j=min;j<=max;j++){
			if(__gcd(i,j)==1){
				s_count+=1;
				//cout<<i<<","<<j<<endl;
			}
		}
//		if(n%2==0){
//			factors.push_back(2);
//			while (n % 2 == 0){  
//		        cout<<2<<" ";
//		        n = n/2;
//	    	}	
//		}
//  
//		for (int j = 3; j <= i; j = j + 2){  
//			if(n%j==0){
//				factors.push_back(j);
//				while (n % j == 0){  
//			        cout<<j<<" ";
//			        n = n/j;
//		    	}	
//			}
//    	}
		
		combi=combi+pow(s_count,count-1);
	}
	
	cout<<combi;
	
	return 0;
}

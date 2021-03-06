#include <bits/stdc++.h> 
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<iomanip>
using namespace std; 
 
 
int maximumTotalWeight(vector<int> weights, vector<int> tasks, int p) {

    int n=weights.size();
    vector<vector<int>> opt(n+1,vector<int>(p+1));

    for (int i=0;i<tasks.size();i++){
        tasks[i]*=2;
    }
    
    for (int i=0;i<n+1;i++){
        for(int j=0;j<p+1;j++){
            if (i==0 or j==0){
                opt[i][j]=0;
            }
            else if (j>=tasks[i-1]){
                opt[i][j]=max(opt[i-1][j],weights[i-1]+opt[i-1][j-tasks[i-1]]);
            }
            else{
                opt[i][j]=opt[i-1][j];
            }
        }
    }
    return opt[n][p];
}

int main() 
{ 
    
    int n=4;
    int runtime=15;
    int m=runtime;
    vector<int> length;
    length.push_back(4);
    length.push_back(4);
    length.push_back(6);
    length.push_back(8);
	
    vector<int> weight;
    weight.push_back(2);
    weight.push_back(4);
    weight.push_back(4);
    weight.push_back(5);
    
    for(int i=0;i<n;i++){
    	length[i]*=2;
	}
    
    int x;
    
	cout<<"Enter the number of integers in the dataset"<<"\n";
    cin>>x;
    cout<<"Enter "<<n<<" integers to be sorted"<<"\n";
    

    vector<vector<int> > opt( n+1 , vector<int> (m+1, 0));
	    for (int i=0;i<5;i++){
    	for (int j=0; j<16;j++){
    		cout<<opt[i][j]<<'\t';
		}
		cout<<endl;
	}
	
	cout<<"Solution:"<<endl;
    	    
    for(int i=1;i<=4;i++){
    	for (int j=1;j<=m;j++){
    		if(j>=length[i-1]){
    			opt[i][j]=max(opt[i-1][j],weight[i-1]+opt[i-1][j-length[i-1]]);
			}
			else{
				opt[i][j]=opt[i-1][j];
			}
		}
	}
    
    for (int i=0;i<5;i++){
    	for (int j=0; j<16;j++){
    		cout<<opt[i][j]<<'\t';
		}
		cout<<endl;
	}
    
    return 0;
}


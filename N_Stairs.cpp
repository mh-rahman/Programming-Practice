#include <bits/stdc++.h>

using namespace std;

int getOpt(int N, vector<int> x,int size) {

	int optValue=0;

	if(N==0||N==x[0]){
		return 1;
	}
	else if (N<x[0]){
		return 0;
	}
	else{
		for (int i=0;i<size;i++){
			optValue+=getOpt(N-x[i],x,size);
		}
	}

	return optValue;
}

int main(){

	int numberOfStairs;
	cout<<"Enter the number of stairs:\n";
	cin>>numberOfStairs;
	int numberOfSteps;
	cout<<"Enter the number of possible steps:\n";
	cin>>numberOfSteps;
	vector<int> steps;
	int temp,minStep=INT_MAX;
	cout<<"Enter the "<<numberOfSteps<<" steps in ascending order:\n";
	for (int i=0;i<numberOfSteps;i++){
		cin>>temp;
		steps.push_back(temp);
		if(temp<minStep){
			minStep=temp;
		}
	}

	//cout<<"Recursion:"<<getOpt(numberOfStairs,steps,numberOfSteps)<<"\n";

	vector <double> optArray;
	for (int i=0; i<=numberOfStairs; i++){
		optArray.push_back(0);
		if (i==0||i==minStep){
			optArray[i]=1;
		}
		else if (i>minStep){
			for (int j=0;j<numberOfSteps;j++){
				if(steps[j]>i){
					break;
				}
				optArray[i]+=optArray[i-steps[j]];
			}
		}
		cout<<optArray[i]<<"\t";
	}

	cout<<"\nBottom Up:"<<optArray[numberOfStairs]<<endl;
	
	if(optArray[numberOfStairs]!=0){
		cout<<"False";
	}
	else{
		cout<<"True";
	}
	
	return 0;
}

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<iomanip>
using namespace std;

vector<int> mSort(vector<int> a){

    //Base Cases
    if(a.size()==1){
        return a;
    }
    else if(a.size()==2){
        if(a[0]<=a[1]){
            return a;
        }
        else{
            int temp;
            temp=a[0];
            a[0]=a[1];
            a[1]=temp;
            return a;
        }
    }
    //Merging
    vector<int> a1,a2,m;
    int i;
    for(i=0;i<a.size()/2;i++){
        a1.push_back(a[i]);
    }
    for(;i<a.size();i++){
        a2.push_back(a[i]);
    }
    a1=mSort(a1);
    a2=mSort(a2);
    
    int j;
    i=0;j=0;

    while(i<a1.size()&&j<a2.size()){
        if(a1[i]<a2[j]){
            a[i+j]=a1[i];
            i++;
        }
        else{
            a[i+j]=a2[j];
            j++;
        }
    }

    while(i<a1.size()){
        a[i+j]=a1[i];
        i++;
    }
    while(j<a2.size()){
        a[i+j]=a2[j];
        j++;
    }

    return a;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int n,i=0,count=0,x,mode;
    float mean,median;
    vector<int> a;
    cout<<"Enter the number of integers in the dataset"<<"\n";
    cin>>n;
    cout<<"Enter "<<n<<" integers to be sorted"<<"\n";
    for(i=0;i<n;i++){
        cout<<"Enter Number"<<"\n";
        cin>>x;
        a.push_back(x);
        count+=a[i];
    }

    a=mSort(a);
    cout<<"Printing Sorted Array";
    for(i=0;i<n;i++){
        cout<<a[i]<<"\t";
    }
    
    return 0;
}


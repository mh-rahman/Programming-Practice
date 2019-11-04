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
    cin>>n;
    //cin>>s;
    //cout<<"Enter "<<n<<" numbers to be sorted"<<"\n";
    for(i=0;i<n;i++){
        //cout<<"Enter Number"<<"\n";
        cin>>x;
        a.push_back(x);
        count+=a[i];
    }

    a=mSort(a);
    //cout<<"Printing Sorted Array";
    /*for(i=0;i<n;i++){
        cout<<a[i]<<"\t";
    }*/
    mean=(float)count/(float)n;
    if(n%2==0){
        median=(float)(a[n/2]+a[n/2-1])/2.0;
    }

    //finding mode
    int cFreq=0, hFreq=0, c;
    c=a[0];
    for(i=0;i<n;i++){
        if(c==a[i]){
            cFreq++;
        }
        else{
            c=a[i];
            cFreq=1;
        }
        if(cFreq>hFreq){
            hFreq=cFreq;
            mode=c;
        }
    }

    //setprecision specifies the minimum precision. fixed says that there will be a fixed number of decimal digits.
    cout<<fixed<<setprecision(1)<<mean<<"\n"<<median<<"\n"<<mode;
    
    
    return 0;
}

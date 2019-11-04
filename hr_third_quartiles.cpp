#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
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

int fMedian(vector<int> a){
    
    int n,median;
    n=a.size();
    if(n%2==0){
        median=(a[n/2]+a[n/2-1])/2;
    }
    else{
        median=a[n/2];
    }

    return median;
}

int main() {

    int n,i=0,count=0,x,mode,q1,q2,q3;
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
    //q2=fMedian(a);

    ////Second Quartile or Median
    if(n%2==0){
        q2=(a[n/2]+a[n/2-1])/2;
    }
    else{
        q2=a[n/2];
    }

    int start1=0, end1, start2, end2;
    end1=n/2-1;
    end2=n-1;
    if(n%2==0){
        start2=n/2;
    }
    else{
        start2=n/2+1;
    }

    //First Quartile
    n=end1-start1+1;
    if(n%2==0){
        q1=(a[n/2]+a[n/2-1])/2;
    }
    else{
        q1=a[n/2];
    }
    cout<<q1<<"\n";
    cout<<q2<<"\n";

    //Third Quartile
    n=end2-start2+1;
    if(n%2==0){
        q3=(a[start2+n/2]+a[start2+n/2-1])/2;
    }
    else{
        q3=a[start2+n/2];
    }
    cout<<q3<<"\n";


    return 0;
}

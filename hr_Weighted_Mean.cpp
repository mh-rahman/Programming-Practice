#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <iomanip>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  

    int n,i=0,count=0,sum=0,x;
    float mean;
    vector<int> numbers,weights;
    cin>>n;
    //cin>>s;
    //cout<<"Enter "<<n<<" numbers to be sorted"<<"\n";
    for(i=0;i<n;i++){
        //cout<<"Enter Number"<<"\n";
        cin>>x;
        numbers.push_back(x);
    }
    for(i=0;i<n;i++){
        //cout<<"Enter Number"<<"\n";
        cin>>x;
        weights.push_back(x);
        sum+=weights[i]*numbers[i];
        count+=weights[i];
    }

    mean=(float)sum/(float)count;

    cout<<fixed<<setprecision(1)<<mean;

    return 0;
}

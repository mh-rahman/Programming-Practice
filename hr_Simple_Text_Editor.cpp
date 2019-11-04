#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <stack>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   

    int nQueries;
    string S;
    stack<string> ss;
    //ss.push(S);
    cin>>nQueries;
    //cout<<"current S is"<<S<<"\n";
    while (nQueries--){
        int n;
        int k;
        string s1;
        cin>>n;
        if (n==1){
            cin>>s1;
            if(S.size()==0 || ss.empty()){
                S=s1;
                //cout<<"current S is"<<S[0]<<"\n";
            }
            else{
                S=S+s1;
                //cout<<"current S is"<<S<<"\n";
            }
            ss.push(S);
        }
        else if (n==2){
            cin>>k;
            while(k){
                S.pop_back();
                k--;
            }
            ss.push(S);
        }
        else if(n==3){
            cin>>k;
            cout<<S[k-1]<<"\n";
        }
        else{
            ss.pop();
            if(!ss.empty()){
                S=ss.top();
            }
            
        }
    }


    return 0;
}

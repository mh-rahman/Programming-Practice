#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

vector<int> waiter(vector<int> number, int q) {

    int max=10000;
    vector<int> primes;
    char *sieve;
    sieve = new char[max/8+1];
    // Fill sieve with 1  
    memset(sieve, 0xFF, (max/8+1) * sizeof(char));
    for(int x = 2; x <= max; x++)
        if(sieve[x/8] & (0x01 << (x % 8))){
            primes.push_back(x);
            // Is prime. Mark multiplicates.
            for(int j = 2*x; j <= max; j += x)
                sieve[j/8] &= ~(0x01 << (j % 8));
        }
    delete[] sieve;

    /*
    int i=0,j=0,k;
    vector<int> temp;
    vector<int> result;
    vector<int> prime;

    while(i<q){
        cout<<"current prime = "<<primes[i]<<"\n";
        for(j=number.size()-1;j>-1;j--){
            if(number[j]%primes[i]==0){
                cout<<"Pushing to prime "<<number[j]<<"\n";
                prime.push_back(number[j]);
            }
            else{
                cout<<"Pushing to temp "<<number[j]<<"\n";
                temp.push_back(number[j]);
            }
        }
        number=temp;
        temp={};
        for(k=prime.size()-1;k>-1;k--){
            result.push_back(prime[k]);
        }
        prime={};
        i++;
    }
    cout<<"All iterations completed \n";
    for(i=number.size()-1;i>-1;i--){
        cout<<"Pushing to result "<<number[i]<<"\n";
        result.push_back(number[i]);
    }
    return result;
    */

    int i=0,r=0;
    stack <int> a1,a2,b,temp;
    //vector<int> result;

    for (i=0;i<number.size();i++){
        a1.push(number[i]);
        cout<<"pushing "<<a1.top()<<" to top of stack a1 \n";
    }

    i=0;

    while(i<q){

        cout<<"Entering first while loop \n";

        while(!a1.empty()){
            if(a1.top()%primes[i]==0){
                b.push(a1.top());
                a1.pop();
            }
            else{
                a2.push(a1.top());
                a1.pop();
            }
        }

        while(!b.empty()){
            cout<<"pushing "<<b.top()<<" to result at position "<<r<<"\n";
            number[r]=b.top();
            b.pop();
            r++;
        }

        temp=a1;
        a1=a2;
        a2=temp;
        i++;

    }

    while(!a1.empty()){
        number[r]=a1.top();
        a1.pop();
        r++;
    }

    return number;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string nq_temp;
    getline(cin, nq_temp);

    vector<string> nq = split_string(nq_temp);

    int n = stoi(nq[0]);

    int q = stoi(nq[1]);

    string number_temp_temp;
    getline(cin, number_temp_temp);

    vector<string> number_temp = split_string(number_temp_temp);

    vector<int> number(n);

    for (int number_itr = 0; number_itr < n; number_itr++) {
        int number_item = stoi(number_temp[number_itr]);

        number[number_itr] = number_item;
    }

    vector<int> result = waiter(number, q);

    for (int result_itr = 0; result_itr < result.size(); result_itr++) {
        fout << result[result_itr];

        if (result_itr != result.size() - 1) {
            fout << "\n";
        }
    }

    fout << "\n";

    fout.close();

    return 0;
}

vector<string> split_string(string input_string) {
    string::iterator new_end = unique(input_string.begin(), input_string.end(), [] (const char &x, const char &y) {
        return x == y and x == ' ';
    });

    input_string.erase(new_end, input_string.end());

    while (input_string[input_string.length() - 1] == ' ') {
        input_string.pop_back();
    }

    vector<string> splits;
    char delimiter = ' ';

    size_t i = 0;
    size_t pos = input_string.find(delimiter);

    while (pos != string::npos) {
        splits.push_back(input_string.substr(i, pos - i));

        i = pos + 1;
        pos = input_string.find(delimiter, i);
    }

    splits.push_back(input_string.substr(i, min(pos, input_string.length()) - i + 1));

    return splits;
}

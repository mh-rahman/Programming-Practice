#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);


struct minHeap{
    int capacity;
    int heapSize=-1;
    int *harr;

    minHeap(int x){
        capacity=x;
        heapSize=0;
        harr=new int[x];
    }

    //Functions

    int parent (int x){
        return (x-1)/2;
    }

    int left(int x){
        return 2*x+1;
    }

    int right (int x){
        return 2*x+2;
    }

    //void swap (int )

    void insert(int x){
        if(heapSize==capacity){
            //cout<<"OVerflow";
        }
        else{
            int i=heapSize,temp;
            harr[i]=x;
            heapSize++;

            while(i!=0 && harr[parent(i)]>harr[i]){
                temp=harr[parent(i)];
                harr[parent(i)]=harr[i];
                harr[i]=temp;
                i=parent(i);
            }
        }
    }

    int top(){
        if(heapSize<=0){
            //cout<<"Heap is empty.\n";
            return -1;
        }
        return harr[0];
    }

    int extractMin(){
        if(heapSize<=0){
            //cout<<"Heap is empty.\n";
            return -1;
        }
        int min=top();
        heapSize--;
        harr[0]=harr[heapSize];
        heapify(0);

        return min;
    }

    void heapify(int i){
        int small=i;
        if(left(i)<heapSize && harr[left(i)]<harr[small]){
            small=left(i);
        }
        if(right(i)<heapSize && harr[right(i)]<harr[small]){
            small=right(i);
        }
        if(small!=i){
            int temp;
            temp=harr[i];
            harr[i]=harr[small];
            harr[small]=temp;
            heapify(small);
        }
    }

};


int cookies(int k, vector<int> A) {

    minHeap h(A.size());
    //h.insert(10);
    //cout<<"Inserting 10 to Heap. Top of heap is "<<h.top()<<"\n";
    for (int i=0;i<A.size();i++){
        h.insert(A[i]);
        //cout<<"Inserting "<<A[i]<<" to Heap. Top of heap is "<<h.top()<<"\n";
    }

    /*cout<<"\n Printing Heap contents\n";
    for (int i=0;i<A.size();i++){
        cout<<h.extractMin()<<"\t";
    }*/

    int cookie1, cookie2,steps=0;

    while(h.top()<k){
        cookie1=h.extractMin();
        cookie2=h.extractMin();

        if(cookie1==-1 || cookie2==-1){
            return -1;
        }

        h.insert(cookie1+2*cookie2);
        steps++;
    }
    
    return steps;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string nk_temp;
    getline(cin, nk_temp);

    vector<string> nk = split_string(nk_temp);

    int n = stoi(nk[0]);

    int k = stoi(nk[1]);

    string A_temp_temp;
    getline(cin, A_temp_temp);

    vector<string> A_temp = split_string(A_temp_temp);

    vector<int> A(n);

    for (int A_itr = 0; A_itr < n; A_itr++) {
        int A_item = stoi(A_temp[A_itr]);

        A[A_itr] = A_item;
    }

    int result = cookies(k, A);

    fout << result << "\n";

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

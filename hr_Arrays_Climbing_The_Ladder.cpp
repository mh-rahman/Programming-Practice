#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

/**
int getRank (int aScore, vector<int> unique, int start, int end){

    int rank,mid;
    if (start==end){
        if (aScore>=unique[start]){
            rank=start+1;
        }
        else{
            rank=start+2;
        }
        return rank;
    }
    else if(end==(start+1)){
        if (aScore>=unique[start]){
            rank=start+1;
        }
        else if (aScore>=unique[end]){
            rank = end+1;
        }
        else
            rank=end+2;
        return rank;
    }
    mid = (start+end)/2;
        if (aScore==unique[mid]){
            rank=mid+1;
        }
        else if (aScore<unique[mid]) {
            rank=getRank(aScore,unique,mid+1,end);
        }
        else if (aScore>unique[mid]) {
            rank=getRank(aScore,unique,start,mid-1);
        }
    return rank;
}
**/

// Complete the climbingLeaderboard function below.
vector<int> climbingLeaderboard(vector<int> scores, vector<int> alice) {

    vector<int> unique, rank(alice.size());
    unsigned int i,j=0;
    unique.push_back(scores[0]);

    for (i=0;i<scores.size();i++){
        if (unique[j]!=scores[i]){
            j++;
            unique.push_back(scores[i]);
        }
    }

    //int x=0;
    j=0;

    for (i=rank.size();i>0;i--){
        for (;j<unique.size()&&unique[j]>alice[i-1];){
            j++;
        }
        //x=j;
        rank[i-1]=j+1;
    }
    

    /**
    Optimized - trying merge sort approach - reducing time to O(logn)

    j=unique.size()-1;

    for (i=0;i<alice.size();i++){
        if (alice[i]==unique[j/2]){
            rank[i]=(j/2)+1;
        }
        else if (alice[i]<unique[j/2]) {
            rank[i]=getRank(alice[i],unique,(j/2)+1,j);
        }
        else if (alice[i]>unique[j]) {
            rank[i]=getRank(alice[i],unique,0,j/2-1);
        }
    }
    **/
    

    return rank;

}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int scores_count;
    cin >> scores_count;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string scores_temp_temp;
    getline(cin, scores_temp_temp);

    vector<string> scores_temp = split_string(scores_temp_temp);

    vector<int> scores(scores_count);

    for (int i = 0; i < scores_count; i++) {
        int scores_item = stoi(scores_temp[i]);

        scores[i] = scores_item;
    }

    int alice_count;
    cin >> alice_count;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string alice_temp_temp;
    getline(cin, alice_temp_temp);

    vector<string> alice_temp = split_string(alice_temp_temp);

    vector<int> alice(alice_count);

    for (int i = 0; i < alice_count; i++) {
        int alice_item = stoi(alice_temp[i]);

        alice[i] = alice_item;
    }

    vector<int> result = climbingLeaderboard(scores, alice);

    for (int i = 0; i < result.size(); i++) {
        fout << result[i];

        if (i != result.size() - 1) {
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

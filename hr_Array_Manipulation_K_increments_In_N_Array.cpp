/**
Starting (Create) with a 1-indexed array of zeros and a list of operations, for each operation add a value to each of the array element between two given indices, inclusive.
Once all operations have been performed, return the maximum value in your array. 
Example:
Input:
    1 5 3
    4 8 7
    6 9 1
Output:
	10
Explanation:
Starting		[0,0,0, 0, 0,0,0,0,0, 0]
1st operation	[3,3,3, 3, 3,0,0,0,0, 0]
2nd operation	[3,3,3,10,10,7,7,7,0, 0]
3rd operation	[3,3,3,10,10,8,8,8,1, 0]

**/


#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

// Complete the arrayManipulation function below.
long arrayManipulation(int n, vector<vector<int>> queries) {

    unsigned long int max=0,i,j,sum=0;

    vector<unsigned long int> myArray(n);
    
    /** in-efficient approach (Brute force)
    for (i=0;i<queries.size();i++){
        for (j=queries[i][0]-1;j<queries[i][1];j++){
            myArray[j]+=queries[i][2];
            if (myArray[j]>max){
                max=myArray[j];
            }
        }
    }
    **/

    //Efficient approach - by marking the extremeties of ranges for each query and then keeping track of slope to find the maximum value

    for (i=0;i<queries.size();i++){
        myArray[queries[i][0]-1]+=queries[i][2];
        if (queries[i][1]<n){
            myArray[queries[i][1]]-=queries[i][2];
        }
    }

    for (i=0;i<n;i++){
        sum+=myArray[i];
        if (sum>max){
            max=sum;
        }
    }


    return max;

}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string nm_temp;
    getline(cin, nm_temp);

    vector<string> nm = split_string(nm_temp);

    int n = stoi(nm[0]);

    int m = stoi(nm[1]);

    vector<vector<int>> queries(m);
    for (int i = 0; i < m; i++) {
        queries[i].resize(3);

        for (int j = 0; j < 3; j++) {
            cin >> queries[i][j];
        }

        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }

    long result = arrayManipulation(n, queries);

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

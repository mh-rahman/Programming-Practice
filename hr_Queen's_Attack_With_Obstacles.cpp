
#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);



// Complete the queensAttack function below.
int queensAttack(int n, int k, int r_q, int c_q, vector<vector<int>> obstacles) {

    vector<vector <int>> ro(4);
    int i,attackSquares=0;

    //resize the ro matrix
    for (i=0;i<4;i++){
        ro[i].resize(2);
    }

    for (i=0;i<obstacles.size();i++){
        if (obstacles[i][0]==r_q){
            //if rows match, we store the columns values of obstacles
            if (obstacles[i][1]<c_q){
                if(ro[0][0]==0){
                    ro[0][0]=obstacles[i][1];
                }
                else if (obstacles[i][1]>ro[0][0]){
                    ro[0][0]=obstacles[i][1];
                }
            }
            else if (obstacles[i][1]>c_q){
                if(ro[0][1]==0){
                    ro[0][1]=obstacles[i][1];
                }
                else if (obstacles[i][1]<ro[0][1]){
                    ro[0][1]=obstacles[i][1];
                }
            }

        }
        else if (obstacles[i][1]==c_q){
            //if columns match, we store the row values of obstacles
            if (obstacles[i][0]<r_q){
                if(ro[1][0]==0){
                    ro[1][0]=obstacles[i][0];
                }
                else if (obstacles[i][0]>ro[1][0]){
                    ro[1][0]=obstacles[i][0];
                }
            }
            else if (obstacles[i][0]>r_q){
                if(ro[1][1]==0){
                    ro[1][1]=obstacles[i][0];
                }
                else if (obstacles[i][0]<ro[1][1]){
                    ro[1][1]=obstacles[i][0];
                }
            }
        }
        else if ((obstacles[i][0]-r_q)==(obstacles[i][1]-c_q)){
          //if obstacles lie on diagonals, we store the row values of obstacles
            if (obstacles[i][0]<r_q){
                if(ro[2][0]==0){
                    ro[2][0]=obstacles[i][0];
                }
                else if (obstacles[i][0]>ro[2][0]){
                    ro[2][0]=obstacles[i][0];
                }
            }
            else if (obstacles[i][0]>r_q){
                if(ro[2][1]==0){
                    ro[2][1]=obstacles[i][0];
                }
                else if (obstacles[i][0]<ro[2][1]){
                    ro[2][1]=obstacles[i][0];
                }
            }  
        }
        else if ((obstacles[i][0]+obstacles[i][1])==(r_q+c_q)){
            //if obstacles lie on diagonals, we store the row values of obstacles
            if (obstacles[i][0]<r_q){
                if(ro[3][0]==0){
                    ro[3][0]=obstacles[i][0];
                }
                else if (obstacles[i][0]>ro[3][0]){
                    ro[3][0]=obstacles[i][0];
                }
            }
            else if (obstacles[i][0]>r_q){
                if(ro[3][1]==0){
                    ro[3][1]=obstacles[i][0];
                }
                else if (obstacles[i][0]<ro[3][1]){
                    ro[3][1]=obstacles[i][0];
                }
            }  
        }
    }

    //calculating row-wise attack squares
    if(ro[0][0]==0){
        attackSquares+=(c_q-1);
    }
    else if(ro[0][0]!=0){
         attackSquares+=(c_q-ro[0][0]-1);
    }
    if(ro[0][1]==0){
        attackSquares+=(n-c_q);
    }
    else if(ro[0][1]!=0){
         attackSquares+=(ro[0][1]-c_q-1);
    }

    //calculating column-wise attack squares
    if(ro[1][0]==0){
        attackSquares+=(r_q-1);
    }
    else if(ro[1][0]!=0){
         attackSquares+=(r_q-ro[1][0]-1);
    }
    if(ro[1][1]==0){
        attackSquares+=(n-r_q);
    }
    else if(ro[1][1]!=0){
         attackSquares+=(ro[1][1]-r_q-1);
    }

    //calculating diagonal-1 attack squares
    if(ro[2][0]==0){
        attackSquares+=min(c_q-1,r_q-1);
    }
    else if(ro[2][0]!=0){
         attackSquares+=(r_q-ro[2][0]-1);
    }
    if(ro[2][1]==0){
        attackSquares+=min(n-r_q,n-c_q);
    }
    else if(ro[2][1]!=0){
         attackSquares+=(ro[2][1]-r_q-1);
    }

    //calculating diagonal-2 attack squares
    if(ro[3][0]==0){
        attackSquares=attackSquares+min(r_q-1,n-c_q);
    }
    else if(ro[3][0]!=0){
         attackSquares+=(r_q-ro[3][0]-1);
    }
    if(ro[3][1]==0){
        attackSquares=attackSquares+min(n-r_q,c_q-1);
    }
    else if(ro[3][1]!=0){
         attackSquares+=(ro[3][1]-r_q-1);
    }


    return attackSquares;

}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string nk_temp;
    getline(cin, nk_temp);

    vector<string> nk = split_string(nk_temp);

    int n = stoi(nk[0]);

    int k = stoi(nk[1]);

    string r_qC_q_temp;
    getline(cin, r_qC_q_temp);

    vector<string> r_qC_q = split_string(r_qC_q_temp);

    int r_q = stoi(r_qC_q[0]);

    int c_q = stoi(r_qC_q[1]);

    vector<vector<int>> obstacles(k);
    for (int i = 0; i < k; i++) {
        obstacles[i].resize(2);

        for (int j = 0; j < 2; j++) {
            cin >> obstacles[i][j];
        }

        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }

    int result = queensAttack(n, k, r_q, c_q, obstacles);

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

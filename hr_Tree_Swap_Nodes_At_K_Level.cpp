#include <bits/stdc++.h>

using namespace std;

struct node {
    int data;
    node *left;
    node *right;
    int depth;

    node (int i){
        this->data=i;
        this->left=NULL;
        this->right=NULL;
    }

};

queue<node*> inorder (node *root, int k,queue<node*> q){

    node *temp;
    if(root->depth%k==0){
        temp=root->left;
        root->left=root->right;
        root->right=temp;
    }

    if(root->left!=NULL){
        q=inorder(root->left, k,q);
    }

    q.push(root);
    cout<<"Pushed to Queue"<<q.back()->data<<"\n";

    if(root->right!=NULL){
        q=inorder(root->right,k,q);
    }

    return q;

}

vector<vector<int>> swapNodes(vector<vector<int>> indexes, vector<int> queries) {
    node *root = new node(1);
    root->depth=1;
    node *current = root;

    queue<node*> q;
    q.push(root);
    int i,n=1,height=1,j;
    while(!q.empty()){
        current=q.front();
        if(current->depth>height){
            height=current->depth;
        }
        if(i<indexes.size()&&indexes[i][0]!=-1){
            node *temp=new node(indexes[i][0]);
            q.push(temp);
            current->left=temp;
            temp->depth=current->depth+1;
            n++;
        }
        if(i<indexes.size()&&indexes[i][1]!=-1){
            node *temp=new node(indexes[i][1]);
            q.push(temp);
            current->right=temp;
            temp->depth=current->depth+1;
            n++;
        }
        i++;
        q.pop();
    }
    cout<<"height="<<height<<"\n";
    cout<<n<<"\n";//number of nodes

     

    
    vector<vector<int>> result(queries.size(), vector<int>(indexes.size()));
    //vector<vector<int>> result[1][queries.size()];

    for(i=0;i<queries.size();i++){
        cout<<queries[i]<<"\n";
        q=inorder(root,queries[i],q);

        for (j=0;!q.empty()&&j<n;j++){        
            result[i][j]=q.front()->data;    
            q.pop();
        }

    }

    return result;
    

    

}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    vector<vector<int>> indexes(n);
    for (int indexes_row_itr = 0; indexes_row_itr < n; indexes_row_itr++) {
        indexes[indexes_row_itr].resize(2);

        for (int indexes_column_itr = 0; indexes_column_itr < 2; indexes_column_itr++) {
            cin >> indexes[indexes_row_itr][indexes_column_itr];
        }

        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }

    int queries_count;
    cin >> queries_count;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    vector<int> queries(queries_count);

    for (int queries_itr = 0; queries_itr < queries_count; queries_itr++) {
        int queries_item;
        cin >> queries_item;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        queries[queries_itr] = queries_item;
    }

    vector<vector<int>> result = swapNodes(indexes, queries);

    for (int result_row_itr = 0; result_row_itr < result.size(); result_row_itr++) {
        for (int result_column_itr = 0; result_column_itr < result[result_row_itr].size(); result_column_itr++) {
            fout << result[result_row_itr][result_column_itr];

            if (result_column_itr != result[result_row_itr].size() - 1) {
                fout << " ";
            }
        }

        if (result_row_itr != result.size() - 1) {
            fout << "\n";
        }
    }

    fout << "\n";

    fout.close();

    return 0;
}

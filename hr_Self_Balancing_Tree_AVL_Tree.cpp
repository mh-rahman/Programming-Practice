/* Node is defined as :
typedef struct node
{
    int val;
    struct node* left;
    struct node* right;
    int ht;
} node; */

bool isBalanced(node *root){
    int l,r;
    if (root==NULL){
        return 1;
    }
    if(root->left==NULL){
        l=-1;
    }
    else{
        l=root->left->ht;
    }
    if(root->right==NULL){
        r=-1;
    }
    else{
        r=root->right->ht;
    }
    l=l-r;
    if(l<2&&l>-2){
        return 1;
    }
    else{
        return 0;
    }
}

int setHeight (node *root){
    int l,r;
    if (root==NULL){
        return -1;
    }
    if(root->left==NULL&&root->right==NULL){
        return 0;
    }
    if(root->left==NULL){
        l=-1;
    }
    else{
        l=root->left->ht;
    }
    if(root->right==NULL){
        r=-1;
    }
    else{
        r=root->right->ht;
    }
    return max(l,r)+1;
}

int balanceFactor(node *root){
    int l,r;
    if (root==NULL){
        return 0;
    }
    if(root->left==NULL){
        l=-1;
    }
    else{
        l=root->left->ht;
    }
    if(root->right==NULL){
        r=-1;
    }
    else{
        r=root->right->ht;
    }
    return l-r;
}

node * balance (node *root){
    node *temp = new node();
    if(balanceFactor(root)>1){
        if(balanceFactor(root->left)==1){
            //left left case
            temp=root;
            root=root->left;
            temp->left=root->right;
            root->right=temp;
            temp->ht=temp->ht-2;
            return root;
        }
        else{
            //left right case
            temp=root->left;
            root->left=temp->right;
            temp->right=root->left->left;
            root->left->left=temp;
            temp->ht--;
            root->left->ht++;
            root=balance(root);
            return root;
        }
    }
    else{
        if(balanceFactor(root->right)==-1){
            //right right case
            temp=root;
            root=root->right;
            temp->right=root->left;
            root->left=temp;
            temp->ht=temp->ht-2;
            return root;
        }
        else{
            //right left case
            temp=root->right;
            root->right=temp->left;
            temp->left=root->right->right;
            root->right->right=temp;
            temp->ht--;
            root->right->ht++;
            root=balance(root);
            return root;
        }
    }
}

node * insert(node * root,int val)
{
    //cout<<"code reached here "<<"node="<<root->val<<"\n";
    if(val<root->val){
        //insert in left subtree
        if(root->left==NULL){
            //cout<<"code reached here "<<"node="<<root->val<<"\n";
            node *temp = new node();
            temp->val=val;
            temp->left=NULL;
            temp->right=NULL;
            temp->ht=0;
            root->left=temp;
        }
        else{
            //cout<<"code reached here "<<"node="<<root->val<<"\n";
            root->left=insert(root->left,val);
        }
    }
    else{
        //insert in right subtree
        if(root->right==NULL){
            node *temp = new node();
            temp->val=val;
            temp->left=NULL;
            temp->right=NULL;
            temp->ht=0;
            root->right=temp;
            //cout<<"code reached here "<<"node="<<root->val<<"\n";
            //cout<<"inserted new node "<<root->right->val<<"\n";
        }
        else{
            //cout<<"code reached here "<<"node="<<root->val<<"\n";
            root->right=insert(root->right,val);

        }
    }
    
    //cout<<"previous height of node "<<root->val<<"="<<root->ht<<"\n";
    root->ht=setHeight(root);
    /*if(!isBalanced(root->left)){
        cout<<"Left subtree of "<<root->val<<" is not balanced"<<"\n";
        root->left=balance(root->left);
    }
    if(!isBalanced(root->right)){
        cout<<"Right subtree of "<<root->val<<" is not balanced"<<"\n";
        root->right=balance(root->right);
    }*/
    if(!isBalanced(root)){
        //cout<<"Node "<<root->val<<" is not balanced"<<"\n";
        root=balance(root);
    }
    root->ht=setHeight(root);
    //cout<<"New height of node "<<root->val<<"="<<root->ht<<"\n";
    
    return root;

  
}
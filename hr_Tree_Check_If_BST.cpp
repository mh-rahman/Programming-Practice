/* Hidden stub code will pass a root argument to the function below. Complete the function to solve the challenge. Hint: you may want to write one or more helper functions.  

The Node struct is defined as follows:
	struct Node {
		int data;
		Node* left;
		Node* right;
	}
*/  
    
    int getMin(Node* root){
        
        if(root->left==nullptr){
            return root->data;
        }
        else{
            while(root->left!=nullptr){
                root=root->left;
            }
            return root->data;
        }
        
    }
    int getMax(Node* root){
        
        if(root->right==nullptr){
            return root->data;
        }
        else{
            while(root->right!=nullptr){
                root=root->right;
            }
            return root->data;
        }
        
    }
    
	bool checkBST(Node* root) {
        
        if (root==nullptr){
            return 1;
        }
        int min_right, max_left;
        int leftVal, rightVal;
        
        if (root->left==nullptr){
            leftVal=0;
        }
        else{
            leftVal=root->left->data;
        }
        if (root->right==nullptr){
            rightVal=10000;
        }
        else{
            rightVal=root->right->data;
        }
        
        if(leftVal < root->data && root->data < rightVal){
            if(root->right==nullptr){
                min_right=10000;
            }
            else{
                min_right=getMin(root->right);    
            }
            if(root->left==nullptr){
                max_left=0;    
            }
            else{
                max_left=getMax(root->left);
                //cout<<"current node="<<root->data<<" min_right="<<min_right<<" max_left="<<max_left<<"\n";
            }
            if(checkBST(root->left)&& checkBST(root->right) && min_right>root->data && max_left<root->data){
                //cout<<"pass"<<root->data;
                return 1;
            }
            else{
                //cout<<"fail"<<root->data;
                return 0;
            }
            
            
        
        }
        else{
            //cout<<"fail"<<root->data;
            return 0;
        }
		
	}
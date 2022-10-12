class Solution {
public:
    TreeNode* deleteNode(TreeNode* root, int key) {
        if(!root) return nullptr;
		// search for key node
        if(root -> val < key) root -> right = deleteNode(root -> right, key);
        else if(root -> val > key) root -> left = deleteNode(root -> left, key);
        else { // root -> val == key
            auto toDelete = root;
            if(!root -> left || !root -> right) 
                root = root -> left ? root -> left : root -> right;
            else {
				auto cur = root, par = root;
                root = root -> right;
                while(root -> left) par = root, root = root -> left;  // finding smallest in right subtree
                cur -> val = root -> val;                             // replace node to be deleted- cur with value of smallest node found
				// take care of child node...same as above
                if(par -> left == root) par -> left = root -> right;
                else par -> right = root -> right;
				toDelete = root;
                root = cur;
            }
            delete toDelete;            			
        }
        return root;
    }
};

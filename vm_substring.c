#define MAX_CHAR 26
class SuffixTrieNode 
{ 
public: 
    SuffixTrieNode *children[MAX_CHAR]; 
    SuffixTrieNode() // Constructor 
    { 
        // Initialize all child pointers as NULL 
        for (int i = 0; i < MAX_CHAR; i++) 
          children[i] = NULL; 
    } 
  
    // A recursive function to insert a suffix of the s 
    // in subtree rooted with this node 
    void insertSuffix(string suffix); 
}; 
  
// A Trie of all suffixes 
class SuffixTrie 
{ 
    SuffixTrieNode *root; 
    long _countNodesInTrie(SuffixTrieNode *); 
public: 
    // Constructor (Builds a trie of suffies of the given text) 
    SuffixTrie(string s) 
    { 
        root = new SuffixTrieNode(); 
  
        // Consider all suffixes of given string and insert 
        // them into the Suffix Trie using recursive function 
        // insertSuffix() in SuffixTrieNode class 
        for (int i = 0; i < s.length(); i++) 
            root->insertSuffix(s.substr(i)); 
    } 
  
    //  method to count total nodes in suffix trie 
    int countNodesInTrie() { return _countNodesInTrie(root); } 
}; 
  
// A recursive function to insert a suffix of the s in 
// subtree rooted with this node 
void SuffixTrieNode::insertSuffix(string s) 
{ 
    // If string has more characters 
    if (s.length() > 0) 
    { 
        // Find the first character and convert it 
        // into 0-25 range. 
        char cIndex = s.at(0) - 'a'; 
  
        // If there is no edge for this character, 
        // add a new edge 
        if (children[cIndex] == NULL) 
            children[cIndex] = new SuffixTrieNode(); 
  
        // Recur for next suffix 
        children[cIndex]->insertSuffix(s.substr(1)); 
    } 
} 
  
// A recursive function to count nodes in trie 
long SuffixTrie::_countNodesInTrie(SuffixTrieNode* node) 
{ 
    // If all characters of pattern have been processed, 
    if (node == NULL) 
        return 0; 
  
    long count = 0; 
    for (int i = 0; i < MAX_CHAR; i++) 
    { 
        // if children is not NULL then find count 
        // of all nodes in this subtrie 
        if (node->children[i] != NULL) 
            count += _countNodesInTrie(node->children[i]); 
    } 
  
    // return count of nodes of subtrie and plus 
    // 1 because of node's own count 
    return (1 + count); 
} 
long substringCalculator(string s) {
    // Construct a Trie of all suffixes 
    SuffixTrie sTrie(s); 
  
    // Return count of nodes in Trie of Suffixes 
    long m = sTrie.countNodesInTrie(); 
    return (m-1);
}

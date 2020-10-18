import java.util.HashMap; 

// Trie Node, which stores a character and the children in a HashMap 
class TrieNode { 
	public TrieNode(char ch) { 
		value = ch; 
		children = new HashMap<>(); 
		bIsEnd = false; 
	} 
	public HashMap<Character,TrieNode> getChildren() { return children; } 
	public char getValue()						 { return value;	 } 
	public void setIsEnd(boolean val)			 { bIsEnd = val;	 } 
	public boolean isEnd()						 { return bIsEnd; } 

	private char value; 
	private HashMap<Character,TrieNode> children; 
	private boolean bIsEnd; 
} 

// Implements the actual Trie 
class Trie { 
	// Constructor 
	public Trie() {	 root = new TrieNode((char)0);	 }	 

	// Method to insert a new word to Trie 
	public void insert(String word) { 

		// Find length of the given word 
		int length = word.length(); 
		TrieNode crawl = root; 

		// Traverse through all characters of given word 
		for( int level = 0; level < length; level++) 
		{ 
			HashMap<Character,TrieNode> child = crawl.getChildren(); 
			char ch = word.charAt(level); 

			// If there is already a child for current character of given word 
			if( child.containsKey(ch)) 
				crawl = child.get(ch); 
			else // Else create a child 
			{ 
				TrieNode temp = new TrieNode(ch); 
				child.put( ch, temp ); 
				crawl = temp; 
			} 
		} 

		// Set bIsEnd true for last character 
		crawl.setIsEnd(true); 
	} 

	// The main method that finds out the longest string 'input' 
	public String getMatchingPrefix(String input) { 
		String result = ""; // Initialize resultant string 
		int length = input.length(); // Find length of the input string	 

		// Initialize reference to traverse through Trie 
		TrieNode crawl = root; 

		// Iterate through all characters of input string 'str' and traverse 
		// down the Trie 
		int level, prevMatch = 0; 
		for( level = 0 ; level < length; level++ ) 
		{ 
			// Find current character of str 
			char ch = input.charAt(level);	 

			// HashMap of current Trie node to traverse down 
			HashMap<Character,TrieNode> child = crawl.getChildren();						 

			// See if there is a Trie edge for the current character 
			if( child.containsKey(ch) ) 
			{ 
			result += ch;		 //Update result 
			crawl = child.get(ch); //Update crawl to move down in Trie 

			// If this is end of a word, then update prevMatch 
			if( crawl.isEnd() ) 
					prevMatch = level + 1; 
			} 
			else break; 
		} 

		// If the last processed character did not match end of a word, 
		// return the previously matching prefix 
		if( !crawl.isEnd() ) 
				return result.substring(0, prevMatch);		 

		else return result; 
	} 

	private TrieNode root; 
} 

// Testing class 
public class Test { 
public static void main(String[] args) { 
		Trie dict = new Trie(); 
		dict.insert("are"); 
		dict.insert("area"); 
		dict.insert("base"); 
		dict.insert("cat"); 
		dict.insert("cater"); 
		dict.insert("basement"); 

		String input = "caterer"; 
		System.out.print(input + ": "); 
		System.out.println(dict.getMatchingPrefix(input));			 

		input = "basement"; 
		System.out.print(input + ": "); 
		System.out.println(dict.getMatchingPrefix(input));					 

		input = "are"; 
		System.out.print(input + ": "); 
		System.out.println(dict.getMatchingPrefix(input));			 

		input = "arex"; 
		System.out.print(input + ": "); 
		System.out.println(dict.getMatchingPrefix(input));			 

		input = "basemexz"; 
		System.out.print(input + ": "); 
		System.out.println(dict.getMatchingPrefix(input));					 

		input = "xyz"; 
		System.out.print(input + ": "); 
		System.out.println(dict.getMatchingPrefix(input)); 
	} 
}

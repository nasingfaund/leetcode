class TrieNode:
    def __init__(self, children: Dict[str, 'TrieNode'] = None, end_of_word: bool = False):
        self.children = children or dict()
        self.end_of_word = end_of_word
        
class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                new_node = TrieNode()
                curr.children[c] = new_node
                curr = new_node
            else:
                curr = curr.children[c]
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.end_of_word
                

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True

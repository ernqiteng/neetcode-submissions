class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for i in range(len(word)):
            if word[i] not in node.children.keys():
                node.children[word[i]] = TrieNode()
            node = node.children[word[i]]
        node.endOfWord = True

    def search(self, word: str) -> bool:
        node = self.root
        for i in range(len(word)):
            if word[i] not in node.children.keys():
                return False
            node = node.children[word[i]]
        return node.endOfWord        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in range(len(prefix)):
            if prefix[i] not in node.children.keys():
                return False
            node = node.children[prefix[i]]
        return True 
        
        
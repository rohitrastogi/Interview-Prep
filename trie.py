from collections import deque 
#simple trie implementation
#insert, search, 'suggest'

# max number of children is number of different characters (26 in case of letters)
# max height is length of key (infinite length)

class TrieNode():
    def __init__(self):
        self.value = None
        # key: character, value: node
        self.children = {}

    def contains(self, string):
        curr = self
        for char in string:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return False
        return True if curr.value else False 

    def insert(self, string):
        curr = self
        last_index = None
        for index, char in enumerate(string):
            if char in curr.children:
                curr = curr.children[char]
            else:
                last_index = index
                break
        for char in string[last_index:]:
            curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.value = string 

    #use bfs because we want to sort suggestions by length 
    def suggest(self, string):
    
        def find(): 
            curr = self
            for char in string:
                if char in curr.children:
                    curr = curr.children[char]
                else:
                    return None
            return curr

        suggestions = []
        queue = deque([])
        root = find()
        if root:
            queue.append(find())
        while queue:
            curr = queue.popleft()
            for char in curr.children:
                val = curr.children[char].value
                if val:
                    suggestions.append(val)
                queue.append(curr.children[char])

        return suggestions
        
        
test = TrieNode()
test.insert('test')
print(test.contains('test'))
print(test.contains('terribletestcase'))
test.insert('terribletestcase')
test.insert('tests')
test.insert('startswithadifferentchar')
print(test.suggest('t')) 
print(test.suggest('s'))
print(test.suggest('a'))

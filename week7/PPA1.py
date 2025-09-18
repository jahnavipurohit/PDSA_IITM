'''Write a function Huffman(s) that accepts a string s of characters a,b,c,d,e and f without any space. 
The function should generate the prefix code for each character based on its frequency in string s 
and return a dictionary where the key of the dictionary represents the character and the 
corresponding value represents the Huffman code for that character.

Select two smallest frequency nodes each time. If more than two nodes have the same smallest frequency, 
then select nodes in the lexicographical order of their symbol. Assume that x and y are 
the two smallest nodes, then:-
If x. frequency < y.frequency then x will always come on the left and 
y will always come on the right of the parent node.
If x. frequency = y.frequency then the symbol of node, which comes first in lexicographical order, 
will become the left child, and others will become the right child of the parent node.
If x is a left node and y is a right node, then the parent node will be identified by
x. symbol + y.symbol for further creation of the tree.'''

class Node:
    def __init__(self,frequency,symbol = None,left = None,right = None):
        self.frequency = frequency
        self.symbol = symbol
        self.left = left
        self.right = right

    def __lt__(self, other):
        return (self.frequency, self.symbol) < (other.frequency, other.symbol)

def generate_codes(node, code, codes_dict):
    if node is None:
        return

    if node.left is None and node.right is None:
        codes_dict[node.symbol] = code
        return

    generate_codes(node.left, code + '0', codes_dict)
    generate_codes(node.right, code + '1', codes_dict)


def Huffman(s):
    if not s:
        return {}

    # Manually count the frequency of each character
    frequencies = {}
    for char in s:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1

    # Create a list of Node objects
    nodes = [Node(freq, char) for char, freq in frequencies.items()]

    # Manually build the Huffman tree by combining nodes
    while len(nodes) > 1:
        # Sort the nodes list to find the two smallest frequency nodes
        # The __lt__ method handles the sorting order and tie-breaking
        nodes.sort()
        x = nodes.pop(0)
        y = nodes.pop(0)

        # Create a new parent node
        parent_frequency = x.frequency + y.frequency
        parent_symbol = x.symbol + y.symbol
        parent_node = Node(parent_frequency, parent_symbol, x, y)
        
        # Add the new parent node back to the list
        nodes.append(parent_node)

    root = nodes[0]
    huffman_codes = {}
    generate_codes(root, "", huffman_codes)
    
    return huffman_codes



s = input()
res = Huffman(s)
for char in sorted(res):
    print(char,res[char])
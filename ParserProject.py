import sys
from antlr4 import *
from antlr4.tree.Tree import TerminalNode  # Import TerminalNode from the Tree module
from D1Parser import D1Parser  # Import your generated parser
from D1Lexer import D1Lexer      # Import your generated lexer

def print_tree(node, level=0):
    # If the node is None, return early
    if node is None:
        return
    
    indent = '  ' * level
    node_type = type(node).__name__  # Get the name of the node type
    node_text = node.getText()  # Get the text for the current node
    
    # Print the node text along with its type
    print(f"{indent}{node_type}: {node_text}")
    
    # Iterate over children nodes
    if hasattr(node, 'children'):
        for child in node.children:
            print_tree(child, level + 1)

# Main execution
def main(input_file):
    input_stream = FileStream(input_file)
    lexer = D1Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = D1Parser(stream)
    
    tree = parser.program()  # Start parsing from the program rule
    print_tree(tree)  # Print the parse tree

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python ParserProject.py <input_file>")
        sys.exit(1)

    main(sys.argv[1])

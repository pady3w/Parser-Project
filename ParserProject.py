from antlr4 import *
from D3Lexer import D3Lexer
from D3Parser import D3Parser
from antlr4 import TerminalNode

class IndentDedentProcessor:
    def __init__(self, input_code):
        self.input_code = input_code
        self.output_code = []
        self.indent_stack = [0]

    def preprocess(self):
        lines = self.input_code.splitlines()
        for line in lines:
            stripped_line = line.lstrip()
            current_indent = len(line) - len(stripped_line)

            # Ignore blank lines
            if stripped_line:
                if current_indent > self.indent_stack[-1]:
                    self.output_code.append('<INDENT>')
                    self.indent_stack.append(current_indent)
                while current_indent < self.indent_stack[-1]:
                    self.output_code.append('<DEDENT>')
                    self.indent_stack.pop()

            self.output_code.append(stripped_line)

        # Ensure proper dedentation at EOF
        while len(self.indent_stack) > 1:
            self.output_code.append('<DEDENT>')
            self.indent_stack.pop()

        return '\n'.join(self.output_code)

class TreePrinter:
    def __init__(self, tree, parser):
        self.tree = tree
        self.parser = parser

    # Helper function to get text from a node
    def get_node_text(self, node):
        if isinstance(node, TerminalNode):
            return node.getText()
        return self.parser.ruleNames[node.getRuleIndex()]
    
    # Start tree printing from the root
    def print_tree(self):
        self.visit(self.tree)

    # Recursively visit and print the nodes of the tree
    def visit(self, node, indent_level=0):
        if node is None:
            return

        indent = '  ' * indent_level
        node_name = self.get_node_text(node)

        # Print the node with its label and value (if applicable)
        print(f"{indent}{node.__class__.__name__}: {node_name}")

        # Visit all children of the current node
        for i in range(node.getChildCount()):
            self.visit(node.getChild(i), indent_level + 1)

if __name__ == "__main__":
    # Read the Python code from project_deliverable_3.py
    with open("project_deliverable_3.py", "r") as f:
        input_code = f.read()

    # Preprocess the code
    preprocessor = IndentDedentProcessor(input_code)
    processed_code = preprocessor.preprocess()

    # Print the preprocessed code for debugging
    print("Preprocessed Code:")
    print(processed_code)

    # Parse the preprocessed code using ANTLR
    input_stream = InputStream(processed_code)
    lexer = D3Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = D3Parser(stream)

    # Generate the parse tree
    tree = parser.program()
    # print(tree.toStringTree(recog=parser))  # Raw parse tree for debugging

    # Pass the tree to TreePrinter
    tree_printer = TreePrinter(tree, parser)

    # Print the tree
    tree_printer.print_tree()
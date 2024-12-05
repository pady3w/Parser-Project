1) Project Intro
This project parses Python files, specifically project_deliverable_3.py. This is done using ANTLR alongside a Python file holding some logic for reading pieces of Python code. The third deliverable is the only one in this repository since all past deliverables are included in D3. 


2) Team Members
Parker Dierkens is the sole team member of this group


3) How to run
To run this project, the user needs to have Java, Python, and ANTLR installed. It is recommended to use VS Code. Download the project files and navigate to their location in a terminal. Once there, you can rebuild D3.interp. D3.tokens, D3Lexer.interp, D3Lexer.py, D3Lexer.tokens, D3Listener.py, and D3Parser.py by calling your designated CLASSPATH for ANTLR followed by the grammar file D3.g4. If you do not have a CLASSPATH set, you can ANTLR directly just like the following: 

java -jar "C:\Program Files\Java\jdk-23\lib\antlr-4.13.2-complete.jar" -Dlanguage=Python3 D3.g4

When your parsing and lexing files are ready you can run the program using the following:

python ParserProject.py project_deliverable_3.py 

The generated parse tree is shown in the terminal. An example of this full tree is shown in "Printed Tree.pdf".


4) Video Link
https://youtu.be/kwns4L3I2IE

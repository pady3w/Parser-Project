# Generated from D1.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .D1Parser import D1Parser
else:
    from D1Parser import D1Parser

# This class defines a complete listener for a parse tree produced by D1Parser.
class D1Listener(ParseTreeListener):

    # Enter a parse tree produced by D1Parser#program.
    def enterProgram(self, ctx:D1Parser.ProgramContext):
        pass

    # Exit a parse tree produced by D1Parser#program.
    def exitProgram(self, ctx:D1Parser.ProgramContext):
        pass


    # Enter a parse tree produced by D1Parser#statement.
    def enterStatement(self, ctx:D1Parser.StatementContext):
        pass

    # Exit a parse tree produced by D1Parser#statement.
    def exitStatement(self, ctx:D1Parser.StatementContext):
        pass


    # Enter a parse tree produced by D1Parser#expressionStatement.
    def enterExpressionStatement(self, ctx:D1Parser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by D1Parser#expressionStatement.
    def exitExpressionStatement(self, ctx:D1Parser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by D1Parser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:D1Parser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by D1Parser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:D1Parser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by D1Parser#expression.
    def enterExpression(self, ctx:D1Parser.ExpressionContext):
        pass

    # Exit a parse tree produced by D1Parser#expression.
    def exitExpression(self, ctx:D1Parser.ExpressionContext):
        pass


    # Enter a parse tree produced by D1Parser#list.
    def enterList(self, ctx:D1Parser.ListContext):
        pass

    # Exit a parse tree produced by D1Parser#list.
    def exitList(self, ctx:D1Parser.ListContext):
        pass


    # Enter a parse tree produced by D1Parser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:D1Parser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by D1Parser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:D1Parser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by D1Parser#arithmeticOperator.
    def enterArithmeticOperator(self, ctx:D1Parser.ArithmeticOperatorContext):
        pass

    # Exit a parse tree produced by D1Parser#arithmeticOperator.
    def exitArithmeticOperator(self, ctx:D1Parser.ArithmeticOperatorContext):
        pass



del D1Parser
# Generated from D3.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .D3Parser import D3Parser
else:
    from D3Parser import D3Parser

# This class defines a complete listener for a parse tree produced by D3Parser.
class D3Listener(ParseTreeListener):

    # Enter a parse tree produced by D3Parser#program.
    def enterProgram(self, ctx:D3Parser.ProgramContext):
        pass

    # Exit a parse tree produced by D3Parser#program.
    def exitProgram(self, ctx:D3Parser.ProgramContext):
        pass


    # Enter a parse tree produced by D3Parser#statement.
    def enterStatement(self, ctx:D3Parser.StatementContext):
        pass

    # Exit a parse tree produced by D3Parser#statement.
    def exitStatement(self, ctx:D3Parser.StatementContext):
        pass


    # Enter a parse tree produced by D3Parser#expressionStatement.
    def enterExpressionStatement(self, ctx:D3Parser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by D3Parser#expressionStatement.
    def exitExpressionStatement(self, ctx:D3Parser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by D3Parser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:D3Parser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by D3Parser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:D3Parser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by D3Parser#expression.
    def enterExpression(self, ctx:D3Parser.ExpressionContext):
        pass

    # Exit a parse tree produced by D3Parser#expression.
    def exitExpression(self, ctx:D3Parser.ExpressionContext):
        pass


    # Enter a parse tree produced by D3Parser#conditionalStatement.
    def enterConditionalStatement(self, ctx:D3Parser.ConditionalStatementContext):
        pass

    # Exit a parse tree produced by D3Parser#conditionalStatement.
    def exitConditionalStatement(self, ctx:D3Parser.ConditionalStatementContext):
        pass


    # Enter a parse tree produced by D3Parser#loopStatement.
    def enterLoopStatement(self, ctx:D3Parser.LoopStatementContext):
        pass

    # Exit a parse tree produced by D3Parser#loopStatement.
    def exitLoopStatement(self, ctx:D3Parser.LoopStatementContext):
        pass


    # Enter a parse tree produced by D3Parser#block.
    def enterBlock(self, ctx:D3Parser.BlockContext):
        pass

    # Exit a parse tree produced by D3Parser#block.
    def exitBlock(self, ctx:D3Parser.BlockContext):
        pass


    # Enter a parse tree produced by D3Parser#condition.
    def enterCondition(self, ctx:D3Parser.ConditionContext):
        pass

    # Exit a parse tree produced by D3Parser#condition.
    def exitCondition(self, ctx:D3Parser.ConditionContext):
        pass


    # Enter a parse tree produced by D3Parser#logicalTerm.
    def enterLogicalTerm(self, ctx:D3Parser.LogicalTermContext):
        pass

    # Exit a parse tree produced by D3Parser#logicalTerm.
    def exitLogicalTerm(self, ctx:D3Parser.LogicalTermContext):
        pass


    # Enter a parse tree produced by D3Parser#ArgumentList.
    def enterArgumentList(self, ctx:D3Parser.ArgumentListContext):
        pass

    # Exit a parse tree produced by D3Parser#ArgumentList.
    def exitArgumentList(self, ctx:D3Parser.ArgumentListContext):
        pass


    # Enter a parse tree produced by D3Parser#comparison.
    def enterComparison(self, ctx:D3Parser.ComparisonContext):
        pass

    # Exit a parse tree produced by D3Parser#comparison.
    def exitComparison(self, ctx:D3Parser.ComparisonContext):
        pass


    # Enter a parse tree produced by D3Parser#list.
    def enterList(self, ctx:D3Parser.ListContext):
        pass

    # Exit a parse tree produced by D3Parser#list.
    def exitList(self, ctx:D3Parser.ListContext):
        pass


    # Enter a parse tree produced by D3Parser#comparisonOperator.
    def enterComparisonOperator(self, ctx:D3Parser.ComparisonOperatorContext):
        pass

    # Exit a parse tree produced by D3Parser#comparisonOperator.
    def exitComparisonOperator(self, ctx:D3Parser.ComparisonOperatorContext):
        pass


    # Enter a parse tree produced by D3Parser#logicalOperator.
    def enterLogicalOperator(self, ctx:D3Parser.LogicalOperatorContext):
        pass

    # Exit a parse tree produced by D3Parser#logicalOperator.
    def exitLogicalOperator(self, ctx:D3Parser.LogicalOperatorContext):
        pass


    # Enter a parse tree produced by D3Parser#unaryOperator.
    def enterUnaryOperator(self, ctx:D3Parser.UnaryOperatorContext):
        pass

    # Exit a parse tree produced by D3Parser#unaryOperator.
    def exitUnaryOperator(self, ctx:D3Parser.UnaryOperatorContext):
        pass


    # Enter a parse tree produced by D3Parser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:D3Parser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by D3Parser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:D3Parser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by D3Parser#arithmeticOperator.
    def enterArithmeticOperator(self, ctx:D3Parser.ArithmeticOperatorContext):
        pass

    # Exit a parse tree produced by D3Parser#arithmeticOperator.
    def exitArithmeticOperator(self, ctx:D3Parser.ArithmeticOperatorContext):
        pass



del D3Parser
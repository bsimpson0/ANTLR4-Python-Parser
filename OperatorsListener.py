# Generated from Operators.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .OperatorsParser import OperatorsParser
else:
    from OperatorsParser import OperatorsParser

# This class defines a complete listener for a parse tree produced by OperatorsParser.
class OperatorsListener(ParseTreeListener):

    # Enter a parse tree produced by OperatorsParser#program.
    def enterProgram(self, ctx:OperatorsParser.ProgramContext):
        pass

    # Exit a parse tree produced by OperatorsParser#program.
    def exitProgram(self, ctx:OperatorsParser.ProgramContext):
        pass


    # Enter a parse tree produced by OperatorsParser#statement.
    def enterStatement(self, ctx:OperatorsParser.StatementContext):
        pass

    # Exit a parse tree produced by OperatorsParser#statement.
    def exitStatement(self, ctx:OperatorsParser.StatementContext):
        pass


    # Enter a parse tree produced by OperatorsParser#assignment.
    def enterAssignment(self, ctx:OperatorsParser.AssignmentContext):
        pass

    # Exit a parse tree produced by OperatorsParser#assignment.
    def exitAssignment(self, ctx:OperatorsParser.AssignmentContext):
        pass


    # Enter a parse tree produced by OperatorsParser#expression.
    def enterExpression(self, ctx:OperatorsParser.ExpressionContext):
        pass

    # Exit a parse tree produced by OperatorsParser#expression.
    def exitExpression(self, ctx:OperatorsParser.ExpressionContext):
        pass


    # Enter a parse tree produced by OperatorsParser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:OperatorsParser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by OperatorsParser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:OperatorsParser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by OperatorsParser#arithmeticOperator.
    def enterArithmeticOperator(self, ctx:OperatorsParser.ArithmeticOperatorContext):
        pass

    # Exit a parse tree produced by OperatorsParser#arithmeticOperator.
    def exitArithmeticOperator(self, ctx:OperatorsParser.ArithmeticOperatorContext):
        pass


    # Enter a parse tree produced by OperatorsParser#comparisonOperator.
    def enterComparisonOperator(self, ctx:OperatorsParser.ComparisonOperatorContext):
        pass

    # Exit a parse tree produced by OperatorsParser#comparisonOperator.
    def exitComparisonOperator(self, ctx:OperatorsParser.ComparisonOperatorContext):
        pass


    # Enter a parse tree produced by OperatorsParser#logicalOperator.
    def enterLogicalOperator(self, ctx:OperatorsParser.LogicalOperatorContext):
        pass

    # Exit a parse tree produced by OperatorsParser#logicalOperator.
    def exitLogicalOperator(self, ctx:OperatorsParser.LogicalOperatorContext):
        pass


    # Enter a parse tree produced by OperatorsParser#conditionalStatement.
    def enterConditionalStatement(self, ctx:OperatorsParser.ConditionalStatementContext):
        pass

    # Exit a parse tree produced by OperatorsParser#conditionalStatement.
    def exitConditionalStatement(self, ctx:OperatorsParser.ConditionalStatementContext):
        pass


    # Enter a parse tree produced by OperatorsParser#ifStatement.
    def enterIfStatement(self, ctx:OperatorsParser.IfStatementContext):
        pass

    # Exit a parse tree produced by OperatorsParser#ifStatement.
    def exitIfStatement(self, ctx:OperatorsParser.IfStatementContext):
        pass


    # Enter a parse tree produced by OperatorsParser#elifStatement.
    def enterElifStatement(self, ctx:OperatorsParser.ElifStatementContext):
        pass

    # Exit a parse tree produced by OperatorsParser#elifStatement.
    def exitElifStatement(self, ctx:OperatorsParser.ElifStatementContext):
        pass


    # Enter a parse tree produced by OperatorsParser#elseStatement.
    def enterElseStatement(self, ctx:OperatorsParser.ElseStatementContext):
        pass

    # Exit a parse tree produced by OperatorsParser#elseStatement.
    def exitElseStatement(self, ctx:OperatorsParser.ElseStatementContext):
        pass


    # Enter a parse tree produced by OperatorsParser#whileStatement.
    def enterWhileStatement(self, ctx:OperatorsParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by OperatorsParser#whileStatement.
    def exitWhileStatement(self, ctx:OperatorsParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by OperatorsParser#forStatement.
    def enterForStatement(self, ctx:OperatorsParser.ForStatementContext):
        pass

    # Exit a parse tree produced by OperatorsParser#forStatement.
    def exitForStatement(self, ctx:OperatorsParser.ForStatementContext):
        pass


    # Enter a parse tree produced by OperatorsParser#logicalAnd.
    def enterLogicalAnd(self, ctx:OperatorsParser.LogicalAndContext):
        pass

    # Exit a parse tree produced by OperatorsParser#logicalAnd.
    def exitLogicalAnd(self, ctx:OperatorsParser.LogicalAndContext):
        pass


    # Enter a parse tree produced by OperatorsParser#logicalOr.
    def enterLogicalOr(self, ctx:OperatorsParser.LogicalOrContext):
        pass

    # Exit a parse tree produced by OperatorsParser#logicalOr.
    def exitLogicalOr(self, ctx:OperatorsParser.LogicalOrContext):
        pass


    # Enter a parse tree produced by OperatorsParser#logicalNot.
    def enterLogicalNot(self, ctx:OperatorsParser.LogicalNotContext):
        pass

    # Exit a parse tree produced by OperatorsParser#logicalNot.
    def exitLogicalNot(self, ctx:OperatorsParser.LogicalNotContext):
        pass


    # Enter a parse tree produced by OperatorsParser#forIn.
    def enterForIn(self, ctx:OperatorsParser.ForInContext):
        pass

    # Exit a parse tree produced by OperatorsParser#forIn.
    def exitForIn(self, ctx:OperatorsParser.ForInContext):
        pass


    # Enter a parse tree produced by OperatorsParser#forRange.
    def enterForRange(self, ctx:OperatorsParser.ForRangeContext):
        pass

    # Exit a parse tree produced by OperatorsParser#forRange.
    def exitForRange(self, ctx:OperatorsParser.ForRangeContext):
        pass


    # Enter a parse tree produced by OperatorsParser#range.
    def enterRange(self, ctx:OperatorsParser.RangeContext):
        pass

    # Exit a parse tree produced by OperatorsParser#range.
    def exitRange(self, ctx:OperatorsParser.RangeContext):
        pass


    # Enter a parse tree produced by OperatorsParser#array.
    def enterArray(self, ctx:OperatorsParser.ArrayContext):
        pass

    # Exit a parse tree produced by OperatorsParser#array.
    def exitArray(self, ctx:OperatorsParser.ArrayContext):
        pass



del OperatorsParser
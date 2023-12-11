// Generated from /home/parallels/Desktop/test4450/Operators.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link OperatorsParser}.
 */
public interface OperatorsListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link OperatorsParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(OperatorsParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link OperatorsParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(OperatorsParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link OperatorsParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(OperatorsParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link OperatorsParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(OperatorsParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link OperatorsParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(OperatorsParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link OperatorsParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(OperatorsParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link OperatorsParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(OperatorsParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link OperatorsParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(OperatorsParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link OperatorsParser#array}.
	 * @param ctx the parse tree
	 */
	void enterArray(OperatorsParser.ArrayContext ctx);
	/**
	 * Exit a parse tree produced by {@link OperatorsParser#array}.
	 * @param ctx the parse tree
	 */
	void exitArray(OperatorsParser.ArrayContext ctx);
	/**
	 * Enter a parse tree produced by {@link OperatorsParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void enterIfStatement(OperatorsParser.IfStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link OperatorsParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void exitIfStatement(OperatorsParser.IfStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link OperatorsParser#elifStatement}.
	 * @param ctx the parse tree
	 */
	void enterElifStatement(OperatorsParser.ElifStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link OperatorsParser#elifStatement}.
	 * @param ctx the parse tree
	 */
	void exitElifStatement(OperatorsParser.ElifStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link OperatorsParser#elseStatement}.
	 * @param ctx the parse tree
	 */
	void enterElseStatement(OperatorsParser.ElseStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link OperatorsParser#elseStatement}.
	 * @param ctx the parse tree
	 */
	void exitElseStatement(OperatorsParser.ElseStatementContext ctx);
}
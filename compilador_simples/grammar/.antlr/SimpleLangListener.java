// Generated from c:/Users/caioburton/Documents/tutorial-llvm/compilador_simples/grammar/SimpleLang.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link SimpleLangParser}.
 */
public interface SimpleLangListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link SimpleLangParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(SimpleLangParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleLangParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(SimpleLangParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleLangParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(SimpleLangParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleLangParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(SimpleLangParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link SimpleLangParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(SimpleLangParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link SimpleLangParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(SimpleLangParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Variable}
	 * labeled alternative in {@link SimpleLangParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterVariable(SimpleLangParser.VariableContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Variable}
	 * labeled alternative in {@link SimpleLangParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitVariable(SimpleLangParser.VariableContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Number}
	 * labeled alternative in {@link SimpleLangParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterNumber(SimpleLangParser.NumberContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Number}
	 * labeled alternative in {@link SimpleLangParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitNumber(SimpleLangParser.NumberContext ctx);
	/**
	 * Enter a parse tree produced by the {@code MulDiv}
	 * labeled alternative in {@link SimpleLangParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterMulDiv(SimpleLangParser.MulDivContext ctx);
	/**
	 * Exit a parse tree produced by the {@code MulDiv}
	 * labeled alternative in {@link SimpleLangParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitMulDiv(SimpleLangParser.MulDivContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AddSub}
	 * labeled alternative in {@link SimpleLangParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterAddSub(SimpleLangParser.AddSubContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AddSub}
	 * labeled alternative in {@link SimpleLangParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitAddSub(SimpleLangParser.AddSubContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Parentheses}
	 * labeled alternative in {@link SimpleLangParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterParentheses(SimpleLangParser.ParenthesesContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Parentheses}
	 * labeled alternative in {@link SimpleLangParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitParentheses(SimpleLangParser.ParenthesesContext ctx);
}
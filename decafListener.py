# Generated from decaf.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .decafParser import decafParser
else:
    from decafParser import decafParser

# This class defines a complete listener for a parse tree produced by decafParser.
class decafListener(ParseTreeListener):

    # Enter a parse tree produced by decafParser#program.
    def enterProgram(self, ctx:decafParser.ProgramContext):
        pass

    # Exit a parse tree produced by decafParser#program.
    def exitProgram(self, ctx:decafParser.ProgramContext):
        pass


    # Enter a parse tree produced by decafParser#declaration.
    def enterDeclaration(self, ctx:decafParser.DeclarationContext):
        pass

    # Exit a parse tree produced by decafParser#declaration.
    def exitDeclaration(self, ctx:decafParser.DeclarationContext):
        pass


    # Enter a parse tree produced by decafParser#normalVar.
    def enterNormalVar(self, ctx:decafParser.NormalVarContext):
        pass

    # Exit a parse tree produced by decafParser#normalVar.
    def exitNormalVar(self, ctx:decafParser.NormalVarContext):
        pass


    # Enter a parse tree produced by decafParser#arrayVar.
    def enterArrayVar(self, ctx:decafParser.ArrayVarContext):
        pass

    # Exit a parse tree produced by decafParser#arrayVar.
    def exitArrayVar(self, ctx:decafParser.ArrayVarContext):
        pass


    # Enter a parse tree produced by decafParser#structDeclaration.
    def enterStructDeclaration(self, ctx:decafParser.StructDeclarationContext):
        pass

    # Exit a parse tree produced by decafParser#structDeclaration.
    def exitStructDeclaration(self, ctx:decafParser.StructDeclarationContext):
        pass


    # Enter a parse tree produced by decafParser#varType.
    def enterVarType(self, ctx:decafParser.VarTypeContext):
        pass

    # Exit a parse tree produced by decafParser#varType.
    def exitVarType(self, ctx:decafParser.VarTypeContext):
        pass


    # Enter a parse tree produced by decafParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:decafParser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by decafParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:decafParser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by decafParser#methodType.
    def enterMethodType(self, ctx:decafParser.MethodTypeContext):
        pass

    # Exit a parse tree produced by decafParser#methodType.
    def exitMethodType(self, ctx:decafParser.MethodTypeContext):
        pass


    # Enter a parse tree produced by decafParser#parameter.
    def enterParameter(self, ctx:decafParser.ParameterContext):
        pass

    # Exit a parse tree produced by decafParser#parameter.
    def exitParameter(self, ctx:decafParser.ParameterContext):
        pass


    # Enter a parse tree produced by decafParser#parameterType.
    def enterParameterType(self, ctx:decafParser.ParameterTypeContext):
        pass

    # Exit a parse tree produced by decafParser#parameterType.
    def exitParameterType(self, ctx:decafParser.ParameterTypeContext):
        pass


    # Enter a parse tree produced by decafParser#block.
    def enterBlock(self, ctx:decafParser.BlockContext):
        pass

    # Exit a parse tree produced by decafParser#block.
    def exitBlock(self, ctx:decafParser.BlockContext):
        pass


    # Enter a parse tree produced by decafParser#ifScope.
    def enterIfScope(self, ctx:decafParser.IfScopeContext):
        pass

    # Exit a parse tree produced by decafParser#ifScope.
    def exitIfScope(self, ctx:decafParser.IfScopeContext):
        pass


    # Enter a parse tree produced by decafParser#whileScope.
    def enterWhileScope(self, ctx:decafParser.WhileScopeContext):
        pass

    # Exit a parse tree produced by decafParser#whileScope.
    def exitWhileScope(self, ctx:decafParser.WhileScopeContext):
        pass


    # Enter a parse tree produced by decafParser#st_return.
    def enterSt_return(self, ctx:decafParser.St_returnContext):
        pass

    # Exit a parse tree produced by decafParser#st_return.
    def exitSt_return(self, ctx:decafParser.St_returnContext):
        pass


    # Enter a parse tree produced by decafParser#stmnt_methodCall.
    def enterStmnt_methodCall(self, ctx:decafParser.Stmnt_methodCallContext):
        pass

    # Exit a parse tree produced by decafParser#stmnt_methodCall.
    def exitStmnt_methodCall(self, ctx:decafParser.Stmnt_methodCallContext):
        pass


    # Enter a parse tree produced by decafParser#stmnt_block.
    def enterStmnt_block(self, ctx:decafParser.Stmnt_blockContext):
        pass

    # Exit a parse tree produced by decafParser#stmnt_block.
    def exitStmnt_block(self, ctx:decafParser.Stmnt_blockContext):
        pass


    # Enter a parse tree produced by decafParser#stmnt_equal.
    def enterStmnt_equal(self, ctx:decafParser.Stmnt_equalContext):
        pass

    # Exit a parse tree produced by decafParser#stmnt_equal.
    def exitStmnt_equal(self, ctx:decafParser.Stmnt_equalContext):
        pass


    # Enter a parse tree produced by decafParser#stmnt_expression.
    def enterStmnt_expression(self, ctx:decafParser.Stmnt_expressionContext):
        pass

    # Exit a parse tree produced by decafParser#stmnt_expression.
    def exitStmnt_expression(self, ctx:decafParser.Stmnt_expressionContext):
        pass


    # Enter a parse tree produced by decafParser#location.
    def enterLocation(self, ctx:decafParser.LocationContext):
        pass

    # Exit a parse tree produced by decafParser#location.
    def exitLocation(self, ctx:decafParser.LocationContext):
        pass


    # Enter a parse tree produced by decafParser#expr_literal.
    def enterExpr_literal(self, ctx:decafParser.Expr_literalContext):
        pass

    # Exit a parse tree produced by decafParser#expr_literal.
    def exitExpr_literal(self, ctx:decafParser.Expr_literalContext):
        pass


    # Enter a parse tree produced by decafParser#exp_predop.
    def enterExp_predop(self, ctx:decafParser.Exp_predopContext):
        pass

    # Exit a parse tree produced by decafParser#exp_predop.
    def exitExp_predop(self, ctx:decafParser.Exp_predopContext):
        pass


    # Enter a parse tree produced by decafParser#exp_relop.
    def enterExp_relop(self, ctx:decafParser.Exp_relopContext):
        pass

    # Exit a parse tree produced by decafParser#exp_relop.
    def exitExp_relop(self, ctx:decafParser.Exp_relopContext):
        pass


    # Enter a parse tree produced by decafParser#exp_ar_op.
    def enterExp_ar_op(self, ctx:decafParser.Exp_ar_opContext):
        pass

    # Exit a parse tree produced by decafParser#exp_ar_op.
    def exitExp_ar_op(self, ctx:decafParser.Exp_ar_opContext):
        pass


    # Enter a parse tree produced by decafParser#ex_minus.
    def enterEx_minus(self, ctx:decafParser.Ex_minusContext):
        pass

    # Exit a parse tree produced by decafParser#ex_minus.
    def exitEx_minus(self, ctx:decafParser.Ex_minusContext):
        pass


    # Enter a parse tree produced by decafParser#ex_par.
    def enterEx_par(self, ctx:decafParser.Ex_parContext):
        pass

    # Exit a parse tree produced by decafParser#ex_par.
    def exitEx_par(self, ctx:decafParser.Ex_parContext):
        pass


    # Enter a parse tree produced by decafParser#exp_eqop.
    def enterExp_eqop(self, ctx:decafParser.Exp_eqopContext):
        pass

    # Exit a parse tree produced by decafParser#exp_eqop.
    def exitExp_eqop(self, ctx:decafParser.Exp_eqopContext):
        pass


    # Enter a parse tree produced by decafParser#exp_condop.
    def enterExp_condop(self, ctx:decafParser.Exp_condopContext):
        pass

    # Exit a parse tree produced by decafParser#exp_condop.
    def exitExp_condop(self, ctx:decafParser.Exp_condopContext):
        pass


    # Enter a parse tree produced by decafParser#ex_not.
    def enterEx_not(self, ctx:decafParser.Ex_notContext):
        pass

    # Exit a parse tree produced by decafParser#ex_not.
    def exitEx_not(self, ctx:decafParser.Ex_notContext):
        pass


    # Enter a parse tree produced by decafParser#exp_location.
    def enterExp_location(self, ctx:decafParser.Exp_locationContext):
        pass

    # Exit a parse tree produced by decafParser#exp_location.
    def exitExp_location(self, ctx:decafParser.Exp_locationContext):
        pass


    # Enter a parse tree produced by decafParser#expr_methodCall.
    def enterExpr_methodCall(self, ctx:decafParser.Expr_methodCallContext):
        pass

    # Exit a parse tree produced by decafParser#expr_methodCall.
    def exitExpr_methodCall(self, ctx:decafParser.Expr_methodCallContext):
        pass


    # Enter a parse tree produced by decafParser#methodCall.
    def enterMethodCall(self, ctx:decafParser.MethodCallContext):
        pass

    # Exit a parse tree produced by decafParser#methodCall.
    def exitMethodCall(self, ctx:decafParser.MethodCallContext):
        pass


    # Enter a parse tree produced by decafParser#arg.
    def enterArg(self, ctx:decafParser.ArgContext):
        pass

    # Exit a parse tree produced by decafParser#arg.
    def exitArg(self, ctx:decafParser.ArgContext):
        pass


    # Enter a parse tree produced by decafParser#arith_op.
    def enterArith_op(self, ctx:decafParser.Arith_opContext):
        pass

    # Exit a parse tree produced by decafParser#arith_op.
    def exitArith_op(self, ctx:decafParser.Arith_opContext):
        pass


    # Enter a parse tree produced by decafParser#pred_op.
    def enterPred_op(self, ctx:decafParser.Pred_opContext):
        pass

    # Exit a parse tree produced by decafParser#pred_op.
    def exitPred_op(self, ctx:decafParser.Pred_opContext):
        pass


    # Enter a parse tree produced by decafParser#rel_op.
    def enterRel_op(self, ctx:decafParser.Rel_opContext):
        pass

    # Exit a parse tree produced by decafParser#rel_op.
    def exitRel_op(self, ctx:decafParser.Rel_opContext):
        pass


    # Enter a parse tree produced by decafParser#eq_op.
    def enterEq_op(self, ctx:decafParser.Eq_opContext):
        pass

    # Exit a parse tree produced by decafParser#eq_op.
    def exitEq_op(self, ctx:decafParser.Eq_opContext):
        pass


    # Enter a parse tree produced by decafParser#cond_op.
    def enterCond_op(self, ctx:decafParser.Cond_opContext):
        pass

    # Exit a parse tree produced by decafParser#cond_op.
    def exitCond_op(self, ctx:decafParser.Cond_opContext):
        pass


    # Enter a parse tree produced by decafParser#literal.
    def enterLiteral(self, ctx:decafParser.LiteralContext):
        pass

    # Exit a parse tree produced by decafParser#literal.
    def exitLiteral(self, ctx:decafParser.LiteralContext):
        pass


    # Enter a parse tree produced by decafParser#int_Literal.
    def enterInt_Literal(self, ctx:decafParser.Int_LiteralContext):
        pass

    # Exit a parse tree produced by decafParser#int_Literal.
    def exitInt_Literal(self, ctx:decafParser.Int_LiteralContext):
        pass


    # Enter a parse tree produced by decafParser#char_Literal.
    def enterChar_Literal(self, ctx:decafParser.Char_LiteralContext):
        pass

    # Exit a parse tree produced by decafParser#char_Literal.
    def exitChar_Literal(self, ctx:decafParser.Char_LiteralContext):
        pass


    # Enter a parse tree produced by decafParser#bool_Literal.
    def enterBool_Literal(self, ctx:decafParser.Bool_LiteralContext):
        pass

    # Exit a parse tree produced by decafParser#bool_Literal.
    def exitBool_Literal(self, ctx:decafParser.Bool_LiteralContext):
        pass



del decafParser
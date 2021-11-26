# Generated from decaf.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .decafParser import decafParser
else:
    from decafParser import decafParser

# This class defines a complete generic visitor for a parse tree produced by decafParser.

class decafVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by decafParser#program.
    def visitProgram(self, ctx:decafParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#declaration.
    def visitDeclaration(self, ctx:decafParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#normalVar.
    def visitNormalVar(self, ctx:decafParser.NormalVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#arrayVar.
    def visitArrayVar(self, ctx:decafParser.ArrayVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#structDeclaration.
    def visitStructDeclaration(self, ctx:decafParser.StructDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#varType.
    def visitVarType(self, ctx:decafParser.VarTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:decafParser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#methodType.
    def visitMethodType(self, ctx:decafParser.MethodTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#parameter.
    def visitParameter(self, ctx:decafParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#parameterType.
    def visitParameterType(self, ctx:decafParser.ParameterTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#block.
    def visitBlock(self, ctx:decafParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#ifScope.
    def visitIfScope(self, ctx:decafParser.IfScopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#whileScope.
    def visitWhileScope(self, ctx:decafParser.WhileScopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#st_return.
    def visitSt_return(self, ctx:decafParser.St_returnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#stmnt_methodCall.
    def visitStmnt_methodCall(self, ctx:decafParser.Stmnt_methodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#stmnt_block.
    def visitStmnt_block(self, ctx:decafParser.Stmnt_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#stmnt_equal.
    def visitStmnt_equal(self, ctx:decafParser.Stmnt_equalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#stmnt_expression.
    def visitStmnt_expression(self, ctx:decafParser.Stmnt_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#location.
    def visitLocation(self, ctx:decafParser.LocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#expr_literal.
    def visitExpr_literal(self, ctx:decafParser.Expr_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#exp_predop.
    def visitExp_predop(self, ctx:decafParser.Exp_predopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#exp_relop.
    def visitExp_relop(self, ctx:decafParser.Exp_relopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#exp_ar_op.
    def visitExp_ar_op(self, ctx:decafParser.Exp_ar_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#ex_minus.
    def visitEx_minus(self, ctx:decafParser.Ex_minusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#ex_par.
    def visitEx_par(self, ctx:decafParser.Ex_parContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#exp_eqop.
    def visitExp_eqop(self, ctx:decafParser.Exp_eqopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#exp_condop.
    def visitExp_condop(self, ctx:decafParser.Exp_condopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#ex_not.
    def visitEx_not(self, ctx:decafParser.Ex_notContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#exp_location.
    def visitExp_location(self, ctx:decafParser.Exp_locationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#expr_methodCall.
    def visitExpr_methodCall(self, ctx:decafParser.Expr_methodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#methodCall.
    def visitMethodCall(self, ctx:decafParser.MethodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#arg.
    def visitArg(self, ctx:decafParser.ArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#arith_op.
    def visitArith_op(self, ctx:decafParser.Arith_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#pred_op.
    def visitPred_op(self, ctx:decafParser.Pred_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#rel_op.
    def visitRel_op(self, ctx:decafParser.Rel_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#eq_op.
    def visitEq_op(self, ctx:decafParser.Eq_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#cond_op.
    def visitCond_op(self, ctx:decafParser.Cond_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#literal.
    def visitLiteral(self, ctx:decafParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#int_Literal.
    def visitInt_Literal(self, ctx:decafParser.Int_LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#char_Literal.
    def visitChar_Literal(self, ctx:decafParser.Char_LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by decafParser#bool_Literal.
    def visitBool_Literal(self, ctx:decafParser.Bool_LiteralContext):
        return self.visitChildren(ctx)



del decafParser
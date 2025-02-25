# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#decl.
    def visitDecl(self, ctx:MiniGoParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statement.
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#typedef.
    def visitTypedef(self, ctx:MiniGoParser.TypedefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#constdecl.
    def visitConstdecl(self, ctx:MiniGoParser.ConstdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#vardecl.
    def visitVardecl(self, ctx:MiniGoParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#vardeclassign.
    def visitVardeclassign(self, ctx:MiniGoParser.VardeclassignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array.
    def visitArray(self, ctx:MiniGoParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_type.
    def visitArray_type(self, ctx:MiniGoParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_index.
    def visitArray_index(self, ctx:MiniGoParser.Array_indexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_list.
    def visitArray_list(self, ctx:MiniGoParser.Array_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#array_mem.
    def visitArray_mem(self, ctx:MiniGoParser.Array_memContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structdecl.
    def visitStructdecl(self, ctx:MiniGoParser.StructdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structfielddecl.
    def visitStructfielddecl(self, ctx:MiniGoParser.StructfielddeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structliteral.
    def visitStructliteral(self, ctx:MiniGoParser.StructliteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structfieldliteral.
    def visitStructfieldliteral(self, ctx:MiniGoParser.StructfieldliteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interfacedecl.
    def visitInterfacedecl(self, ctx:MiniGoParser.InterfacedeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_signature.
    def visitMethod_signature(self, ctx:MiniGoParser.Method_signatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#argument.
    def visitArgument(self, ctx:MiniGoParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#var_access.
    def visitVar_access(self, ctx:MiniGoParser.Var_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#field_access.
    def visitField_access(self, ctx:MiniGoParser.Field_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_var_access.
    def visitMethod_var_access(self, ctx:MiniGoParser.Method_var_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#func_and_method_decl.
    def visitFunc_and_method_decl(self, ctx:MiniGoParser.Func_and_method_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method_receiver.
    def visitMethod_receiver(self, ctx:MiniGoParser.Method_receiverContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ret.
    def visitRet(self, ctx:MiniGoParser.RetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funccall.
    def visitFunccall(self, ctx:MiniGoParser.FunccallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methodcall.
    def visitMethodcall(self, ctx:MiniGoParser.MethodcallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignment.
    def visitAssignment(self, ctx:MiniGoParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expression.
    def visitExpression(self, ctx:MiniGoParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#if_stmt.
    def visitIf_stmt(self, ctx:MiniGoParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#if_condition.
    def visitIf_condition(self, ctx:MiniGoParser.If_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#block.
    def visitBlock(self, ctx:MiniGoParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#for_loop.
    def visitFor_loop(self, ctx:MiniGoParser.For_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignment_for.
    def visitAssignment_for(self, ctx:MiniGoParser.Assignment_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal.
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        return self.visitChildren(ctx)



del MiniGoParser
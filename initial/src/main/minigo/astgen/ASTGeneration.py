from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *

class ASTGeneration(MiniGoVisitor):
    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return Program([self.visit(i) for i in ctx.decl()])


    # Visit a parse tree produced by MiniGoParser#decl.
    def visitDecl(self, ctx:MiniGoParser.DeclContext):
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MiniGoParser#statement.
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#typedef.
    def visitTypedef(self, ctx:MiniGoParser.TypedefContext):
        if ctx.ATOMIC_TYPE() != None:
            match ctx.ATOMIC_TYPE().getText():
                case 'int':
                    return IntType()
                case 'float':
                    return FloatType()
                case 'boolean':
                    return BoolType()
                case 'string':
                    return StringType()
        elif ctx.ID() != None:
            return Id(ctx.ID().getText())
        elif ctx.array_type() != None:
            typ, lst = self.visit(ctx.array_type())
            return ArrayType(eleType=typ, dimens=lst)

    # Visit a parse tree produced by MiniGoParser#constdecl.
    def visitConstdecl(self, ctx:MiniGoParser.ConstdeclContext):
        val = self.visit(ctx.expression())
        return ConstDecl(ctx.ID().getText(), None, val)

    # Visit a parse tree produced by MiniGoParser#vardecl.
    def visitVardecl(self, ctx:MiniGoParser.VardeclContext):
        type_var = self.visit(ctx.typedef())
        return VarDecl(ctx.ID().getText(),type_var,None)
 
    # Visit a parse tree produced by MiniGoParser#vardeclassign.
    def visitVardeclassign(self, ctx:MiniGoParser.VardeclassignContext):
        if ctx.expression() != None:
            val = self.visit(ctx.expression())
            if ctx.typedef() is None:
                return VarDecl(ctx.ID().getText(),None,val)
            else:
                typ = self.visit(ctx.typedef())
                return VarDecl(ctx.ID().getText(),typ,val)
        elif ctx.array() != None:
            arr = self.visit(ctx.array())
            if ctx.typedef() is None:
                return VarDecl(varName=ctx.ID().getText(),varType=None,varInit=arr)
            return VarDecl(varName=ctx.ID().getText(),varType=self.visit(ctx.typedef()),varInit=arr)
        elif ctx.structliteral() != None:
            if ctx.typedef() is None:
                return VarDecl(varName=ctx.ID().getText(),varType=None,varInit=self.visit(ctx.structliteral()))
            return VarDecl(varName=ctx.ID().getText(),varType=self.visit(ctx.typedef()),varInit=self.visit(ctx.structliteral()))


    # Visit a parse tree produced by MiniGoParser#array.
    def visitArray(self, ctx:MiniGoParser.ArrayContext):
        typ, lst = self.visit(ctx.array_type())
        arr_list = self.visit(ctx.array_list())
        return ArrayLiteral(dimens=lst, eleType=typ, value=arr_list)

    # Visit a parse tree produced by MiniGoParser#array_type.
    def visitArray_type(self, ctx:MiniGoParser.Array_typeContext):
        size = ctx.getChildCount()
        list_index = []
        for i in range(size - 1):
            if ctx.array_index(i).INTEGER() != None:
                arr_index = ctx.array_index(i).INTEGER()
                list_index.append(IntLiteral(arr_index.getText()))
            elif ctx.array_index(i).ID() != None:
                arr_index = ctx.array_index(i).ID()
                list_index.append(Id(arr_index.getText()))
        
        if ctx.ATOMIC_TYPE() != None:
            match ctx.ATOMIC_TYPE().getText():
                case 'int':
                    return IntType(), list_index
                case 'float':
                    return FloatType(), list_index
                case 'boolean':
                    return BoolType(), list_index
                case 'string':
                    return StringType(), list_index
        else:
            return Id(ctx.ID().getText()), list_index
                    
    # Visit a parse tree produced by MiniGoParser#array_index.
    def visitArray_index(self, ctx:MiniGoParser.Array_indexContext):
        if ctx.INTEGER() != None:
            return IntLiteral(ctx.getChild(1).getText())
        elif ctx.ID() != None:
            return Id(ctx.getChild(1).getText())


    # Visit a parse tree produced by MiniGoParser#array_list.
    def visitArray_list(self, ctx:MiniGoParser.Array_listContext):
        return [self.visit(i) for i in ctx.array_mem()]

    # Visit a parse tree produced by MiniGoParser#array_mem.
    def visitArray_mem(self, ctx:MiniGoParser.Array_memContext):
        if ctx.ID() != None:
            return Id(ctx.ID().getText())
        if ctx.array_list() != None:
            arr_list = ctx.array_list()
            return ArrayLiteral(dimens=[],eleType=None,value=[self.visit(i) for i in arr_list.array_mem()])
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by MiniGoParser#structdecl.
    def visitStructdecl(self, ctx:MiniGoParser.StructdeclContext):
        return StructType(name=ctx.ID().getText(), elements=[self.visit(c) for c in ctx.structfielddecl()],methods=[])


    # Visit a parse tree produced by MiniGoParser#structfielddecl.
    def visitStructfielddecl(self, ctx:MiniGoParser.StructfielddeclContext):
        return [ctx.ID().getText(), self.visit(ctx.typedef())]


    # Visit a parse tree produced by MiniGoParser#structliteral.
    def visitStructliteral(self, ctx:MiniGoParser.StructliteralContext):
        nme = ctx.ID().getText()
        struct_fields = ctx.structfieldliteral()
        return StructLiteral(name=nme, elements=[self.visit(i) for i in struct_fields])


    # Visit a parse tree produced by MiniGoParser#structfieldliteral.
    def visitStructfieldliteral(self, ctx:MiniGoParser.StructfieldliteralContext):
        field_name = ctx.ID().getText()
        field_val = self.visit(ctx.getChild(2))
        return [field_name, field_val]


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
        size = ctx.getChildCount()
        if size == 1:
            return Id(ctx.getChild(0).getText())
        else:
            child_list = [ctx.getChild(i) for i in range(1, size)]
            
            def handling_child_list(id, child_lst,cscArr=False,cscField=False,lst=[]):
                if len(child_lst) == 1:
                    child = child_lst[0]
                    if cscArr or lst == []:
                        lst.append(child)
                    if child.getChildCount() == 3:
                        return ArrayCell(arr=str(id),idx=[self.visit(c) for c in lst])
                    else:
                        return FieldAccess(receiver=str(id),field=self.visit(child))
                else:
                    child = child_lst[0]
                    next_child = child_lst[1]
                    lst.append(child)
                    if child.getChildCount() == 3:
                        if next_child.getChildCount() == 3:
                            return handling_child_list(str(id), child_lst[1:], True, False, lst)
                        else:
                            arr_ind = ArrayCell(arr=id,idx=[self.visit(c) for c in lst])
                            return handling_child_list(str(arr_ind), child_lst[1:], lst=[])
                    else:
                        lside = FieldAccess(receiver=str(id),field=self.visit(child))
                        if next_child.getChildCount() == 3:
#                            print(f"handling_child_list({lside}, {[c.getText() for c in child_lst[1:]]})")
                            return handling_child_list(lside, child_lst[1:], lst=[])
                        else:
                            return handling_child_list(lside, child_lst[1:], False, True, lst)

            return handling_child_list(ctx.ID().getText(), child_list)
    
    def visitField_access(self, ctx:MiniGoParser.Field_accessContext):
        return ctx.ID().getText()

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
        name = ctx.ID()
        return FuncCall(funName=name,args=[self.visit(e) for e in ctx.expression()])
        

    # Visit a parse tree produced by MiniGoParser#methodcall.
    def visitMethodcall(self, ctx:MiniGoParser.MethodcallContext):
        if ctx.var_access() != None:
            return MethCall(receiver=self.visit(ctx.var_access()),metName=ctx.ID().getText(),args=[self.visit(e) for e in ctx.expression()])


    # Visit a parse tree produced by MiniGoParser#assignment.
    def visitAssignment(self, ctx:MiniGoParser.AssignmentContext):
        if ctx.ASSIGN_STMT_OP() != None:
            lhs = self.visit(ctx.getChild(0))
            rhs = self.visit(ctx.getChild(2))
            return Assign(lhs, rhs)


    # Visit a parse tree produced by MiniGoParser#expression.
    def visitExpression(self, ctx:MiniGoParser.ExpressionContext):
        childCount = ctx.getChildCount()
        if childCount == 1:
            return self.visit(ctx.getChild(0))
        if childCount == 2:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.getChild(1)))
        if ctx.getChild(0).getText() == '(':
            return self.visit(ctx.getChild(1))
        return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))


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
        if ctx.BOOLEAN() != None:
            return BooleanLiteral(ctx.BOOLEAN())
        if ctx.INTEGER() != None:
            return IntLiteral(ctx.INTEGER())
        if ctx.FLOAT() != None:
            return FloatLiteral(ctx.FLOAT())
        if ctx.STRING() != None:
            text = ctx.STRING().getText()
            return StringLiteral(text)

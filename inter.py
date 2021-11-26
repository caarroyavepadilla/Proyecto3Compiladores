from decafVisitor import decafVisitor

DEFAULT_TYPES = {
    'int': 4,
    'boolean': 1,
    'char': 1,
}


class Inter(decafVisitor):

    def __init__(self, scopes):
        decafVisitor.__init__(self)
        self.tree = None
        self.og_registers = ["r0", "r1", "r2", "r3", "r4", "r5", "r6", "r7"]
        self.registers = self.og_registers[::-1]
        self.line = ""
        self.label = 0
        self.laboratorios = ""
        self.scope_ids = 0
        self.scope_current = ["global"]
        self.scopes = scopes

    def visitProgram(self, ctx):
        self.visitChildren(ctx)
        return 0

    def visitMethodDeclaration(self, ctx):
        name = ctx.ID().getText()
        self.scope_ids += 1
        self.scope_current.append(name)
        start = name + ": \n"
        current = self.scopes[self.scope_current[-1]]
        start += "func begin " + str(current.get_size()) + "\n"
        self.line += start
        self.visitChildren(ctx)
        end = "func end \n"
        self.line += end
        self.scope_current.pop()
        return 0

    def visitSt_return(self, ctx):
        if ctx.expression:
            register = self.visit(ctx.expression())
            self.line += "Return " + str(register) + "\n"
            if register in self.og_registers:
                self.registers.append(register)
        return 0

    def visitMethodCall(self, ctx):
        method = ctx.ID().getText()
        if ctx.arg():
            for arg in ctx.arg():
                param = self.visit(arg)
                self.line += "push param " + str(param) + "\n"
                if param in self.og_registers:
                    self.registers.append(param)
        register = self.registers.pop()
        self.line += register + "=_LCall " + method + "\n"
        if register in self.og_registers:
            self.registers.append(register)
        return 0
    
    def visitEx_par(self, ctx):
        return self.visit(ctx.expression())
    
    def visitWhileScope(self, ctx):
        self.scope_ids += 1
        self.scope_current.append("while" + str(self.scope_ids))
        start_lb = "L" + str(self.label)
        while_line = start_lb + ":\n"
        self.label += 1
        self.line += while_line
        register = self.visit(ctx.expression())
        end_lb = "L" + str(self.label)
        self.label += 1
        while_ct1 = "IfZ " + register + " B " + end_lb + " \n"
        if register in self.og_registers:
            self.registers.append(register)
        self.line += while_ct1
        self.visit(ctx.block())
        while_end = "B " + start_lb + " \n"
        while_end += end_lb + ":\n"
        self.line += while_end
        self.scope_current.pop()
        return 0

    def visitIfScope(self, ctx):
        self.scope_ids += 1
        name = "if" + str(self.scope_ids)
        self.scope_current.append(name)
        register = self.visit(ctx.expression())
        jump = "L" + str(self.label)
        self.label += 1
        if_ln = "IfZ " + register + " B " + jump + "\n"
        if register in self.og_registers:
            self.registers.append(register)
        self.line += if_ln
        self.line += jump + ":\n"
        self.visit(ctx.block1)
        if ctx.block2:
            end_ln = jump + ": \n"
            end = "L" + str(self.label)
            self.line += "B " + end + "\n"
            self.line += end_ln
            self.visit(ctx.block2)
            self.line += end + ": \n"
            self.label += 1
        self.line += self.laboratorios
        self.scope_current.pop()
        return 0
    
    def visitExp_ar_op(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        register = self.registers.pop()
        op = register + " = " + str(left) + " " + ctx.arith_op().getText() + " " + str(right)
        if right in self.og_registers:
            self.registers.append(right)
        if left in self.og_registers:
            self.registers.append(left)
        self.line += op + "\n"
        vaina = self.line
        index = vaina.find("L" + str(self.label - 1) + ":")
        self.laboratorios += vaina[index::]
        self.line = vaina[:index]
        return register
    
    def visitExp_predop(self,ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        register = self.registers.pop()
        op = register + " = " + str(left) + " " + ctx.pred_op().getText() + " " + str(right)
        if right in self.og_registers:
            self.registers.append(right)
        if left in self.og_registers:
            self.registers.append(left)
        self.line += op + "\n"
        return register

    def visitExp_relop(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        register = self.registers.pop()
        op = register + "=" + str(left) + " " + ctx.rel_op().getText() + " " + str(right)
        if right in self.og_registers:
            self.registers.append(right)
        if left in self.og_registers:
            self.registers.append(left)
        self.line += op + "\n"
        return register

    def visitExp_eqop(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        register = self.registers.pop()
        op = register + "=" + str(left) + " " + ctx.eq_op().getText() + " " + str(right)
        if right in self.og_registers:
            self.registers.append(right)
        if left in self.og_registers:
            self.registers.append(left)
        self.line += op + "\n"
        return register

    def visitExp_condop(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        register = self.registers.pop()
        op = register + "=" + str(left) + " " + ctx.cond_op().getText() + str(right)
        if right in self.og_registers:
            self.registers.append(right)
        if left in self.og_registers:
            self.registers.append(left)
        self.line += op + "\n"
        return register
    
    def visitExpr_literal(self, ctx):
        return self.visitChildren(ctx)

    def visitStmnt_equal(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        equal = str(left) + " = " + str(right) + "\n"
        if right in self.og_registers:
            self.registers.append(right)
        self.line += equal
        return left

    def visitLiteral(self,ctx):
        val = self.visitChildren(ctx)
        return val[1]
    
    def visitInt_Literal(self, ctx):
        num = ctx.NUM()
        return("int", (num.getText()))

    def visitChar_Literal(self, ctx):
        char = ctx.CHAR()
        return("char", (char.getText()))
    
    def visitBool_Literal(self,ctx):
        boolean = ctx.getText()
        if boolean == 'true':
            boolean = "1"
        else:
            boolean = "0"
        return ("boolean", boolean)
    
    def visitLocation(self, ctx, parent = None):
        name = ctx.ID().getText()
        offset = 0
        for scope in self.scope_current[::-1]:
            current_scope = self.scopes[scope]
            if symbol := current_scope.get_symbol(name):
                break
        
        for symbol in current_scope.symbols:
            if symbol.name == name:
                break
            else:
                if symbol.type in DEFAULT_TYPES:
                    offset += DEFAULT_TYPES[symbol.type]
                else:
                    offset += current_scope.get_instance_size(symbol.type.replace("struct", "")) * int(symbol.reps)
        if ctx.expression() is not None:
            resp = self.visit(ctx.expression())
            try:
                if symbol.type in DEFAULT_TYPES:
                    offset += DEFAULT_TYPES[symbol.type] * int(ctx.expression().getText())
                else:
                    sym_type = symbol.type.replace("struct", "")
                    offset += current_scope.get_instance_size(sym_type) * int(ctx.expression().getText())
            except:
                register = self.registers.pop()
                if symbol.type in DEFAULT_TYPES:
                    self.line += register + " = " + resp + " * " + str(DEFAULT_TYPES[symbol.type]) + "\n"
                else:
                    sym_type = symbol.type.replace("struct", "")
                    self.line += register + " = " + resp + " * " + str(current_scope.get_instance_size(sym_type)) + "\n"
                offset = register
        sName = current_scope.name + str(current_scope.id)
        value = sName + "[" + str(offset) + "]"
        
        return value

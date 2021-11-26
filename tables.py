import typeSystem as tables
from decafVisitor import decafVisitor

DEFAULT_TYPES = {
    'int': 4,
    'boolean': 4,
    'char': 4,
}


class myDecafVisitor(decafVisitor):

    def __init__(self):
        decafVisitor.__init__(self)
        self.scope_ids = 0
        self.sym_ids = 0
        self.offset = 0
        self.insta_ids = 0
        self.ERRORS = []
        global_scope = tables.Scope()
        self.scopes = [global_scope]
        self.total_scopes = {global_scope.name: global_scope,}

    def visitProgram(self, ctx):
        self.visitChildren(ctx)

        if self.scopes[-1].get_instance("main") is None:
            new_error = tables.Error("Main method not defined", ctx.start.line, ctx.start.column)
            self.ERRORS.append(new_error)
        return 0

    def visitMethodDeclaration(self, ctx):
        method_name = ctx.ID().getText()
        method_type = ctx.methodType().getText()
        self.scope_ids += 1
        n_scope = tables.Scope(self.scope_ids, method_name, self.scopes[-1], method_type)
        self.scopes.append(n_scope)
        params = ctx.parameter()
        p = []
        p_names = []
        for param in params:
            p_type = param.parameterType().getText()
            p_name = param.ID().getText()
            if p_name not in p_names:
                p_names.append(p_name)
                n_param = tables.Symbol(p_type, p_name, 1)
                p.append(n_param)
                self.sym_ids += 1
                size = 0
                if p_type in DEFAULT_TYPES:
                    size += DEFAULT_TYPES[p_type]
                else:
                    explore = p_type.replace("struct", "")
                    for scope in self.scopes[::-1]:
                        exist = scope.get_instance(explore)
                        if exist:
                            if exist.type == "struct":
                                size = exist.size
                                break
                    else:
                        n_error = tables.Error("type " + exist + " not found", ctx.start.line, ctx.start.column)
                        self.ERRORS.append(n_error)
                self.scopes[-1].add_symbol(p_type, p_name, self.sym_ids)
                self.offset += size
            else:
                n_error = tables.Error("param already defined", ctx.start.line, ctx.start.column)
                self.ERRORS.append(n_error)
        x = (ctx.block().statement())
        occurrence = None
        for j in x:
            if 'return' in j.getText():
                break
        else:
            if method_type != "void":
                n_error = tables.Error("return does no t match method type", ctx.start.line, ctx.start.column)
                self.ERRORS.append(n_error)
        if self.scopes[-2].get_instance(method_name):
            n_error = tables.Error("method already defined in scope", ctx.start.line, ctx.start.column)
            self.ERRORS.append(n_error)
        else:
            self.scopes[-2].add_insta(self.insta_ids, method_name, method_type, occurrence, p)
        self.visitChildren(ctx)
        end_scope = self.scopes.pop()
        self.total_scopes[n_scope.name] = end_scope
        return 0

    def visitIfScope(self, ctx):
        val = self.visit(ctx.expression())
        self.scope_ids += 1
        if val != "boolean":
            n_error = tables.Error("expected boolean got other", ctx.start.line, ctx.start.column)
            self.ERRORS.append(n_error)
        n_scope = tables.Scope(self.scope_ids, "if" + str(self.scope_ids), self.scopes[-1])
        self.scopes.append(n_scope)
        self.visitChildren(ctx)
        end = self.scopes.pop()
        self.total_scopes[n_scope.name] = end
        return None

    def visitWhileScope(self, ctx):
        val = self.visit(ctx.expression())
        self.scope_ids += 1
        if val != "boolean":
            n_error = tables.Error("expected boolean got other", ctx.start.line, ctx.start.column)
            self.ERRORS.append(n_error)
        n_scope = tables.Scope(self.scope_ids, "while" + str(self.scope_ids), self.scopes[-1])
        self.scopes.append(n_scope)
        self.visitChildren(ctx)
        end = self.scopes.pop()
        self.total_scopes[n_scope.name] = end
        return None

    def visitSt_return(self, ctx):
        if ctx.expression() != None:
            val = self.visit(ctx.expression())
            for scope in self.scopes[::-1]:
                if scope.type is not None:
                    if val != scope.type:
                        n_error = tables.Error("return " + ctx.expression().getText() + "does not match method type ", ctx.start.line, ctx.start.column)
                        self.ERRORS.append(n_error)
                        break
        else:
            for scope in self.scopes[::-1]:
                if scope.type != None:
                    if "void" != scope.type:
                        n_error = tables.Error("empty return does not match method type", ctx.start.line)
                        self.ERRORS.append(n_error)
                        break
        return None

    def visitBlock(self, ctx):
        self.visitChildren(ctx)
        return None

    def visitLocation(self, ctx, parent=None):
        name = ctx.ID().getText()
        if ctx.expression() is not None:
            val = self.visit(ctx.expression())
            if val != "int":
                n_error = tables.Error("expected int got type" + "instead", ctx.start.line, ctx.start.column)
                self.ERRORS.append(n_error)
        if parent is not None:
            for scope in self.scopes[::-1]:
                sym = scope.get_sub_att(parent, name)
                if sym is not None:
                    if ctx.location() is not None:
                        val = self.visitLocation(ctx.location(), sym.type.replace('struct', ''))
                        return val
                    return sym.type
            else:
                n_error = tables.Error(name + " not found in" + parent, ctx.start.line, ctx.start.column)
                self.ERRORS.append(n_error)
        if ctx.location() is None:
            for scope in self.scopes[::-1]:
                sym = scope.get_symbol(name)
                if sym is not None:
                    sym_type = sym.type
                    return sym_type
            else:
                n_error = tables.Error(name + " not found", ctx.start.line, ctx.start.column)
                self.ERRORS.append(n_error)
        else:
            for scope in self.scopes[::-1]:
                sym = scope.get_symbol(name)
                if sym is not None:
                    sym_type = sym.type
                    if "struct" in sym_type:
                        val = self.visitLocation(ctx.location(), sym_type.replace('struct', ''))
                        return val
                    else:
                        n_error = tables.Error(name + "has no subattributes", ctx.start.line, ctx.start.column)
                        self.ERRORS.append(n_error)
        return None

    def visitStructDeclaration(self, ctx):
        name = ctx.ID().getText()
        type = "struct"
        att = ctx.varDeclaration()
        s_params = []
        size = 0
        s_att_names = []
        for a in att:
            v_type = a.varType().getText()
            v_name = a.ID().getText()
            if v_name not in s_att_names:
                s_att_names.append(v_name)
                s = tables.Symbol(v_type, v_name, id)
                s_params.append(s)
                if v_type in DEFAULT_TYPES:
                    size += DEFAULT_TYPES[v_type]
                else:
                    explore = v_type.replace("struct", "")
                    for scope in self.scopes[::-1]:
                        exist = scope.get_instance(explore)
                        if exist:
                            if exist.type == "struct":
                                size += exist.size
                                break
                    else:
                        n_error = tables.Error("type " + explore + " not found", ctx.start.line, ctx.start.column)
                        self.ERRORS.append(n_error)

            else:
                n_error = tables.Error("Type " + v_name + " already defined in scope", ctx.start.line, ctx.start.column)
                self.ERRORS.append(n_error)

        self.scopes[-1].add_insta(self.insta_ids, name, 'struct', None, s_params, size)
        self.insta_ids += 1
        return type, name

    def visitNormalVar(self, ctx):
        type_var = ctx.varType().getText()
        name = ctx.ID().getText()
        self.sym_ids += 1
        if self.scopes[-1].get_symbol(name):
            n_error = tables.Error('"' + name + '" already defined', ctx.start.line, ctx.start.column)
            self.ERRORS.append(n_error)
        else:
            self.scopes[-1].add_symbol(type_var, name, 1,self.sym_ids, self.offset)
        if type_var in DEFAULT_TYPES:
            self.offset += DEFAULT_TYPES[type_var]
        else:
            explore = type_var.replace("struct", "")
            for scope in self.scopes[::-1]:
                exist = scope.get_instance(explore)
                if exist:
                    if exist.type == "struct":
                        self.offset += exist.size
                        break
            else:
                n_error = tables.Error("type " + exist + " not found", ctx.start.line, ctx.start.column)
                self.ERRORS.append(n_error)
        self.visitChildren(ctx)
        return type_var, name

    def visitArrayVar(self, ctx):
        type_var = ctx.varType().getText()
        name = ctx.ID().getText()
        num = ctx.NUM().getText()
        if int(num) <= 0:
            n_error = tables.Error("array has to have size", ctx.start.line, ctx.start.column)
            self.ERRORS.append(n_error)
        else:
            self.sym_ids += 1
            self.scopes[-1].add_symbol(type_var, name, num, self.sym_ids, self.offset)
            if type_var in DEFAULT_TYPES:
                self.offset += (DEFAULT_TYPES[type_var] * int(num))
            else:
                explore = type_var.replace("struct", "")
                for scope in self.scopes[::-1]:
                    exist = scope.get_instance(explore)
                    if exist:
                        if exist.type == "struct":
                            self.offset += exist.size * int(num)
                            break
                else:
                    n_error = tables.Error("type " + explore + " not found", ctx.start.line, ctx.start.column)
                    self.ERRORS.append(n_error)
        self.visitChildren(ctx)
        return 0

    def visitMethodCall(self, ctx):
        name = ctx.ID().getText()
        args = ctx.arg()
        self.visitChildren(ctx)
        for scope in self.scopes[::-1]:
            method = scope.get_instance(name)
            if method != None:
                if len(args) == len(method.params):
                    current = 0
                    for arg in args:
                        val = self.visit(arg)
                        if val != None and val == method.params[current].type:
                            break
                        elif val != None:
                            n_error = tables.Error(
                                "type of" + val + " " + arg.getText() + " does not match with parameter" +
                                method.params[current].type + " " + method.params[current].name, ctx.start.line,
                                ctx.start.column)
                            self.ERRORS.append(n_error)
                        current += 1
                return method.type
        return None

    def visitStmnt_equal(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        if left is None:
            n_error = tables.Error(ctx.left.getText() + " is none", ctx.start.line, ctx.start.column)
            self.ERRORS.append(n_error)
        elif right is  None:
            n_error = tables.Error(ctx.right.getText() + " is none", ctx.start.line, ctx.start.column)
            self.ERRORS.append(n_error)
        elif left != right:
            n_error = tables.Error("expected same type", ctx.start.line, ctx.start.column)
            self.ERRORS.append(n_error)
        return None

    def visitEx_not(self, ctx):
        val = self.visit(ctx.expression())
        if val == "boolean":
            return val
        else:
            n_error = tables.Error("expected boolean got " + val, ctx.start.line, ctx.start.column)
            self.ERRORS.append(n_error)

    def visitEx_par(self, ctx):
        val = self.visit(ctx.expression())
        return val

    def visitEx_minus(self, ctx):
        val = self.visit(ctx.expression())
        return val

    def visitExp_ar_op(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        if right == "int" and left == "int":
            return "int"
        elif left == None:
            n_error = tables.Error(ctx.left.getText() + " is none", ctx.start.line, ctx.start.column)
            self.ERRORS.append(n_error)
        elif right == None:
            n_error = tables.Error(ctx.right.getText() + " is none", ctx.start.line, ctx.start.column)
            self.ERRORS.append(n_error)
        else:
            n_error = tables.Error("types does not match", ctx.start.line, ctx.start.column)
            self.ERRORS.append(n_error)
        return None

    def visitExp_predop(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        if right == "int" and left == "int":
            return "int"
        elif left == None:
            n_error = tables.Error(ctx.left.getText() + " is none", ctx.start.line, ctx.start.column)
            self.ERRORS.append(n_error)
        elif right == None:
            n_error = tables.Error(ctx.right.getText() + " is none", ctx.start.line, ctx.start.column)
            self.ERRORS.append(n_error)
        else:
            n_error = tables.Error("types does not match", ctx.start.line, ctx.start.column)
            self.ERRORS.append(n_error)
        return None

    def visitExp_relop(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        if right == "int" and left == "int":
            return "boolean"
        elif left == None:
            n_error = tables.Error(ctx.left.getText() + " is none", ctx.start.line, ctx.start.column)
            self.ERRORS.append(n_error)
        elif right == None:
            n_error = tables.Error(ctx.right.getText() + " is none", ctx.start.line, ctx.start.column)
            self.ERRORS.append(n_error)
        else:
            n_error = tables.Error("types does not match", ctx.start.line, ctx.start.column)
            self.ERRORS.append(n_error)
        return None

    def visitExp_eqop(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        if left == right:
            return "boolean"
        elif left == None:
            n_error = tables.Error(ctx.left.getText() + " is none", ctx.start.line, ctx.start.column)
            self.ERRORS.append(n_error)
        elif right == None:
            n_error = tables.Error(ctx.right.getText() + " is none", ctx.start.line, ctx.start.column)
            self.ERRORS.append(n_error)
        else:
            n_error = tables.Error("types does not match", ctx.start.line, ctx.start.column)
            self.ERRORS.append(n_error)
        return None

    def visitExp_condop(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        if right == "boolean" and left == "boolean":
            return "boolean"
        elif left == None:
            n_error = tables.Error(ctx.left.getText() + " is none", ctx.start.line, ctx.start.column)
            self.ERRORS.append(n_error)
        elif right == None:
            n_error = tables.Error(ctx.right.getText() + " is none", ctx.start.line, ctx.start.column)
            self.ERRORS.append(n_error)
        else:
            n_error = tables.Error("types does not match", ctx.start.line, ctx.start.column)
            self.ERRORS.append(n_error)
        return None

    def visitLiteral(self, ctx):
        val = self.visitChildren(ctx)
        return val[0]

    def visitInt_Literal(self, ctx):
        num = ctx.NUM()
        if num == None:
            n_error = tables.Error("expected num", ctx.start.line, ctx.start.column)
            self.ERRORS.append(n_error)
        return "int", int(num.getText())

    def visitChar_Literal(self, ctx):
        char = ctx.CHAR()
        if char is None:
            n_error = tables.Error("expected char", ctx.start.line, ctx.start.column)
            self.ERRORS.append(n_error)
        return "char", char.getText()

    def visitBool_Literal(self, ctx):
        boolean = ctx.getText()
        if boolean != "true" and boolean != "false":
            n_error = tables.Error("expected boolean value", ctx.start.line, ctx.start.column)
            self.ERRORS.append(n_error)
        return "boolean", boolean

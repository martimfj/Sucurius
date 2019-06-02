from symbol_table import SymbolTable

class Number():
    def __init__(self, value):
        self.value = value

    def eval(self, st):
        return int(self.value)

class BinaryOp():
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right

    def eval(self, st):
        right =  self.right.eval(st)
        left = self.left.eval(st)

        if self.operator.gettokentype() == "MINUS":
            return left - right

        elif self.operator.gettokentype() == "PLUS":
            return left + right

        elif self.operator.gettokentype() == "MUL":
            return left * right

        elif self.operator.gettokentype() == "DIV":
            return left // right

        elif self.operator.gettokentype() == "BIGGER":
            return left > right

        elif self.operator.gettokentype() == "SMALLER":
            return left < right

        elif self.operator.gettokentype() == "EQUAL":
            return left == right

        elif self.operator.gettokentype() == "DIFF":
            return left != right  

        elif self.operator.gettokentype() == "AND":
            return left and right

        elif self.operator.gettokentype() == "OR":
            return left or right
        
        else:
            raise ValueError("Error (BinaryOp): {} not supported".format(self.operator.gettokentype()))

class UnaryOp():
    def __init__(self, operator, value):
        self.operator = operator
        self.value = value

    def eval(self, st):
        if self.operator.gettokentype() == "MINUS":
            return - self.value.eval(st)

        elif self.operator.gettokentype() == "PLUS":
            return + self.value.eval(st)

        elif self.operator.gettokentype() == "NOT":
            return not self.value.eval(st)

class Print():
    def __init__(self, value):
        self.value = value

    def eval(self, st):
        print(self.value.eval(st))

class Statements():
    def __init__(self, first_statement):
        self.statements = [first_statement]

    def add_statement(self, statement):
        self.statements.append(statement)

    def eval(self, st):
        for statement in self.statements:
            statement.eval(st)

class IfElse():
    def __init__(self, expression, if_statements, else_statements = None):
        self.expression = expression
        self.if_statements = if_statements
        self.else_statements = else_statements

    def eval(self, st):
        if self.expression.eval(st) == True:
            self.if_statements.eval(st)
        else:
            if self.else_statements is not None:
                self.else_statements.eval(st)

class While():
    def __init__(self, expression, while_statements):
        self.expression = expression
        self.while_statements = while_statements

    def eval(self, st):
        while self.expression.eval(st) == True:
            self.while_statements.eval(st)

class Identifier():
    def __init__(self, identifier):
        self.identifier = identifier

    def eval(self, st):
        return st.getter(self.identifier)

class Assigment():
    def __init__(self, identifier, value):
        self.identifier = identifier
        self.value = value

    def eval(self, st):
        st.setter(self.identifier, self.value.eval(st))

class FuncDec():
    def __init__(self, value, args, func_statements):
        self.value = value
        self.args = args
        self.func_statements = func_statements

    def eval(self, st):
        st.setter(self.value, self)

class FuncCall():
    def __init__(self, value, args):
        self.value = value
        self.args = args

    def eval(self, st):
        new_st = SymbolTable(st)
        decFunc = new_st.getter(self.value)

        if len(decFunc.args) == len(self.args):
            for decVar, callVar in zip(decFunc.args, self.args):
                new_st.setter(decVar.getstr(), callVar.eval(new_st))
        else:
            raise ValueError("AST Error (FuncCall): Expected {} arguments. got {}".format(len(decFunc.args), len(self.args)))

        decFunc.func_statements.eval(new_st)
        return new_st.getter(decFunc.value)

        
    
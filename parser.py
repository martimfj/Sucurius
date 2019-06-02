"""
Based on the example page: https://rply.readthedocs.io/en/latest/users-guide/parsers.html
"""

from rply import ParserGenerator
from ast import *

class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            ['NUMBER', 'PLUS', 'IDENTIFIER', 'MINUS', 'MUL', 'DIV',
            'BIGGER', 'SMALLER', 'EQUAL', 'ASSINGMENT', 'DIFF', 'COMMA', 
            'OPEN_PAREN', 'CLOSE_PAREN', 'OPEN_BRACKET', 'CLOSE_BRACKET',
            'PRINT', 'IF', 'ELSE', 'WHILE', 'FUNC', 'AND', 'OR', 'NOT', 'NEWLINE'
            ],

            precedence=[
            ('left', ['PLUS', 'MINUS']),
            ('left', ['MUL', 'DIV']),
            ('left', ['AND', 'OR']),
            ]
        )

    def parse(self):

        @self.pg.production('program : statements')
        def program(p):
            return p[0]

        @self.pg.production('statements : statement')
        def first_statement(p):
            return Statements(p[0])

        @self.pg.production('statements : statements statement')
        def consecutive_statement(p):
            p[0].add_statement(p[1])
            return p[0]

        @self.pg.production('statement : PRINT OPEN_PAREN relational_expression CLOSE_PAREN NEWLINE')
        def statement_print(p):
            return Print(p[2])

        @self.pg.production('statement : IF OPEN_PAREN relational_expression CLOSE_PAREN OPEN_BRACKET NEWLINE statements CLOSE_BRACKET NEWLINE')
        def statement_if(p):
            return IfElse(p[2], p[6])

        @self.pg.production('statement : IF OPEN_PAREN relational_expression CLOSE_PAREN OPEN_BRACKET NEWLINE statements CLOSE_BRACKET NEWLINE ELSE OPEN_BRACKET NEWLINE statements CLOSE_BRACKET NEWLINE')
        def statement_if_else(p):
            return IfElse(p[2], p[6], p[12])

        @self.pg.production('statement : WHILE OPEN_PAREN relational_expression CLOSE_PAREN OPEN_BRACKET NEWLINE statements CLOSE_BRACKET NEWLINE')
        def statement_while(p):
            return While(p[2], p[6])

        @self.pg.production('statement : IDENTIFIER ASSINGMENT expression NEWLINE')
        def statement_assigment(p):
            return Assigment(p[0].getstr(), p[2])

        @self.pg.production('statement : FUNC IDENTIFIER OPEN_PAREN dec_args CLOSE_PAREN OPEN_BRACKET NEWLINE statements CLOSE_BRACKET NEWLINE')
        def statement_decfunc(p):
            return FuncDec(p[1].getstr(), p[3], p[7])

        @self.pg.production('dec_args : IDENTIFIER COMMA dec_args')
        def dec_func_multiargs(p):
            return p[2] + [p[0]]

        @self.pg.production('dec_args : IDENTIFIER')
        def dec_func_arg(p):
            return [p[0]]

        @self.pg.production('dec_args :')
        def dec_func_emptyargs(p):
            return []

        @self.pg.production('call_args : relational_expression COMMA call_args')
        def call_func_multiargs(p):
            return p[2] + [p[0]]

        @self.pg.production('call_args : relational_expression')
        def call_func_arg(p):
            return [p[0]]

        @self.pg.production('call_args :')
        def call_func_emptyargs(p):
            return []
        
        @self.pg.production('relational_expression : expression BIGGER expression')
        @self.pg.production('relational_expression : expression SMALLER expression')
        @self.pg.production('relational_expression : expression EQUAL expression')
        @self.pg.production('relational_expression : expression DIFF expression')
        def relational_expression(p):
            return BinaryOp(p[1], p[0], p[2])

        @self.pg.production('relational_expression : expression')
        def relational_expression_expression(p):
            return p[0]

        @self.pg.production('expression : term PLUS term')
        @self.pg.production('expression : term MINUS term')
        @self.pg.production('expression : term OR term')
        def expression(p):
            return BinaryOp(p[1], p[0], p[2])

        @self.pg.production('expression : term')
        def expression_term(p):
            return p[0]

        @self.pg.production('term : factor MUL factor')
        @self.pg.production('term : factor DIV factor')
        @self.pg.production('term : factor AND factor')
        def term(p):
            return BinaryOp(p[1], p[0], p[2])

        @self.pg.production('term : factor')
        def term_factor(p):
            return p[0]

        @self.pg.production('factor : NUMBER')
        def factor(p):
            return Number(p[0].getstr())

        @self.pg.production('factor : IDENTIFIER')
        def identifier(p):
            return Identifier(p[0].getstr())

        @self.pg.production('factor : OPEN_PAREN relational_expression CLOSE_PAREN')
        def expression_parens(p):
            return p[1]

        @self.pg.production('factor : PLUS factor')
        @self.pg.production('factor : MINUS factor')
        @self.pg.production('factor : NOT factor')
        def term(p):
            return UnaryOp(p[0], p[1])

        @self.pg.production('factor : IDENTIFIER OPEN_PAREN call_args CLOSE_PAREN')
        def callfunc(p):
            return FuncCall(p[0].getstr(), p[2])

        @self.pg.error
        def error_handle(token):
            raise ValueError("{} not expected. {}".format(token, token.getsourcepos()))

    def get_parser(self):
        return self.pg.build()
"""
Based on the example page: https://rply.readthedocs.io/en/latest/users-guide/lexers.html
"""

from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def addTokens(self):
        self.lexer.add('NUMBER', r'\d+')
        self.lexer.add('PLUS', r'\+')
        self.lexer.add('MINUS', r'-')
        self.lexer.add('MUL', r'\*')
        self.lexer.add('DIV', r'/')

        self.lexer.add('BIGGER', r'\>')
        self.lexer.add('SMALLER', r'\<')
        self.lexer.add('EQUAL', r'==')
        self.lexer.add('ASSINGMENT', r'=')
        self.lexer.add('DIFF', r'\!=')
        self.lexer.add('COMMA', r',')

        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')
        self.lexer.add('OPEN_BRACKET', r'\{')
        self.lexer.add('CLOSE_BRACKET', r'\}')

        self.lexer.add('PRINT', r'imprime')
        self.lexer.add('IF', r'se(?!\w)')
        self.lexer.add('ELSE', r'senao(?!\w)')
        self.lexer.add('WHILE', r'enquanto')
        self.lexer.add('FUNC', r'func(?!\w)')
        self.lexer.add('AND', r'e')
        self.lexer.add('OR', r'ou')
        self.lexer.add('NOT', r'inv')
        self.lexer.add('NEWLINE', r'[\r\n]+')

        # Identifiers comes last, so it does not match other tokens
        self.lexer.add('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*') 
        self.lexer.ignore('[ \t\r\f\v]+') # Ignores whitespace

    def createLexer(self):
        self.addTokens()
        return self.lexer.build()
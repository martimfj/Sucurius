from lexer import Lexer
from parser import Parser
from symbol_table import SymbolTable

string = """price1 = 154
price2 = 352
quantity = 6
flag = 1
se(price1 > price2){
    savings = price1-price2
    imprime(savings)
}
senao{
    savings = (price2-price1)
    imprime(savings)
}
enquanto(flag == 1){
    se(quantity > 0){
        imprime(savings * quantity)
        quantity = quantity - 1
    }
    senao{
        flag = flag + 2
    }    
}
"""

lexer = Lexer().createLexer()
tokens = lexer.lex(string)

st = SymbolTable()
pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval(st)
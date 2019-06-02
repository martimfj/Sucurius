from lexer import Lexer
from parser import Parser
from symbol_table import SymbolTable
import re
import sys

def main():
    try:
        filename = sys.argv[1]
    except IndexError:
        print("Este programa aceita um arquivo .su como entrada. Executando arquivo teste...")
        filename = "test_file.su"

    with open (filename, 'r') as file:
        raw_code = file.read()
    
    # Pre Processing
    code = re.sub("^(\s*(\r\n|\n|\r))", '', re.sub("'.*\n", "\n", raw_code)) + "\n"

    # Lexer
    lexer = Lexer().createLexer()
    tokens = lexer.lex(code)
    
    # Symbol Table
    st = SymbolTable(None)

    # Parser
    parser = Parser()
    parser.parse()
    parser.get_parser().parse(tokens).eval(st)

if __name__ == "__main__":
    main()
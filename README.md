# Sucurius

#Introdução

## EBNF
```
program: { statement };

statement: (assignment | print | if_else | while | commands | funcdef | funccall) "\n";

funcdef: "func" identificador "(" { parameters } ")" "{" {statement} "}";

parameters: ("," expression);

funccall: identificador "(" { parameters } ")";

assignment: identificador "=" expression;

print: "imprime" "(" expression ")";

if_else: "se" "(" rel_exp ")" "{" {statement} "}" ["senao" "{" {statement} "}"];

while: "enquanto" "(" rel_exp ")" "{" {statement} "}";

rel_exp: expression ("==" | ">" | "<") expression;

expression: term { ("+" | "-" | "ou") term };

term: factor { ("*" | "/" | "e") factor };

factor: number | indentifier | ("+", | "-" | "inv") factor | "(" expression ")";

indentifier = letter, { letter | digit | "_" };

letter = "A" | "B" | "C" | "D" | "E" | "F" | "G"
       | "H" | "I" | "J" | "K" | "L" | "M" | "N"
       | "O" | "P" | "Q" | "R" | "S" | "T" | "U"
       | "V" | "W" | "X" | "Y" | "Z" ;

number: digit { digit };

digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;
```

# Sucurius

## Introdução
Este projeto tem como objetivo implementar uma linguagem de programação para brasileiros que desejam começar a programar. Visto que grande parte das linguagens de programação tem sua sintaxe em inglês e que apenas 5.1% da população possui algum conhecimento em inglês*, aprender a programar pode ter uma baixa curva de aprendizado caso inglês seja um limitante.

A proposta da linguagem Sucurius (ou Sucuri), é apresentar aos iniciantes da programação as estruturas básicas de uma linguagem com sintaxe similar a Python, com a adição de chaves para facilitar a identificação de escopo.

*[Estudos do Britsh Council](https://www.britishcouncil.org.br/sites/default/files/demandas_de_aprendizagempesquisacompleta.pdf)

## Recursos
- Variáveis
- Blocos condicionais
- Blocos de repetição (loop)
- Impressão no terminal
- Funções (permite recursão)
- Tipo de variável aceito: Inteiros (True: 1; False: 0)
- Operações: +, -, *, /, e, ou, ==, <, >, inv

## Exemplo
```
func fibo(n){
    se((n < 1) ou (n == 1)){
        fibo = n
    }
    senao{
        fibo = fibo(n - 1) + fibo(n - 2)
    }
}

imprime(fibo(10))
```

## EBNF
```
program: { statement };

statement: (assignment | print | if_else | while | commands | func_def) "\n";

func_def: "func" indentifier "(" dec_args ")" "{" {statement} "}";

dec_args: ( indentifier {"," indentifier} );

func_call: indentifier "(" call_args ")";

call_args: ( rel_exp {"," rel_exp} );

assignment: indentifier "=" expression;

print: "imprime" "(" rel_exp ")";

if_else: "se" "(" rel_exp ")" "{" {statement} "}" ["senao" "{" {statement} "}"];

while: "enquanto" "(" rel_exp ")" "{" {statement} "}";

rel_exp: expression ("==" | ">" | "<") expression;

expression: term { ("+" | "-" | "ou") term };

term: factor { ("*" | "/" | "e") factor };

factor: number | indentifier | ("+", | "-" | "inv") factor | "(" expression ")" | func_call;

indentifier = letter, { letter | digit | "_" };

letter = "A" | "B" | "C" | "D" | "E" | "F" | "G"
       | "H" | "I" | "J" | "K" | "L" | "M" | "N"
       | "O" | "P" | "Q" | "R" | "S" | "T" | "U"
       | "V" | "W" | "X" | "Y" | "Z" ;

number: digit { digit };

digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;
```

## Como utilizar
Para conseguir executar este projeto é necessário ter:
- Python 3.6 ou superior (Pacote Anaconda é recomendado)
- Biblioteca rply instalada (pip install rply)

Escreva seu código em um arquivo .su e passe como argumento na execução do arquivo `main.py`:
```
python main.py programa_fibo.su
```

Caso não seja passado um arquivo como argumento, o programa executará o arquivo `test_file.su` por padrão.
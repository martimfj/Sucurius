# Sucurius

## EBNF
```
letra = "A" | "B" | "C" | "D" | "E" | "F" | "G"
       | "H" | "I" | "J" | "K" | "L" | "M" | "N"
       | "O" | "P" | "Q" | "R" | "S" | "T" | "U"
       | "V" | "W" | "X" | "Y" | "Z" ;

digito = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;

numero = digito, { digito };
identificador = letra, { letra | digito };

funcao = "definir", identificador, "(", ")", comandos;
comandos = "{", { comando }, "}";
comando = variavel | imprimir | condicional | enquanto | funcao | chama_funcao;
chama_funcao = identificador, "(", {argumentos}, ")";
argumentos = { numero | variavel };

variavel = identificador , "=" , expressao;
expressao = termo, { ( "+" | "-" ), termo };
termo = fator, { ( "*" | "/" ), fator };
fator = identificador | ( ( "+" | "-" ), fator ) | numero | ( "(", expressao, ")" );

imprimir = "imprime", "(", expressao, ")";
condicional = "se", "(", expressao_boleana, ")", comandos;
loop = "enquanto", "(", expressao_boleana, ")", comandos;
expressao_boleana = termo_boleana, { ( "ou" | "e" ), termo_boleana };
termo_boleana = expressao, { ( "==" | "<" | ">" ), expressao }
```

#### Dúvidas:
- Como implementar o EBNF do `else`.
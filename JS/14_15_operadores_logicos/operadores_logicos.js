/* Operdaores logicos: &&(and), retorna true apenas se as 
duas expressoes retornarem true */

var numero = 8;
var numero_2 = 9;

if (numero == 8 && numero_2 == 9){
    console.log("testando operadores logicos");
}

/* a sintaxe também pode ser:

    if((priorizar um calculo)){
        console.log()
    }
*/

/* Operador logico: ||(or), ele retorna true caso uma das
operacoes retorne verdadeiro 

Dependendo da posição do && e || o resultado muda

*/

var nome = "Bruna";
var idade = 18;

if (nome === "Kayo" && idade === 18){
    console.log("testando 1!");
}

else if(nome === "Bruna" || idade !== 17){
    console.log("Testando 2");
}




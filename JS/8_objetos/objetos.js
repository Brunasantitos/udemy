//objeto: {} determina a sintaxe de um objeto, e suas propriedades ficam dentro das {}

var obj = {
    nome: "Bruna",
    idade: 14,
    cursada: true
};

console.log(obj);

//para acessar apenas a propriedade, basta

console.log(obj.nome);
console.log(obj.idade);

//para mudar o valor de uma propriedade:

obj.nome = "Kayo";
console.log(obj.nome);

//criar objeto:

obj.graduacao = false;

console.log(obj);

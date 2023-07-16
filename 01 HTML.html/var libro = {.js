var libro= { 
    titulo: 'las legiones Malditas',
    autor: 'Santiago Posteguillo', 
    informacion:function (){return this.titulo + "escrito por" + this.autor;}
}
console.log(typeof libro.informacion);

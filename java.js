var a=true;
console.log(typeof(a)); // boolean
var b="sree"
console.log(typeof(b)); // string
var c=5;
var d=b+c;
console.log(d);
c++;
console.log(c);
function add(a,b){
    console.log("area"+" "+(a+b));
}
var a=23;
var b=34;
add(a,b);
if(a>b){
    console.log("true");
}
else{
    console.log("false");
}
let x="red";
if(x=="red"||x=="yellow"||x=="green"){
    console.log("true");
}
else{
    console.log("false");
}
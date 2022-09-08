//-------------------------------------------------->
//1 fullname()
function fullName(){
    console.log('Ron Hearn')
}
fullName()
//-------------------------------------------------->
//2
function fullerName(first, last){
    console.log(first + " " + last)
}
fullerName('ron', 'hearn')
console.log('---------------------------------')
//-------------------------------------------------->
//3
function sum(a, b){
    let total = a + b
    console.log(total)
}
sum(100,20)
console.log('---------------------------------')
//-------------------------------------------------->
//4
function perimiter(l,w){
    let perim = l + l + w + w
    console.log(perim)
}
perimiter(40,30)
console.log('---------------------------------')
//-------------------------------------------------->
//5
const area = (l,w) => l * w
console.log(area(100,40))

console.log('---------------------------------')
//-------------------------------------------------->
//6
const volOfRecPrism = (l, w, h) =>  l * w * h
console.log(volOfRecPrism(5,2,8))
console.log('---------------------------------')
//-------------------------------------------------->
//7
const areaCircle = (r, pi = 3.143) => pi * r * r
console.log(areaCircle(20))
console.log('---------------------------------')
//-------------------------------------------------->
//8
const circumOfCircle = (r , pi = 3.143) => 2 * pi * r
console.log(circumOfCircle(44))
console.log('---------------------------------')
//-------------------------------------------------->
//9
const density = (mass, volume) => mass / volume
console.log(density(40,20))
console.log('---------------------------------')
//-------------------------------------------------->
//10
const speed = (td, tt) => td / tt
console.log(speed(300, 2))
console.log('---------------------------------')
//-------------------------------------------------->
//11
const weight = (mass, gravity = 9.81) => mass * gravity
console.log(weight(100))

console.log('---------------------------------')
//-------------------------------------------------->
//12
const convertCelToFahren = (c) => (c * 9 / 5) + 32
console.log(convertCelToFahren(100))
console.log('---------------------------------')
//-------------------------------------------------->
//13
const bmi = (w, h) => w / (h * h)
let bmiNum = bmi(113,1.75)
if (bmiNum > 30){
    console.log('OBESE')

}else if (bmiNum > 24.28){
    console.log('OVERWEIGHT')

}else if (bmiNum > 18.4){
    console.log('NORMAL WEIGHT')
}else{
    console.log('UNDERWEIGHT')
}
console.log('---------------------------------')

//-------------------------------------------------->
//14
const checkSeason = (month) => {
    if (month.toLowerCase() == "january" || month.toLowerCase() == 'february' || month.toLowerCase() == 'december'){
        return 'Winter'
    
    }else if (month.toLowerCase() == 'march' || month.toLowerCase() == 'april' || month.toLowerCase() == 'may'){
        return 'Sping'
    }else if (month.toLowerCase() == 'june' || month.toLowerCase() == 'july' || month.toLowerCase() == 'august'){
        return 'Summer'
    }else {
        return 'Autumn'
    }
}
console.log(checkSeason('november'))

console.log('---------------------------------')
//-------------------------------------------------->
//15
const maxFinder = (x, y, z) => {
    if( x > y){
        if (x > z){
            return x
        }
    }else if (y > z){
        return y
    }else{
        return z
    }
}
console.log(maxFinder(3770,2320,1002))

console.log('---------------------------------')
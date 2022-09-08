//-------------------------------------------------->
//1
const solveLinearEquation = (a, b, c) => {
    let k = 0
    let arr = [-1,-1]
    while(k <= c/a && (c - a*k)% b != 0){
        k++
    }
    if ((c-a*k)%b == 0){
        arr[0] = k
        arr[1] = (c-a*k) / b
        if(arr[0] < 0 || arr[1] < 0){
            arr[1] = -1
            arr[0] = -1
        }
    }
    return arr
}
console.log(solveLinearEquation(6,7,7))
console.log('---------------------------------')
//-------------------------------------------------->
//2
const quadratic = (a, b, c) => {
    let lowerLimit = (-1 * b - Math.sqrt(Math.pow(b, 2) - (4 * a * c))) / (2 * a)
    let upperLimit = (-1 * b + Math.sqrt(Math.pow(b, 2) - (4 * a * c))) / (2 * a)
    return `{${upperLimit}, ${lowerLimit}}`
}

console.log(quadratic(1, -1, 0));
console.log('---------------------------------')
//-------------------------------------------------->
//3
const arrPrinter = (arr) => {
    for (ele of arr){
        console.log(ele)
    }
}
arrPrinter([2,3,4,5])
console.log('---------------------------------')
//-------------------------------------------------->
//4
let showDate = new Date()
console.log('0'+showDate.getMonth()+"/0"+ showDate.getDate()+"/"+showDate.getFullYear() +"/ 0"+showDate.getHours()+":"+ showDate.getMinutes())

console.log('---------------------------------')
//-------------------------------------------------->
//5
const swapVal = (x, y) =>{
    let hold = x;
    x= y
    y = hold
    return `x = ${x} and y = ${y}`
}
console.log(swapVal(10,60))

console.log('---------------------------------')
//-------------------------------------------------->
//6
const reverseArry = (arr) =>{
    let revArr = []
    for (el of arr){
        revArr.unshift(el)
    }
    return revArr
}
console.log(reverseArry([1,2,3,4,5,6,7,8]))
console.log('---------------------------------')
//-------------------------------------------------->
//7
const capArry = (arr) =>{
    let capArr = []
    for (el of arr){
        capArr.push(el.toUpperCase())
    }
    return capArr
}
console.log(capArry(['a','s','d','f','g','h']))
console.log('---------------------------------')
//-------------------------------------------------->
//8
let arrAdd = [1,2,3,4,5,6]
const addItem = (item) => {
    arrAdd.push(item)
    return arrAdd
}

console.log(addItem(7))
console.log('---------------------------------')
//-------------------------------------------------->
//9
let rArr = ['one','two','three','four','five']
const removeItem = (index) =>{
    rArr.splice(index, 1)
    return rArr
}
console.log(removeItem(2))
console.log('---------------------------------')
//-------------------------------------------------->
//10
const sumOfNumbers = (num) => num + num+1 +num-1
console.log(sumOfNumbers(10))
console.log('---------------------------------')
//-------------------------------------------------->
//11
const sumOfOdd = (num) => num + num+1 +num-1
console.log(sumOfOdd(10))
console.log('---------------------------------')
//-------------------------------------------------->
//12
const sumOfEven = (num) => num + num+1 +num-1
console.log(sumOfEven(10))

console.log('---------------------------------')
//-------------------------------------------------->
//13
const evensAndOdds = (num) =>{
    let even = num / 2
    let odd = num / 2
    return `odd = ${odd} & even = ${even}`
}
console.log(evensAndOdds(10))
console.log('---------------------------------')
//-------------------------------------------------->
//14
const sumAll = (...args) =>{
    let tot =0
        for (el of args){
            tot += Number(el)

        }
    return tot
}
console.log(sumAll(1,2,3,4,5,6))
console.log('---------------------------------')
//-------------------------------------------------->
//5
const randomUserIp = () =>{
    let first = Math.floor(Math.random()* 200)
    let second = Math.floor(Math.random()* 200)
    let thrid = Math.floor(Math.random()* 2)
    let fourth =Math.floor(Math.random()* 2)
    return `${first}.${second}.${thrid}.${fourth}`
}
console.log(randomUserIp())
console.log('---------------------------------')
//-------------------------------------------------->
//1
console.log('---------------------------------')
//-------------------------------------------------->
//1
console.log('---------------------------------')
//-------------------------------------------------->
//1
console.log('---------------------------------')

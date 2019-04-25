// 1급 객체란
// 1. 인자로 넘길 수 있어야 한다.
// 2. 변수나 데이터에 할당할 수 있어야 한다.
// 3. 객체의 리턴값으로 리턴할 수 있어야 한다.

// 사용할 배열
const numbers = [4,5,6]


// 숫자로 된 배열을 받아서 모두 더한다
const numbersAddEach = (numbers) => {
    let sum = 0
    for (const number of numbers) {
        sum += number
    }
    return sum
}

// 숫자로 된 배열을 받아서 모두 뺀다.
const numbersSubEach = (numbers) => {
    let sum = 0
    for (const number of numbers) {
        sum -= number
    }
    return sum
}

// 숫자로 된 배열을 받아서 모두 곱한다.
const numbersMulEach = (numbers) => {
    let sum = 1
    for (const number of numbers) {
        sum *= number
    }
    return sum
}

numbersMulEach(numbers) // 곱하기 해줌

const numbersEach = (numbers, callback) => {
    for (const number of numbers) {
        callback(number)
    }
}

numbersEach(numbers, (number) => {
    console.log('numbersEach', number) // 4, 5, 6
})

let sum = 0

numbersEach(numbers, (number) => {
    sum += number
})

// ES6 이후로 도입된 Array Helper Method
numbers.forEach((number) => {
    sum += number
})

console.log(sum)
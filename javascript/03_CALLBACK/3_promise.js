// 다 만들면 커피를 줄게라는 약속을 함
// 중간에 무슨일이 생기면 알려줌

/*
// 두 함수가 같음
const sum = (a, b) => {
    return a + b
}

const sum = (a, b) => a + b
*/

// resolve에 성공시 넘겨줄 객체
// reject에 무슨일이 생길시 발생기킬 에러를 담음
const orderCoffee = (order) => new Promise((resolve, reject) => {
    let coffee

    setTimeout(() => {
        if (order === undefined) {
            reject('손님 주문 안하셨는데요;')
        }
        // 다 만들면 coffee를 넘겨줌
        coffee = order
        resolve(coffee)
    }, 1000);
})

// orderCoffee()
orderCoffee('Americano')
    .then((coffee) => { // 그리고, 함수를 실행시키고 나서
        console.log(`${coffee} 잘 마실게요!`)
    })
    .catch((error) => { // reject시에 출력할 에러를 catch함
        console.log(error)
    })

orderCoffee('Americano')
    .then((coffee) => {
        console.log(coffee)
        return orderCoffee('Latte')
    })
    .then((coffee) => {
        console.log(coffee) // Latte
        // Promise >> undefined
    })
    .then((coffee) => {
        console.log(coffee) // undefined
    })
    .catch((error) => {
        console.log(error)
    })

const XHR = new XMLHttpRequest()
const URL = 'http://koreanjson.com/posts/1'

XHR.open('GET', URL)
XHR.send()

XHR.addEventListener('load', (event) => {
    const rawData = event.target.response
    const parseData = JSON.parse(rawData)
    console.log(parseData)
})

fetch(URL) // URL로부터 응답을 받아오고, 
    .then((response) => response.json()) // 응답 결과를 object로 parsing
    .then((object) => console.log(object))
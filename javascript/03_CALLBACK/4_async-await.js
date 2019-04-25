const orderCoffee = (order) => new Promise((resolve, reject) => {
    let coffee

    setTimeout(() => {
        if (order === undefined) {
            reject('손님 주문 안하셨는데요;')
        }
        coffee = order
        resolve(coffee)
    }, 1000);
})

const getCoffee = async () => {
    const coffee = await orderCoffee('Americano')
    console.log(coffee) // Americano
}

getCoffee()


const getData = async () => {
    const URL = 'https://koreanjson.com/posts/1'
    const response = await fetch(URL) // 데이터를 불러오겠다.
    const data = await response.json() // 파싱한다
    console.log(data)
}

getData()
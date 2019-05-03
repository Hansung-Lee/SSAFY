function def1 () {
    // this: 실행시점의 객체를 바라본다.
}

const def2 = () => {
    // this: 선언 시점의 객체를 바라본다.
}

// callback 함수는 전역객체(windows)에서 실행된다

document.querySelector
window.document.querySelector
alert
window.alert

var number = 123
window.number // 123

const number2 = 123
window.number2 // undefined
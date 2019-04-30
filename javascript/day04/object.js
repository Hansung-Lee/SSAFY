// 사람 (in Python)
/*
class Person():
    def __init__(self, name):
        self.name = name
human = Person('john')
*/

human1 = {
    name: '홍길동',

    greet() {
        return `안녕 나는 ${this.name}이야`
    }
}

human2 = {
    name: '유재석',

    greet: function () {
        return `안녕 나는 ${this.name}이야`
    }
}

console.log(human1.name)
console.log(human1.greet())

console.log(human2.name)
console.log(human2.greet())


class Person {
    constructor(name) {
        this.name = name
    }
    greet() {
        return `안녕 나는 ${this.name}이야`
    }
}

const human3 = new Person('이순신')

console.log(human3.name)
console.log(human3.greet())
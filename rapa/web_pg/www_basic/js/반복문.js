const todos = ['출근', '고객미팅', 'js수강', '탁구']
for (let i in todos){
console.log(`${i}번째 할일 : ${todos[todos.length-1-i]}`)
}

const todos1 = ['출근', '고객미팅', 'js수강', '탁구']
for (const todo of todos1){
console.log(`오늘 할 일 : ${todo}`)
}

for (let i = 0; i < 5; i++) {
    console.log(`${i}번째 반복입니다.`)
    }

let output = 0
for (let i=1; i<=100; i++){
    output +=i
}
// console.log(`${i}번째 할일`)
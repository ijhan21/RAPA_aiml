const num =10
let array = []
for (let i=0; i<num;i++){
    let output = ""
    for (let j=0; j<num-i;j++){
        output +=' . '
        }
    for (let j=0; j<=2*i;j++){
    output +=' 8 '
    }
    for (let j=0; j<num-i;j++){
        output +=' . '
        }
    console.log(output)
    array.push(output)
}
for (ar in array){
    if (ar==0){ continue}
    console.log(array[array.length-1-ar])
}

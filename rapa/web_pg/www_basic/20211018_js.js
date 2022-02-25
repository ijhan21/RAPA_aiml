// selection sort

// 선택정렬
// for(let i=0;i<arr.length;i++){
//     tmp = i
//     for(let j=i+1; j<arr.length;j++){
//         if(arr[tmp]>arr[j]){
//             [arr[tmp],arr[j]]=[arr[j],arr[tmp]]
//         }
//     }
// }
// console.log(arr)

// 버블 정렬
arr = [1,3,11,6,10,75,121,4,4]

for(let i=0;i<arr.length-1;i++){
    for(let j=1;j<arr.length-i;j++){
        if(arr[j-1]>arr[j]){
            [arr[j-1],arr[j]] = [arr[j],arr[j-1]] 
        }
    }
}
console.log(arr)
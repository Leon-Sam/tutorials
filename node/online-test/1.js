
function solution(A) {
  //Written for Node.js 8.9.4 runtime
  //Function: Given an array of integers, return the smallest postive integer that doesn't occur in the array

  let dict={};
  let result=1 //Initialize to 1, incase no suitable result is found

  //Place each element into hashmap
  A.forEach(element => {
     dict[element]=true;
  });

  //Iterate through newly created hashmap
  for (let i=1;i<=1000000;i++){
    //If a value isn't found in in the hashmap, then set as result and break the loop
    if(!dict[i]){
      result=i
      break;
    }
  }
  return result
}


let A=[1,2,3]; //4
let B=[1, 3, 6, 4, 1, 2]; //5
let C=[-1, -3] //1

console.log("A",solution(A))
console.log("B",solution(B))
console.log("C",solution(C))



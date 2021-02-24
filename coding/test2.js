var solution = function (N) {
    let max = Number.MIN_SAFE_INTEGER;
    for (let i = N >= 0 ? 0 : 1; i < `${N}`.length + 1; i++) {
      const result = [`${N}`.slice(0, i), '5', `${N}`.slice(i)].join('');
      //console.log(result);
      if (Number(result) > max) {
        max = Number(result);
      }
    }
    return max;
  };

console.log(solution(268)); //5268
console.log(solution(670)); //6750
console.log(solution(0)); //50
console.log(solution(-999)); //-5999
console.log(solution(945)); //9545
console.log(solution(439)); //5439
console.log(solution(-945)); //-5945
console.log(solution(-439)); //-4359
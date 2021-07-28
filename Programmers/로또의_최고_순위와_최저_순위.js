function solution(lottos, win_nums) {
  let answer = [];
  let cnt = 0;
  const rank = [6,6,5,4,3,2,1];
  let x = lottos.filter(element => 0 == element).length;
  for (let step = 0; step < lottos.length; step++) {
      for (let i = 0; i < lottos.length; i++){
          if (lottos[i] == win_nums[step]) {
              cnt += 1;
          }
      }
  };
  answer.push(rank[cnt+x],rank[cnt]);

  return answer;
}
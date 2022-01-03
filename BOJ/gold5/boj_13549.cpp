// 13549. 숨바꼭질 3
#include <bits/stdc++.h>
using namespace std;
#define MAX 100001
int n, k;
int visited[MAX];

// 2씩 곱해서 순간이동하면서 처음 방문하는곳 q에 삽입
void teleport(int x, queue<int> &q)
{
  // 0일때 처리 안해주면 무한루프로 시간초과
  if (x == 0)
    return;
  int temp = x;
  while (temp < MAX)
  {
    if (visited[temp] == 0)
    {
      visited[temp] = visited[x];
      q.push(temp);
    }
    if (temp == k)
      return;
    temp *= 2;
  }
}
int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> n >> k;
  if (n > k)
  {
    cout << n - k << "\n";
    return 0;
  }
  queue<int> q;
  q.push(n);
  visited[n] = 1;
  teleport(n, q); // 순간이동 가능한곳 큐에 삽입
  while (visited[k] == 0)
  {
    int cur = q.front();
    q.pop();
    if (cur == k)
      break;
    for (int nxt : {cur + 1, cur - 1})
    {
      if (nxt < 0 || nxt >= MAX || (visited[nxt] > 0))
        continue;
      visited[nxt] = visited[cur] + 1;
      q.push(nxt);
      teleport(nxt, q);
    }
  }
  cout << visited[k] - 1 << "\n";
}
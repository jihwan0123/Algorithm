// 1697. 숨바꼭질
#include <bits/stdc++.h>
using namespace std;
int visited[100001];
int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n, k;
  cin >> n >> k;
  visited[n] = 1;
  queue<int> q;
  q.push(n);
  while (true)
  {
    int x = q.front();
    q.pop();
    if (x == k)
    {
      cout << visited[k] - 1 << "\n";
      return 0;
    }
    for (int nx : {x - 1, x + 1, x * 2})
    {
      if (0 <= nx && nx < 100001 && visited[nx] == 0)
      {
        visited[nx] = visited[x] + 1;
        q.push(nx);
      }
    }
  }
}
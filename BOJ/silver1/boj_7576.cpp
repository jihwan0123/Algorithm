// 7576. 토마토
#include <bits/stdc++.h>
using namespace std;
int n, m;
int board[1001][1001];
int visited[1001][1001];
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};
void bfs(queue<pair<int, int>> &q)
{
  while (!q.empty())
  {
    int x = q.front().first;
    int y = q.front().second;
    q.pop();
    for (int i = 0; i < 4; i++)
    {
      int nx = x + dx[i];
      int ny = y + dy[i];
      if (visited[nx][ny] >= 0)
        continue;
      if (1 <= nx && nx <= n && 1 <= ny && ny <= m)
      {
        visited[nx][ny] = visited[x][y] + 1;
        q.push({nx, ny});
      }
    }
  }
}
int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> m >> n;
  queue<pair<int, int>> q;
  for (int i = 1; i <= n; i++)
    for (int j = 1; j <= m; j++)
    {
      cin >> board[i][j];
      // 익은 토마토 큐에 저장
      if (board[i][j] == 1)
        q.push({i, j});
      // 안익은 토마토 -1로 변경
      if (board[i][j] == 0)
        visited[i][j] = -1;
    }
  // 익은 토마토들로부터 bfs
  bfs(q);

  int ans = 0;
  for (int i = 1; i <= n; i++)
    for (int j = 1; j <= m; j++)
    {
      // 안익은 토마토가 남아있으면
      if (visited[i][j] == -1)
      {
        cout << -1 << "\n";
        return 0;
      }
      ans = max(ans, visited[i][j]);
    }

  cout << ans << "\n";
}
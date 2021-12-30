// 1926. 그림
#include <bits/stdc++.h>
using namespace std;
int board[501][501];
bool vis[501][501];
int n, m;
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};
int bfs(int a, int b)
{
  int ret = 0;
  queue<pair<int, int>> q;
  q.push({a, b});
  vis[a][b] = true;
  while (!q.empty())
  {
    int x = q.front().first;
    int y = q.front().second;
    q.pop();
    ret++;
    for (int i = 0; i < 4; i++)
    {
      int nx = x + dx[i];
      int ny = y + dy[i];
      if (1 <= nx && nx <= m && 1 <= ny && ny <= n && !vis[nx][ny] && board[nx][ny] == 1)
      {
        vis[nx][ny] = true;
        q.push({nx, ny});
      }
    }
  }
  return ret;
}
int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> n >> m;
  int paint_cnt = 0;
  int paint_size = 0;
  vector<pair<int, int>> paints;
  for (int i = 1; i <= n; i++)
    for (int j = 1; j <= m; j++)
    {
      cin >> board[j][i];
      if (board[j][i] == 1)
        paints.push_back({j, i});
    }
  for (auto paint : paints)
  {
    int x = paint.first;
    int y = paint.second;
    if (vis[x][y])
      continue;
    int z = bfs(x, y);
    paint_cnt++;
    paint_size = max(paint_size, z);
  }
  cout << paint_cnt << "\n"
       << paint_size << "\n";
}
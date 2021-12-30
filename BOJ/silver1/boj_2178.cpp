// 2178. 미로 탐색
#include <bits/stdc++.h>
using namespace std;
int n, m;
int board[101][101];
int visted[101][101];
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};
int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> n >> m;
  string s;
  for (int i = 1; i <= n; i++)
  {
    cin >> s;
    for (int j = 1; j <= m; j++)
      board[j][i] = s[j - 1] - '0';
  }

  // BFS
  queue<pair<int, int>> q;
  q.push({1, 1});
  visted[1][1] = 1;
  while (!q.empty())
  {
    int x = q.front().first;
    int y = q.front().second;
    q.pop();
    for (int i = 0; i < 4; i++)
    {
      int nx = x + dx[i];
      int ny = y + dy[i];
      if (1 <= nx && nx <= m && 1 <= ny && ny <= n)
      {
        if ((visted[nx][ny] == 0) && (board[nx][ny] == 1))
        {
          visted[nx][ny] = visted[x][y] + 1;
          q.push({nx, ny});
        }
      }
    }
  }
  cout << visted[m][n] << "\n";
}
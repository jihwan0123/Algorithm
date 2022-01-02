// 1600. 말이 되고픈 원숭이
#include <bits/stdc++.h>
using namespace std;
#define MAX 40001
int board[201][201];
int visited[201][201][31];
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};
int horse_x[8] = {1, 2, 2, 1, -1, -2, -2, -1};
int horse_y[8] = {2, 1, -1, -2, -2, -1, 1, 2};
int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  int k, w, h;
  int ans = MAX;
  cin >> k >> w >> h;

  // 입력 주의
  for (int i = 1; i <= h; i++)
    for (int j = 1; j <= w; j++)
      cin >> board[j][i];

  // 1*1이면 0번 이동
  if (w == 1 && h == 1)
  {
    cout << 0 << "\n";
    return 0;
  }

  // BFS
  queue<tuple<int, int, int>> q;
  q.push({1, 1, 0});
  visited[1][1][0] = 1;
  while (!q.empty())
  {
    int x = get<0>(q.front());
    int y = get<1>(q.front());
    int z = get<2>(q.front()); // 나이트 이동 횟수
    q.pop();
    // 나이트 이동 가능하면 이동
    if (z < k)
    {
      for (int i = 0; i < 8; i++)
      {
        int nx = x + horse_x[i];
        int ny = y + horse_y[i];
        if (nx < 1 || nx > w || ny < 1 || ny > h)
          continue;
        if ((board[nx][ny] == 1) || (visited[nx][ny][z + 1] >= 1))
          continue;
        visited[nx][ny][z + 1] = visited[x][y][z] + 1;
        q.push({nx, ny, z + 1});
        if (nx == w && ny == h)
          ans = min(ans, visited[x][y][z]);
      }
    }
    // 나이트 이동 x
    for (int i = 0; i < 4; i++)
    {
      int nx = x + dx[i];
      int ny = y + dy[i];
      if (nx < 1 || nx > w || ny < 1 || ny > h)
        continue;
      if ((board[nx][ny] == 1) || (visited[nx][ny][z] >= 1))
        continue;
      visited[nx][ny][z] = visited[x][y][z] + 1;
      q.push({nx, ny, z});
      if (nx == w && ny == h)
        ans = min(ans, visited[x][y][z]);
    }
  }
  cout << (ans == MAX ? -1 : ans) << "\n";
}
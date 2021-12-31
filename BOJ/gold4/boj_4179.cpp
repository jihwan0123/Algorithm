// 4179. 불!
#include <bits/stdc++.h>
using namespace std;
int r, c;
char maze[1002][1002];        // 미로
int visited_fire[1002][1002]; // 불
int visited[1002][1002];      // 지훈
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
      if (1 <= nx && nx <= r && 1 <= ny && ny <= c && visited_fire[nx][ny] == 0 && maze[nx][ny] != '#')
      {
        visited_fire[nx][ny] = visited_fire[x][y] + 1;
        q.push({nx, ny});
      }
    }
  }
}
int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> r >> c;
  queue<pair<int, int>> fires;
  queue<pair<int, int>> jihoon;
  for (int i = 1; i <= r; i++)
  {
    for (int j = 1; j <= c; j++)
    {
      cin >> maze[i][j];
      // 지훈 시작지점
      if (maze[i][j] == 'J')
      {
        jihoon.push({i, j});
        visited[i][j] = 1;
        if (i == 1 || i == r || j == 1 || j == c)
        {
          cout << 1;
          return 0;
        }
      }
      // 불이 난 지점
      if (maze[i][j] == 'F')
      {
        fires.push({i, j});
        visited_fire[i][j] = 1;
      }
    }
  }

  // 불 BFS
  bfs(fires);
  // 지훈 BFS
  while (!jihoon.empty())
  {
    int x = jihoon.front().first;
    int y = jihoon.front().second;
    jihoon.pop();
    for (int i = 0; i < 4; i++)
    {
      int nx = x + dx[i];
      int ny = y + dy[i];
      // 불보다 먼저 이동할 수 있으면 이동
      if (1 <= nx && nx <= r && 1 <= ny && ny <= c && visited[nx][ny] == 0 && maze[nx][ny] != '#')
      {
        // visited_fire가 0인 경우에도 이동할 수 있도록 뒤에 && 조건 추가
        if ((visited[x][y] + 1 >= visited_fire[nx][ny]) && (visited_fire[nx][ny] >= 1))
          continue;
        jihoon.push({nx, ny});
        visited[nx][ny] = visited[x][y] + 1;
        // 가장자리 왔으면 종료
        if (nx == 1 || nx == r || ny == 1 || ny == c)
        {
          cout << visited[nx][ny] << "\n";
          return 0;
        }
      }
    }
  }
  cout << "IMPOSSIBLE\n";
}
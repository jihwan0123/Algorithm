// 5427. 불
#include <bits/stdc++.h>
using namespace std;
int t, w, h;
char board[1002][1002];       // 미로
int visited_fire[1002][1002]; // 불
int visited[1002][1002];      // 상근
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};
void run()
{
  bool chk = false;
  cin >> h >> w;
  queue<pair<int, int>> fires;
  queue<pair<int, int>> sanggeun;

  for (int i = 1; i <= w; i++)
    for (int j = 1; j <= h; j++)
    {
      board[i][j] = 0;
      visited[i][j] = 0;
      visited_fire[i][j] = 0;
    }

  for (int i = 1; i <= w; i++)
  {
    for (int j = 1; j <= h; j++)
    {
      cin >> board[i][j];
      if (board[i][j] == '@')
      {
        sanggeun.push({i, j});
        visited[i][j] = 1;
        if (i == 1 || i == w || j == 1 || j == h)
        {
          cout << 1 << "\n";
          chk = true;
        }
      }
      if (board[i][j] == '*')
      {
        fires.push({i, j});
        visited_fire[i][j] = 1;
      }
    }
  }
  if (chk)
    return;

  while (!fires.empty())
  {
    int x = fires.front().first;
    int y = fires.front().second;
    fires.pop();
    for (int i = 0; i < 4; i++)
    {
      int nx = x + dx[i];
      int ny = y + dy[i];
      if (1 <= nx && nx <= w && 1 <= ny && ny <= h && visited_fire[nx][ny] == 0 && board[nx][ny] != '#')
      {
        visited_fire[nx][ny] = visited_fire[x][y] + 1;
        fires.push({nx, ny});
      }
    }
  }

  while (!sanggeun.empty())
  {
    int x = sanggeun.front().first;
    int y = sanggeun.front().second;
    sanggeun.pop();
    for (int i = 0; i < 4; i++)
    {
      int nx = x + dx[i];
      int ny = y + dy[i];
      if (1 <= nx && nx <= w && 1 <= ny && ny <= h && visited[nx][ny] == 0 && board[nx][ny] != '#')
      {
        if ((visited[x][y] + 1 >= visited_fire[nx][ny]) && (visited_fire[nx][ny] >= 1))
          continue;
        sanggeun.push({nx, ny});
        visited[nx][ny] = visited[x][y] + 1;
        if (nx == 1 || nx == w || ny == 1 || ny == h)
        {
          cout << visited[nx][ny] << "\n";
          return;
        }
      }
    }
  }
  cout << "IMPOSSIBLE\n";
}

int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> t;
  while (t--)
    run();

  return 0;
}
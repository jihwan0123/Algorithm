// 2146. 다리 만들기
#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
int n;
int ans = 987654321;
int board[101][101];   // 섬 분류
int visited[101][101]; // 방문 체크용
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};
queue<pair<int, int>> q;
queue<pair<int, int>> edges; // 섬의 가장자리 좌표 저장

void clear_queue()
{
  while (!q.empty())
    q.pop();
}

void clear_visited()
{
  for (int i = 1; i <= n; i++)
    for (int j = 1; j <= n; j++)
      visited[i][j] = 0;
}

void bfs(int a, int b, int c)
{
  clear_queue();
  q.push({a, b});
  board[a][b] = c;
  visited[a][b] = 1;
  bool edge = false;
  while (!q.empty())
  {
    int x = q.front().X;
    int y = q.front().Y;
    q.pop();
    for (int i = 0; i < 4; i++)
    {
      int nx = x + dx[i];
      int ny = y + dy[i];
      if (nx < 1 || nx > n || ny < 1 || ny > n || board[nx][ny] == 0 || visited[nx][ny] == 1)
      {
        edge = true;
        continue;
      }
      board[nx][ny] = c;
      visited[nx][ny] = 1;
      q.push({nx, ny});
    }
    if (edge)
      edges.push({x, y});
  }
}

void check(int a, int b)
{
  clear_visited();
  clear_queue();
  q.push({a, b});
  visited[a][b] = 1;
  while (!q.empty())
  {
    int x = q.front().X;
    int y = q.front().Y;
    q.pop();
    for (int i = 0; i < 4; i++)
    {
      int nx = x + dx[i];
      int ny = y + dy[i];
      if (nx < 1 || nx > n || ny < 1 || ny > n)
        continue;
      if ((visited[nx][ny] > 0) || (board[a][b] == board[nx][ny]))
        continue;
      // 다른 섬 만나면 최솟값 갱신
      if (board[nx][ny] != 0)
      {
        ans = min(ans, visited[x][y] - 1);
        return;
      }
      visited[nx][ny] = visited[x][y] + 1;
      q.push({nx, ny});
    }
  }
}
int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> n;
  for (int i = 1; i <= n; i++)
    for (int j = 1; j <= n; j++)
      cin >> board[i][j];

  // 영역 나누기
  int k = 1;
  for (int i = 1; i <= n; i++)
    for (int j = 1; j <= n; j++)
    {
      if ((board[i][j] == 1) && (visited[i][j] == 0))
      {
        bfs(i, j, k);
        k++;
      }
    }

  // 거리 체크
  // for (int i = 1; i <= n; i++)
  //   for (int j = 1; j <= n; j++)
  //     if (board[i][j] != 0)
  //       check(i, j);

  while (!edges.empty())
  {
    int i = edges.front().X;
    int j = edges.front().Y;
    edges.pop();
    check(i, j);
  }

  cout << ans << "\n";

  return 0;
}
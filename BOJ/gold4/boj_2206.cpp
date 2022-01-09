// 2206. 벽 부수고 이동하기
#include <bits/stdc++.h>
using namespace std;
int n, m;
string board[1002];
int visited[1002][1002][2];
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};
int bfs(int a, int b, int c) {
  queue<tuple<int, int, int>> q;
  q.push({a, b, c});
  visited[a][b][c] = 1;
  while (!q.empty()) {
    int x = get<0>(q.front());
    int y = get<1>(q.front());
    int z = get<2>(q.front());
    q.pop();
    if (x == n - 1 && y == m - 1)
      return visited[x][y][z];
    for (int i = 0; i < 4; i++) {
      int nx = x + dx[i];
      int ny = y + dy[i];
      if (nx < 0 || ny < 0 || nx >= n || ny >= m)
        continue;
      // 벽 부수기
      if (board[nx][ny] == '1' && z == 1) {
        visited[nx][ny][0] = visited[x][y][1] + 1;
        q.push({nx, ny, 0});
      }
      if (board[nx][ny] == '0' && visited[nx][ny][z] == 0) {
        visited[nx][ny][z] = visited[x][y][z] + 1;
        q.push({nx, ny, z});
      }
    }
  }
  return -1;
}
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> n >> m;
  for (int i = 0; i < n; i++)
    cin >> board[i];
  cout << bfs(0, 0, 1);
}
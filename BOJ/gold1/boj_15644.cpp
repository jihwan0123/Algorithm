// 15644. 구슬 탈출 3
#include <bits/stdc++.h>
using namespace std;
int n, m;
int rx, ry, bx, by;
char board[11][11];
int visited[11][11][11][11];
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};
// red_x, red_y : 빨간 구슬 좌표, blue_x, blue_y : 파란 구슬 좌표
void bfs(int red_x, int red_y, int blue_x, int blue_y) {
  // 4방향이 벽이면 탈출 불가
  int chk = 0;
  for (int i = 0; i < 4; i++) {
    int x = red_x + dx[i];
    int y = red_y + dy[i];
    if (board[x][y] == '#')
      chk++;
  }
  if (chk == 4) {
    cout << -1;
    return;
  }
  queue<tuple<int, int, int, int, string>> q;
  q.push({red_x, red_y, blue_x, blue_y, ""});
  visited[red_x][red_y][blue_x][blue_y] = 1;
  while (!q.empty()) {
    int rx = get<0>(q.front());
    int ry = get<1>(q.front());
    int bx = get<2>(q.front());
    int by = get<3>(q.front());
    string mv = get<4>(q.front());
    int cnt = visited[rx][ry][bx][by];
    q.pop();
    // 10번 넘게 탈출 못하면 -1
    if (cnt > 10) {
      cout << -1;
      return;
    }
    // 4방향으로 기울이기
    for (int i = 0; i < 4; i++) {
      int n_rx = rx;
      int n_ry = ry;
      int n_bx = bx;
      int n_by = by;
      // Red 이동
      while (1) {
        int t_rx = n_rx + dx[i];
        int t_ry = n_ry + dy[i];
        if (board[t_rx][t_ry] == '#') {
          t_rx -= dx[i];
          t_ry -= dy[i];
          break;
        }
        if (board[t_rx][t_ry] == 'O') {
          n_rx = t_rx;
          n_ry = t_ry;
          break;
        } else {
          n_rx = t_rx;
          n_ry = t_ry;
        }
      }
      // Blue 이동
      while (1) {
        int t_bx = n_bx + dx[i];
        int t_by = n_by + dy[i];
        if (board[t_bx][t_by] == '#') {
          t_bx -= dx[i];
          t_by -= dy[i];
          break;
        }
        if (board[t_bx][t_by] == 'O') {
          n_bx = t_bx;
          n_by = t_by;
          break;
        } else {
          n_bx = t_bx;
          n_by = t_by;
        }
      }
      // Blue 탈출했으면 실패 (동시에 빠져도 실패)
      if (board[n_bx][n_by] == 'O')
        continue;
      // Red, Blue 겹쳐진 경우 늦게 출발한 구슬 한칸 뒤로
      if ((n_rx == n_bx) && (n_ry == n_by)) {
        if (i == 0)
          ry < by ? n_ry-- : n_by--;
        else if (i == 1)
          rx < bx ? n_rx-- : n_bx--;
        else if (i == 2)
          ry > by ? n_ry++ : n_by++;
        else
          rx > bx ? n_rx++ : n_bx++;
      }
      // 방문하지 않았으면 계속 탐색
      if (!visited[n_rx][n_ry][n_bx][n_by]) {
        if (i == 0)
          mv += 'R';
        else if (i == 1)
          mv += 'D';
        else if (i == 2)
          mv += 'L';
        else
          mv += 'U';
        // Red 탈출했으면 종료
        if (board[n_rx][n_ry] == 'O') {
          cout << cnt << '\n' << mv << '\n';
          return;
        }
        visited[n_rx][n_ry][n_bx][n_by] = cnt + 1;
        q.push({n_rx, n_ry, n_bx, n_by, mv});
        mv.pop_back();
      }
    }
  }
  cout << -1;
  return;
}
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> n >> m;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      cin >> board[i][j];
      if (board[i][j] == 'B') {
        bx = i;
        by = j;
      } else if (board[i][j] == 'R') {
        rx = i;
        ry = j;
      }
    }
  }
  bfs(rx, ry, bx, by);
}
// 15683. 감시
#include <bits/stdc++.h>
using namespace std;

#define X first
#define Y second

int n, m;
int ans = 100;
int board[10][10];
bool used[10];
vector<pair<int, int>> cctvs; // cctv 좌표 저장

int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};

void move(int x, int y, int dir, int board[][10]) {
  dir %= 4;
  while (1) {
    x += dx[dir];
    y += dy[dir];
    if (x < 0 || x >= n || y < 0 || y >= m || board[x][y] == 6) return;
    if (board[x][y] <= 0) board[x][y]--;
  }
  return;
}

void move_back(int x, int y, int dir, int board[][10]) {
  dir %= 4;
  while (1) {
    x += dx[dir];
    y += dy[dir];
    if (x < 0 || x >= n || y < 0 || y >= m || board[x][y] == 6) return;
    if (board[x][y] < 0) board[x][y]++;
  }
  return;
}

void func(int k, int cur, int board[][10]) {
  // 전체 cctv 다 체크 했으면 개수 체크
  if (k == (int)cctvs.size()) {
    int cnt = 0;
    for (int i = 0; i < n; i++)
      for (int j = 0; j < m; j++)
        if (board[i][j] == 0) cnt++;
    ans = min(cnt, ans);
    return;
  }

  // 백트래킹
  for (int i = cur; i < cctvs.size(); i++) {
    if (used[i]) continue;
    used[i] = 1;
    int x = cctvs[i].X;
    int y = cctvs[i].Y;
    int c = board[x][y];
    // 백트래킹 (최대 cctv 8개 : 4^8)
    for (int dir = 0; dir < 4; dir++) {
      if (c == 1) {
        move(x, y, dir, board);
        func(k + 1, i, board);
        move_back(x, y, dir, board);
      } else if (c == 2) {
        move(x, y, dir, board);
        move(x, y, dir + 2, board);
        func(k + 1, i, board);
        move_back(x, y, dir, board);
        move_back(x, y, dir + 2, board);
      } else if (c == 3) {
        move(x, y, dir, board);
        move(x, y, dir + 1, board);
        func(k + 1, i, board);
        move_back(x, y, dir, board);
        move_back(x, y, dir + 1, board);
      } else if (c == 4) {
        for (int j = 0; j < 3; j++)
          move(x, y, dir + j, board);
        func(k + 1, i, board);
        for (int j = 0; j < 3; j++)
          move_back(x, y, dir + j, board);
      } else if (c == 5) {
        for (int j = 0; j < 4; j++)
          move(x, y, dir + j, board);
        func(k + 1, i, board);
        for (int j = 0; j < 4; j++)
          move_back(x, y, dir + j, board);
      }
    }
    used[i] = 0;
  }
}

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> n >> m;
  for (int i = 0; i < n; i++)
    for (int j = 0; j < m; j++) {
      cin >> board[i][j];
      if (board[i][j] > 0 && board[i][j] < 6)
        cctvs.push_back({i, j});
    }
  func(0, 0, board);
  cout << ans << '\n';
}
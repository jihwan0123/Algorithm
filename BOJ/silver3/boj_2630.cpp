// 2630. 색종이 만들기
#include <bits/stdc++.h>
using namespace std;
int blue, white;
int board[130][130];
void check(int n, int x, int y)
{
  bool chk = true;
  // x,y부터 x+n,y+n까지 모두 같은지 확인
  for (int i = x; i < n + x; i++)
    for (int j = y; j < y + n; j++)
      if (board[i][j] != board[x][y])
        chk = false;

  // 같으면 blue, white ++
  if (chk)
  {
    board[x][y] == 1 ? blue++ : white++;
    return;
  }
  int m = n / 2;
  // 4개로 쪼개면서 반복
  check(m, x, y);
  check(m, x + m, y);
  check(m, x, y + m);
  check(m, x + m, y + m);
}
int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n;
  cin >> n;
  for (int i = 1; i <= n; i++)
    for (int j = 1; j <= n; j++)
      cin >> board[i][j];
  check(n, 1, 1);
  cout << white << '\n'
       << blue << '\n';
}
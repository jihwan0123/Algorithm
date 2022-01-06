// 1992. 쿼드트리
#include <bits/stdc++.h>
using namespace std;
string board[65];
void check(int n, int x, int y)
{
  // n=1이면 출력하고 종료
  if (n == 1)
  {
    cout << board[x][y];
    return;
  }

  // 압축 가능한지 체크
  bool chk = true;
  for (int i = x; i < x + n; i++)
    for (int j = y; j < y + n; j++)
      if (board[i][j] != board[x][y])
        chk = false;

  if (chk) // 압축 가능하면 압축 결과 출력
  {
    cout << (board[x][y] == '1' ? 1 : 0);
    return;
  }
  else // 불가능하면
  {
    // 왼위, 오위, 왼아래, 오아래 순서로 반복
    int m = n / 2;
    cout << '(';
    check(m, x, y);
    check(m, x, y + m);
    check(m, x + m, y);
    check(m, x + m, y + m);
    cout << ')';
  }
}
int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n;
  cin >> n;
  for (int i = 0; i < n; i++)
  {
    string s;
    cin >> s;
    board[i] = s;
  }
  check(n, 0, 0);
}
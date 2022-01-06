// 2448. 별 찍기 - 11
#include <bits/stdc++.h>
using namespace std;
#define MAX 1024 * 3
char board[MAX][MAX * 2];

void make_star(int n, int y, int x) // x,y 꼭지점으로 크기n
{
  if (n == 3)
  {
    // 별 찍기
    board[y][x] = '*';
    board[y + 1][x - 1] = '*';
    board[y + 1][x + 1] = '*';
    for (int i = x - 2; i <= x + 2; i++)
      board[y + 2][i] = '*';
    return;
  }
  int m = n / 2;
  // 삼각형 꼭지점마다 반복
  make_star(m, y, x);
  make_star(m, y + m, x - m);
  make_star(m, y + m, x + m);
}
int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n;
  cin >> n;
  make_star(n, 0, n - 1);
  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j < n * 2 - 1; j++)
    {
      if (board[i][j] == '*')
        cout << '*';
      else
        cout << ' ';
    }
    cout << '\n';
  }
}
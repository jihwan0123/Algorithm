// A. Stable Arrangement of Rooks
#include <bits/stdc++.h>
using namespace std;
char board[102][102];
int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  int t;
  cin >> t;
  for (int i = 0; i < 102; i++)
    for (int j = 0; j < 102; j++)
      board[i][j] = '.';

  while (t--)
  {
    int n, k;
    cin >> n >> k;
    if (n == 1)
    {
      cout << "R\n";
      continue;
    }
    if (n & 1 == 1) // 홀수면
    {
      if ((n / 2) + 1 < k)
      {
        cout << "-1\n";
        continue;
      }
    }
    else // 짝수면
    {
      if ((n / 2) < k)
      {
        cout << "-1\n";
        continue;
      }
    }

    // 2줄 간격으로 룩 놓기
    int cnt = 0;
    for (int i = 1; i <= n; i += 2)
    {
      board[i][i] = 'R';
      cnt++;
      if (cnt >= k)
        break;
    }

    for (int i = 1; i <= n; i++)
    {
      for (int j = 1; j <= n; j++)
      {
        cout << board[i][j];
        board[i][j] = '.';
      }
      cout << "\n";
    }
  }
}
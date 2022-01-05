// 1074. Z
#include <bits/stdc++.h>
using namespace std;
int run_z(int n, int r, int c)
{
  if (n == 0)
    return 0;
  int m = 1 << (n - 1); // 2^(n-1)
  if (r < m && c < m)   // 0
    return run_z(n - 1, r, c);
  else if (r < m && c >= m) // 1
    return m * m + run_z(n - 1, r, c - m);
  else if (r >= m && c < m) // 2
    return 2 * m * m + run_z(n - 1, r - m, c);
  else // 3
    return 3 * m * m + run_z(n - 1, r - m, c - m);
}

int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n, r, c;
  cin >> n >> r >> c;
  cout << run_z(n, r, c) << "\n";
}
#include <bits/stdc++.h>
using namespace std;
int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  long long n, m;
  long long sx, sy, ex, ey;
  cin >> n >> m;
  cin >> sx >> sy >> ex >> ey;
  // n,m이 1인 경우 출발지 = 도착지가 아니면 못감
  if (n == 1)
  {
    if (sy == ey)
    {
      cout << "YES\n";
      return 0;
    }
    cout << "NO\n";
    return 0;
  }
  if (m == 1)
  {
    if (sx == ex)
    {
      cout << "YES\n";
      return 0;
    }
    cout << "NO\n";
    return 0;
  }

  // 홀,홀 -> 짝짝 or 홀홀
  // 홀,짝 -> 짝,홀 or 홀,짝
  if (((((sx & 1) + (sy & 1))) % 2) == ((((ex & 1) + (ey & 1))) % 2))
    cout << "YES\n";
  else
    cout << "NO\n";
}
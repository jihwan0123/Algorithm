// 9657. 돌 게임 3
#include <bits/stdc++.h>
using namespace std;
int d[1002];
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n;
  cin >> n;
  d[1] = 1, d[3] = 1, d[4] = 1;
  for (int i = 5; i <= n; i++)
    if (!d[i - 4] || !d[i - 3] || !d[i - 1]) d[i] = 1;

  cout << (d[n] == 1 ? "SK" : "CY");
}
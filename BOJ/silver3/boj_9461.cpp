// 9461. 파도반 수열
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
ll d[105];
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  d[1] = 1, d[2] = 1, d[3] = 1;

  for (int i = 4; i <= 100; i++)
    d[i] = d[i - 2] + d[i - 3];

  int t;
  cin >> t;
  while (t--) {
    int n;
    cin >> n;
    cout << d[n] << '\n';
  }
}
/*
1 1 1 2 2 3 4 5 7 9 12
d[n] = d[n-2] + d[n-3]
*/
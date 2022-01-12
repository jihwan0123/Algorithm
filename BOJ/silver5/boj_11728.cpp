// 11728. 배열 합치기
#include <bits/stdc++.h>
using namespace std;

int n, m;
int a[1000002], b[1000002];

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> n >> m;
  for (int i = 0; i < n; i++)
    cin >> a[i];
  for (int i = 0; i < m; i++)
    cin >> b[i];

  sort(a, a + n);
  sort(b, b + m);
  int aidx = 0, bidx = 0;
  while (aidx + bidx < n + m) {
    if (bidx == m)
      cout << a[aidx++] << ' ';
    else if (aidx == n)
      cout << b[bidx++] << ' ';
    else if (a[aidx] <= b[bidx])
      cout << a[aidx++] << ' ';
    else
      cout << b[bidx++] << ' ';
  }
}
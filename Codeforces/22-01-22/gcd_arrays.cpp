// B. GCD Arrays
#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int t;
  cin >> t;
  while (t--) {
    int l, r, k;
    cin >> l >> r >> k;
    if (l == r) {
      cout << (l == 1 ? "NO\n" : "YES\n");
      continue;
    }
    int n = r - l + 1;
    int m = r / 2 - l / 2;
    if (l % 2 == 0) m++;
    cout << (k >= n - m ? "YES\n" : "NO\n");
  }
}
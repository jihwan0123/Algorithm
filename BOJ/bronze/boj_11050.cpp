// 11050. 이항계수 1
#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n, k;
  cin >> n >> k;
  int ans = 1;
  for (int i=2; i<=n; i++) ans *= i;
  for (int i=2; i<=k; i++) ans /= i;
  for (int i=2; i<=(n-k); i++) ans /= i;
  cout << ans;
}
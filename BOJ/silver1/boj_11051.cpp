// 11051. 이항 계수 2
#include <bits/stdc++.h>
using namespace std;
int comb[1002][1002]; // comb[n][k] = nCk
const int mod = 10007;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n, k;
  cin >> n >> k;
  for (int i=1; i<=n; i++){
    comb[i][0] = comb[i][i] = 1;
    for (int j=1; j<i; j++)
      comb[i][j] = (comb[i-1][j] + comb[i-1][j-1]) % mod;
  }
  cout << comb[n][k];
}
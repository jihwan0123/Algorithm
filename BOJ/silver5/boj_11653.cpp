// 11653. 소인수분해
#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n;
  cin >> n;
  for (int i=2; i*i<=n; i++){
    while (n%i == 0) {
      cout << i << '\n';
      n /= i;
    }
  }
  if (n != 1) cout << n;
  // while (n > 1){
  //   for (int i=2; i<=n; i++){
  //     if (i*i > n) {
  //       cout << n << '\n';
  //       n = 1;
  //       break;
  //     }
  //     if (n%i == 0) {
  //       cout << i << '\n';
  //       n/=i;
  //       break;
  //     }
  //   }
  // }
}
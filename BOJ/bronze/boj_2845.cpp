// 2845. 파티가 끝나고 난 뒤
#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int l, p;
  cin >> l >> p;
  int tmp = l * p;
  for (int i = 0; i < 5; i++) {
    int x;
    cin >> x;
    cout << x - tmp << ' ';
  }
}
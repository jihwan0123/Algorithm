// 1193. 분수찾기
#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int x;
  cin >> x;
  int n = 1;
  while (x > n) x -= n++;
  if (n % 2 == 0)
    cout << x << '/' << n + 1 - x;
  else
    cout << n + 1 - x << '/' << x;
}
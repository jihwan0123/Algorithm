// 6064. 카잉 달력
#include <bits/stdc++.h>
using namespace std;

int gcd(int a, int b){
  if (a < b) swap(a,b);
  int n;
  while (b != 0){
    n = a % b;
    a = b; b = n;
  }
  return a;
}

int lcm(int a, int b){
  return a / gcd(a, b) * b;
}

int solve(int m, int n, int x, int y){
  if (x == m) x = 0;
  if (y == n) y = 0;
  int l = lcm(m, n); // 최대값은 lcm(m, n)
  // m으로 나눠지는지 수들 중 n으로 나눠지는지 체크
  for (int i = x; i <= l; i += m)
    if (i % n == y) return i;
  return -1;
}

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int t;
  cin >> t;
  while(t--){
    int m, n, x, y;
    cin >> m >> n >> x >> y;
    cout << solve(m, n, x, y) << '\n';
  }
}
// 1912. 연속합
#include <bits/stdc++.h>
using namespace std;
int d[100005];
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n;
  cin >> n;
  for (int i = 1; i <= n; i++) {
    cin >> d[i];
    // 최대 연속합으로 갱신
    d[i] = max(d[i], d[i - 1] + d[i]);
  }
  // max_element는 최댓값의 주소 반환
  cout << *max_element(d + 1, d + n + 1);
}
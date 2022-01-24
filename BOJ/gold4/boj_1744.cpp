// 1744. 수 묶기
#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n;
  cin >> n;
  int zero_cnt = 0;
  vector<int> plus, minus;
  for (int i = 0; i < n; i++) {
    int x;
    cin >> x;
    if (x > 0) plus.push_back(x);
    else if (x < 0) minus.push_back(x);
    else zero_cnt++;
  }
  sort(plus.begin(), plus.end(), greater<>());
  sort(minus.begin(), minus.end());

  int ans = 0;
  int ps = (int)plus.size();
  int ms = (int)minus.size();
  int pi = 0, mi = 0;
  while (pi < ps) {
    if ((ps - pi) >= 2) {
      if (plus[pi] == 1 || plus[pi + 1] == 1) // 1은 곱하지 않고 더하는게 최대
        ans += plus[pi] + plus[pi + 1];
      else
        ans += plus[pi] * plus[pi + 1];
      pi += 2;
    } 
    else ans += plus[pi++];
  }

  while (mi < ms) {
    if ((ms - mi) >= 2) { // 절대값이 가장 큰 음수 2개 곱하면 최대
      ans += minus[mi] * minus[mi + 1];
      mi += 2;
    } 
    else {
      if (zero_cnt > 0) { // 0 곱할 수 있으면 0 곱해서 음수 제거
        mi++;
        zero_cnt--;
      } 
      else ans += minus[mi++];
    }
  }
  cout << ans;
}
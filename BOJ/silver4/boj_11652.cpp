// 11652. 카드
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n;
  cin >> n;
  vector<ll> arr;
  for (int i = 0; i < n; i++) {
    ll x;
    cin >> x;
    arr.push_back(x);
  }
  sort(arr.begin(), arr.end());
  // 정렬 후 앞에서부터 최대 개수 val 찾기
  ll val = arr[0];
  int idx = 1, cnt = 1, mxcnt = 0;
  while (idx <= n) {
    if (idx != n && (arr[idx - 1] == arr[idx]))
      cnt++;
    else {
      if (cnt > mxcnt) {
        mxcnt = cnt;
        val = arr[idx - 1];
      }
      cnt = 1;
    }
    idx++;
  }
  cout << val;
}
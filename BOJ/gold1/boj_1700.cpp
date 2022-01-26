// 1170. 멀티탭 스케줄링
#include <bits/stdc++.h>
using namespace std;

int n, k, ans;
int a[102], used[102];

bool plug(int x) {
  for (int j=0; j<n; j++) {
    // 이미 꽂혀있거나 사용하지 않고 있으면 사용
    if (!used[j] || (used[j] == a[x])){
      used[j] = a[x];
      return true;
    }
  }
  return false;
}

int unplug(int x){
  int idx = 0, tmp = 0;
  // 나중에 사용하지 않거나, 마지막에 다시 사용할 기기 선택
  for (int i=0; i<n; i++) {
    int cnt = 1;
    for (int j=x; j<k; j++){
      if (used[i] == a[j]) break;
      cnt++;
    }
    if (cnt > tmp) {
      idx = i; tmp = cnt;
    }
  }
  return idx;
}

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> n >> k;
  for (int i=0; i<k; i++) cin >> a[i];
  for (int i=0; i<k; i++) {
    if (plug(i)) continue; // 멀티탭에 꽂을 수 있으면 꽂고 다음으로
    int pn = unplug(i+1); // 뽑아야 하는 plug 번호
    used[pn] = a[i]; // 플러그 뽑고 새로운 기기 사용
    ans++;
  }
  cout << ans;
}
// 3 14
// 1 4 3 2 5 4 3 2 5 3 4 2 3 4
// ans : 4
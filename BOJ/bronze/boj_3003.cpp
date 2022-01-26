// 3003. 킹, 퀸, 룩, 비숍, 나이트, 폰
#include <bits/stdc++.h>
using namespace std;
int a[6];
int b[6] = {1,1,2,2,2,8};
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  for (int i=0; i<6; i++) cin >> a[i];
  for (int i=0; i<6; i++) cout << (b[i]-a[i]) << ' ';
}
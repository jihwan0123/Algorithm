// 5532. 방학 숙제
#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int l,b,a,c,d;
  cin >> l >> a >> b >> c >> d;
  cout << l - max(b%d==0?b/d:b/d+1,a%c==0?a/c:a/c+1);
}
// C. Kill the Monster
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int t;
  cin >> t;
  while (t--) {
    ll hc, dc; cin >> hc >> dc;
    ll hm, dm; cin >> hm >> dm;
    ll k, w, a; cin >> k >> w >> a;
    bool chk = false;
    for (int i=0; i<=k; i++){
      ll h = (i*a)+hc, d = (k-i)*w+dc;
      ll x = hm%d==0?(hm/d):(hm/d)+1;
      ll y = h%dm==0?(h/dm):(h/dm)+1;
      if (x<=y) {
        chk = true;
        break;
      }
    }
    cout << (chk ? "YES\n" : "NO\n");
  }
}
// B. Minority
#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int t;
  cin >> t;
  while(t--){
    string s;
    cin >> s;
    int one = 0;
    int zero = 0;
    for (int i=0; i<s.size(); i++) {
      if (s[i] == '0') zero++;
      else one++;
    }
    if (zero == one) {
      if (zero == 1) cout << 0 << '\n';
      else cout << zero -1 << '\n';
      continue;
    }
    cout << min(zero, one) << '\n';
  }
}
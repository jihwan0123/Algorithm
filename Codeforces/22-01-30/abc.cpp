// A. ABC
#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int t;
  cin >> t;
  while (t--) {
    int n;
    cin >> n;
    string s;
    cin >> s;
    if (n == 1) {
      cout << "YES\n";
      continue;
    } 
    else if (n==2) {
      if (s[0] == s[1]) cout << "NO\n";
      else cout << "YES\n";
      continue;
    }
    // 길이 3 이상은 무조건 palindrome 존재
    else  cout << "NO\n";
  }
}
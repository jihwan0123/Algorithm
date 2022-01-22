// 1541. 잃어버린 괄호
#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  string s;
  cin >> s;
  string n = "";
  int tmp = 1, ans = 0;
  for (char c : s) {
    if (c == '+') {
      ans += stoi(n) * tmp;
      n = "";
    }
    else if (c == '-') {
      ans += stoi(n) * tmp;
      tmp = -1;
      n = "";
    } 
    else n += c;
  }
  cout << ans + (stoi(n) * tmp);
}
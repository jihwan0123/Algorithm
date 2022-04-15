// 7785. 회사에 있는 사람
#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  unordered_set<string> s;
  int n;
  cin >> n;
  while (n--) {
    string s1, s2;
    cin >> s1 >> s2;
    if (s2 == "enter") s.insert(s1);
    else s.erase(s1);
  }
  vector<string> ans{begin(s), end(s)};
  sort(begin(ans), end(ans), [&](string& a, string& b){return a>b;});
  for(auto& a : ans) cout << a << "\n";
}
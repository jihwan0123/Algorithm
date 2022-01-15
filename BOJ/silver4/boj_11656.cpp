// 11656. 접미사 배열
#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  string s;
  cin >> s;
  vector<string> v;
  for (int i = 0; i < s.size(); i++) {
    string tmp = "";
    for (int j = i; j < s.size(); j++)
      tmp += s[j];
    v.push_back(tmp);
  }
  sort(v.begin(), v.end());
  for (auto i : v)
    cout << i << '\n';
}
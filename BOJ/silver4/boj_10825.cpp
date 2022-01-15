// 10825. 국영수
#include <bits/stdc++.h>
using namespace std;

#define X first
#define Y second

bool cmp(pair<tuple<int, int, int>, string> &a,
         pair<tuple<int, int, int>, string> &b) {
  int a1, a2, a3, b1, b2, b3;
  tie(a1, a2, a3) = a.X;
  tie(b1, b2, b3) = b.X;
  if (a1 == b1) {
    if (a2 == b2) {
      if (a3 == b3)
        return a.Y < b.Y;
      else
        return a3 > b3;
    } else
      return a2 < b2;
  } else
    return a1 > b1;
}

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n;
  cin >> n;
  vector<pair<tuple<int, int, int>, string>> v;
  for (int i = 0; i < n; i++) {
    string name;
    int s1, s2, s3;
    cin >> name >> s1 >> s2 >> s3;
    v.push_back({{s1, s2, s3}, name});
  }
  sort(v.begin(), v.end(), cmp);
  for (auto i : v)
    cout << i.Y << '\n';
}
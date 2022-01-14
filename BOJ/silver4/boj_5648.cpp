// 5648. 역원소 정렬
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n;
  cin >> n;
  vector<ll> v;
  for (int i = 0; i < n; i++) {
    string s;
    cin >> s;
    reverse(s.begin(), s.end());
    v.push_back(stoll(s));
  }
  sort(v.begin(), v.end());

  for (auto i : v)
    cout << i << '\n';
}
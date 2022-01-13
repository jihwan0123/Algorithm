// 1431. 시리얼 번호
#include <bits/stdc++.h>
using namespace std;

bool cmp(string &a, string &b) {
  int lena = a.size(), lenb = b.size();
  if (lena != lenb)
    return lena < lenb;

  int suma = 0, sumb = 0;
  for (int i = 0; i < a.size(); i++) {
    if (isdigit(a[i]))
      suma += (a[i] - '0');
    if (isdigit(b[i]))
      sumb += (b[i] - '0');
  }
  if (suma != sumb)
    return suma < sumb;
  return a < b;
}
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n;
  cin >> n;
  vector<string> nums;
  for (int i = 0; i < n; i++) {
    string x;
    cin >> x;
    nums.push_back(x);
  }
  sort(nums.begin(), nums.end(), cmp);
  for (auto num : nums) {
    cout << num << '\n';
  }
}
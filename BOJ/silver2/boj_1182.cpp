// 1182. 부분수열의 합
#include <bits/stdc++.h>
using namespace std;
int n, s, ans;
vector<int> nums;
void func(int k, int total)
{
  if (k == n)
  {
    if (total == s)
      ans++;
    return;
  }
  func(k + 1, total);
  func(k + 1, total + nums[k]);
}
int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> n >> s;
  for (int i = 0; i < n; i++)
  {
    int x;
    cin >> x;
    nums.push_back(x);
  }
  func(0, 0);
  if (s == 0)
    ans--;
  cout << ans;
}
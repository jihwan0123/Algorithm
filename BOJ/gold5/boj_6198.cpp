// 6198. 옥상 정원 꾸미기
#include <bits/stdc++.h>
using namespace std;
int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);

  int n;
  cin >> n;
  stack<int> s;
  long long ans = 0;
  long long h;
  while (n--)
  {
    cin >> h;
    while (!s.empty() && s.top() <= h)
      s.pop();
    ans += s.size();
    s.push(h);
  }
  cout << ans << "\n";
}
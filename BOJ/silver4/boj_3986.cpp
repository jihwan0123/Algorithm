// 3986. 좋은 단어
#include <bits/stdc++.h>
using namespace std;
int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n;
  cin >> n;
  int ans = 0;
  while (n--)
  {
    string s;
    cin >> s;
    stack<char> st;
    for (char c : s)
    {
      if (st.empty())
        st.push(c);
      else
      {
        if (st.top() == c)
          st.pop();
        else
          st.push(c);
      }
    }
    if (st.empty())
      ans++;
  }
  cout << ans << "\n";
}
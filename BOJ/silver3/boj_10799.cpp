// 10799. 쇠막대기
#include <bits/stdc++.h>
using namespace std;
int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  string s;
  cin >> s;
  stack<char> st;
  int ans = 0;
  for (int i = 0; i < s.size(); i++)
  {
    if (s[i] == '(')
    {
      st.push(s[i]);
    }
    else if (s[i] == ')')
    {
      st.pop();
      // 레이저면
      if (s[i - 1] == '(')
        // 스택 사이즈만큼 잘린다
        ans += st.size();
      else // 아니면 + 1
        ans++;
    }
  }
  cout << ans << '\n';
}
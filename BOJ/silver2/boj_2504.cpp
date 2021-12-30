// 2504. 괄호의 값
#include <bits/stdc++.h>
using namespace std;
int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  string s;
  cin >> s;
  if (s.size() & 1 == 1)
  {
    cout << 0 << "\n";
    return 0;
  }

  stack<char> st;
  int ans = 0;
  int temp = 1;
  for (int i = 0; i < s.size(); i++)
  {
    // '(' 면 x2후 stack에 추가
    if (s[i] == '(')
    {
      temp *= 2;
      st.push(s[i]);
    }
    // '[' 면 x3후 stack에 추가
    else if (s[i] == '[')
    {
      temp *= 3;
      st.push(s[i]);
    }
    // ')'면
    else if (s[i] == ')')
    {
      // 괄호 쌍이 맞는지 체크
      if (st.empty() || st.top() != '(')
      {
        cout << 0 << "\n";
        return 0;
      }
      // '(' 쌍이 맞으면 temp 더하고
      if (s[i - 1] == '(')
        ans += temp;
      // 스택에서 제거하고 2로 나눈다.
      st.pop();
      temp /= 2;
    }
    // ']' 면
    else if (s[i] == ']')
    {
      // 괄호 쌍이 맞는지 체크
      if (st.empty() || st.top() != '[')
      {
        cout << 0 << "\n";
        return 0;
      }
      // '[' 쌍이 맞으면 temp 더하고
      if (s[i - 1] == '[')
        ans += temp;
      // 스택에서 제거하고 3으로 나눈다.
      st.pop();
      temp /= 3;
    }
  }
  // 스택에 남아잇으면 괄호 쌍이 안맞음
  if (!st.empty())
    ans = 0;
  cout << ans << "\n";
}
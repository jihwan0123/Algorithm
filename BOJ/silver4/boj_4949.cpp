// 4949. 균형잡힌 세상
#include <bits/stdc++.h>
using namespace std;
int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  while (true)
  {
    string s;
    getline(cin, s);
    // 입력이 . 이면 종료
    if (s == ".")
      return 0;

    stack<char> st;
    bool balance = true; // 균형인지 체크
    for (char c : s)
    {
      if (c == '(' || c == '[') // 여는 괄호면 스택에 삽입
        st.push(c);
      // 닫는 괄호면 괄호 쌍이 맞는지 체크
      else if (c == ')')
      {
        if (st.empty() || st.top() != '(')
        {
          balance = false;
          break;
        }
        st.pop();
      }
      else if (c == ']')
      {
        if (st.empty() || st.top() != '[')
        {
          balance = false;
          break;
        }
        st.pop();
      }
    }
    // 괄호가 남아있으면 불균형
    if (!st.empty())
      balance = false;
    cout << (balance ? "yes\n" : "no\n");
  }
}
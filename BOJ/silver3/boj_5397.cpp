// 5397. 키로거
#include <bits/stdc++.h>
using namespace std;
int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  int t;
  cin >> t;
  while (t--)
  {
    string input;
    cin >> input;
    list<char> lst;
    auto cursor = lst.begin();
    for (auto i : input)
    {
      if (i == '<')
      {
        if (cursor != lst.begin())
          cursor--;
      }
      else if (i == '>')
      {
        if (cursor != lst.end())
          cursor++;
      }
      else if (i == '-')
      {
        if (cursor != lst.begin())
          cursor = lst.erase(--cursor);
      }
      else
        lst.insert(cursor, i);
    }

    for (auto a : lst)
      cout << a;
    cout << '\n';
  }
}
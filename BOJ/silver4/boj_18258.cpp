// 18258. 큐2
#include <bits/stdc++.h>
using namespace std;
int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  queue<int> q;
  int n;
  cin >> n;
  string s;
  int t;
  while (n--)
  {
    cin >> s;
    if (s == "push")
    {
      cin >> t;
      q.push(t);
    }
    else if (s == "pop")
    {
      if (!q.empty())
      {
        cout << q.front() << "\n";
        q.pop();
      }
      else
        cout << -1 << "\n";
    }
    else if (s == "size")
    {
      cout << q.size() << "\n";
    }
    else if (s == "empty")
    {
      if (q.empty())
        cout << 1 << "\n";
      else
        cout << 0 << "\n";
    }
    else if (s == "front")
    {
      if (!q.empty())
        cout << q.front() << "\n";
      else
        cout << -1 << "\n";
    }
    else
    {
      if (!q.empty())
        cout << q.back() << "\n";
      else
        cout << -1 << "\n";
    }
  }
}
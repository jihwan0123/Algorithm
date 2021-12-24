// 11098. 첼시를 도와줘!
#include <bits/stdc++.h>
using namespace std;
int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n;
  cin >> n;
  while (n--)
  {
    int p;
    cin >> p;
    int cost = 0;
    string name;
    while (p--)
    {
      int c;
      string s;
      cin >> c >> s;
      if (cost == 0 || cost < c)
      {
        cost = c;
        name = s;
      }
    }
    cout << name << "\n";
  }
}
// A. Integer Diversity
#include <iostream>
using namespace std;
bool pos[101];
bool neg[101];
int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n, m;
  cin >> n;
  while (n--)
  {
    cin >> m;
    int ans = 0;
    while (m--)
    {
      int x;
      cin >> x;
      if (x >= 0)
      {
        if (!pos[x])
        {
          pos[x] = true;
        }
        else
        {
          if (x == 0)
            continue;
          if (!neg[x])
          {
            neg[x] = true;
          }
        }
      }
      else
      {
        x = -x;
        if (!neg[x])
        {
          neg[x] = true;
        }
        else
        {
          if (!pos[x])
            pos[x] = true;
        }
      }
    }
    for (int i = 0; i < 101; i++)
    {
      if (pos[i])
      {
        ans++;
        pos[i] = false;
      }
      if (neg[i])
      {
        ans++;
        neg[i] = false;
      }
    }
    cout << ans << '\n';
  }
}
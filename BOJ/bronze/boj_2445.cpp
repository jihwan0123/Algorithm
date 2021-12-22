// 2445. 별 찍기 - 8
#include <bits/stdc++.h>
using namespace std;

int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);

  int n;
  cin >> n;

  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j <= 2 * n - 1; j++)
    {
      if (j <= i || (2 * n - 1 - j) <= i)
        cout << "*";
      else
        cout << " ";
    }
    cout << "\n";
  }

  for (int i = n - 2; i >= 0; i--)
  {
    for (int j = 0; j <= 2 * n - 1; j++)
    {
      if (j <= i || (2 * n - 1 - j) <= i)
        cout << "*";
      else
        cout << " ";
    }
    cout << "\n";
  }
}
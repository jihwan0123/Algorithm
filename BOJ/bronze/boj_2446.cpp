// 2446. 별 찍기 - 9
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
    for (int j = 0; j < i; j++)
      cout << " ";
    for (int k = 0; k < 2 * (n - i) - 1; k++)
      cout << "*";
    cout << "\n";
  }

  for (int i = n - 2; i >= 0; i--)
  {
    for (int j = 0; j < i; j++)
      cout << " ";
    for (int k = 0; k < 2 * (n - i) - 1; k++)
      cout << "*";
    cout << "\n";
  }
}
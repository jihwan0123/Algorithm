// 15650. N과 M (2)
#include <bits/stdc++.h>
using namespace std;
int arr[10];
int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n, m;
  cin >> n >> m;
  for (int i = 0; i < m; i++)
    arr[i] = -1;
  do
  {
    for (int i = 0; i < n; i++)
      if (arr[i] == -1)
        cout << i + 1 << ' ';
    cout << '\n';
  } while (next_permutation(arr, arr + n));
}
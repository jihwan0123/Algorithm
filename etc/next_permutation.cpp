#include <bits/stdc++.h>
using namespace std;
int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);

  int a[3] = {1, 2, 3};
  do
  {
    for (int i = 0; i < 3; i++)
      cout << a[i];
    cout << '\n';
  } while (next_permutation(a, a + 3));
  /*
  123
  132
  213
  231
  312
  321
  */

  // 1,2,3,4에서 2개의 수를 순서없이 뽑는 경우
  int b[4] = {0, 0, 1, 1};
  do
  {
    for (int i = 0; i < 4; i++)
      if (b[i] == 0)
        cout << i + 1;
    cout << '\n';
  } while (next_permutation(b, b + 4));
  /*
  12
  13
  14
  23
  24
  34
  */
}

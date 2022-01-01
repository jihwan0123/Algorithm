// 24040. 예쁜 케이크
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;
/* 시간초과
int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  int t;
  cin >> t;
  while (t--)
  {
    ll n;
    cin >> n;
    bool chk = false;
    // a * b = n
    // 2(a + b) = 3k
    for (ll i = 1; i * i <= n; i++)
    {
      if (n % i == 0)
      {
        if ((i + ll(n / i)) % 3 == 0)
        {
          chk = true;
          cout << "TAK\n";
          break;
        }
      }
    }
    if (!chk)
      cout << "NIE\n";
  }
}
*/

int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  int t;
  cin >> t;
  while (t--)
  {
    ll n;
    cin >> n;
    // a * b = n
    // 2(a + b) = 3k
    // a = 3x, b = 3y
    // a = 3x+1 b= 3y+2
    // 3으로 나눈 나머지가 2이거나, 9의 배수이면 가능
    if (n % 3 == 2 || n % 9 == 0)
      cout << "TAK\n";
    else
      cout << "NIE\n";
  }
}
// 2,5,8,9,11,14,17,18,20,23,26,27,29,32

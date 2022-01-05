// 1629. 곱셈
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
ll pow(ll a, ll b, ll mod)
{
  if (b == 1)
    return a % mod;
  ll val = pow(a, b / 2, mod); // 2^(2/n)
  val = val * val % mod;       // 2^n % mod
  // b가 짝수면 val 반환
  if (b % 2 == 0)
    return val;
  // 아니면 a 곱한값 반환
  return val * a % mod;
}

int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  ll a, b, c;
  cin >> a >> b >> c;
  cout << pow(a, b, c) << "\n";
}
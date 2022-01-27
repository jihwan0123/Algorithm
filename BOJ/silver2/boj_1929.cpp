// 1929. 소수 구하기
#include <bits/stdc++.h>
using namespace std;
// 에라토스테네스의 체 : 12ms
void sieve(int &n, int &m){
  vector<bool> state(n+1, true);
  state[1] = false;
  for (int i=2; i*i<=n; i++){
    if (!state[i]) continue;
    for (int j=i*i; j<=n; j+=i)
      state[j] = false;
  }
  for (int i=m; i<=n; i++)
    if (state[i]) cout << i << '\n';
}
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int m, n;
  cin >> m >> n;
  sieve(n, m);
}

// 하나씩 검사하는 방법 : 188ms
/*
bool isprime(int n){
  if (n==1) return 0;
  for (int i=2; i*i<=n; i++)
    if (n%i == 0) return 0;
  return 1;
}
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int m, n;
  cin >> m >> n;
  for (int i=m; i<=n; i++){
    int x;
    cin >> x;
    if (isprime(i)) cout << i << '\n';
  }
}
*/
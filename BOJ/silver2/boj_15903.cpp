// 15903. 카드 합체 놀이
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
/*
ll a[1001];
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n, m;
  cin >> n >> m;
  for (int i = 0; i < n; i++) cin >> a[i];
  while (m--) {
    sort(a, a+n);
    ll tmp = a[0] + a[1];
    a[0] = tmp;
    a[1] = tmp;
  }
  ll ans = 0;
  for (int i = 0; i < n; i++) ans += a[i];
  cout << ans;
}
*/
int main(void){
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n, m;
  cin >> n >> m;
  priority_queue<ll, vector<ll>, greater<ll>> pq;
  while(n--) {
    int x;
    cin >> x;
    pq.push(x);
  }

  while(m--){
    ll a = pq.top(); pq.pop();
    ll b = pq.top(); pq.pop();
    pq.push(a+b);
    pq.push(a+b);
  }
  ll ans = 0;
  while (!pq.empty()){
    ans += pq.top();
    pq.pop();
  }
  cout << ans;
}
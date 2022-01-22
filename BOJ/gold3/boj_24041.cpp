// 24041. 성싶당 밀키트
#include <bits/stdc++.h>
using namespace std;
#define MAX 2e9 + 1
typedef long long ll;
int n, g, k; // n: 재료 개수 g: 세균 최대값, k: 제거 가능한 재료의 수

// x일에 가능한지 체크
bool check(vector<tuple<ll, ll, ll>> &v, ll x)
{
  ll ret = 0;
  vector<ll> removed; // 제거 가능한 재료들
  removed.clear();
  for (auto t : v)
  {
    ll s, l, o;
    tie(s, l, o) = t;
    ll temp = s * max(ll(1), x - l);
    ret += temp;
    if (o == 1)
      removed.push_back(temp);
  }

  // 정렬 후 세균 많은 순서로 k개 제거
  sort(removed.begin(), removed.end(), greater<>());
  int cnt = 0;
  for (auto r : removed)
  {
    if (cnt >= k)
      break;
    ret -= r;
    cnt++;
  }
  // g 이하면 가능
  return (ret <= g) ? true : false;
}
int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> n >> g >> k;
  vector<tuple<ll, ll, ll>> mealkit;
  for (int i = 0; i < n; i++)
  {
    ll s, l, o; // s: 부패속도, l: 유통기한, o: 중요하면 0
    cin >> s >> l >> o;
    mealkit.push_back({s, l, o});
  }

  ll ans = 0;
  ll left = 0;
  ll right = MAX;
  // 이분탐색으로 최대 x일 탐색
  while (left <= right)
  {
    ll mid = (left + right) / 2;
    if (check(mealkit, mid))
    {
      ans = mid;
      left = mid + 1;
    }
    else
      right = mid - 1;
  }
  cout << ans << "\n";
}
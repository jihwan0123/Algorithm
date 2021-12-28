// 1021. 회전하는 큐
#include <bits/stdc++.h>
using namespace std;
int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  deque<int> dq;
  int n, m;
  cin >> n >> m;
  int ans = 0;

  for (int i = 1; i <= n; i++)
    dq.push_back(i);

  while (m--)
  {
    int x;
    cin >> x;
    // 맨앞에 있으면 1번
    if (dq.front() == x)
    {
      dq.pop_front();
      continue;
    }

    int idx = 0;
    for (int i = 0; i < dq.size(); i++)
    {
      if (dq[i] == x)
      {
        idx = i;
        break;
      }
    }

    if (idx <= (int)dq.size() / 2) // 왼쪽으로 이동
    {
      // 2번
      while (dq.front() != x)
      {
        dq.push_back(dq.front());
        dq.pop_front();
        ans++;
      }
    }
    else // 오른쪽으로 이동
    {
      // 3번
      while (dq.front() != x)
      {
        dq.push_front(dq.back());
        dq.pop_back();
        ans++;
      }
    }
    // 1번
    dq.pop_front();
  }
  cout << ans << "\n";
}
// 2164. 카드2
#include <bits/stdc++.h>
using namespace std;
int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n;
  cin >> n;
  if (n <= 2)
  {
    cout << n << "\n";
    return 0;
  }

  queue<int> q;
  for (int i = 1; i <= n; i++)
    q.push(i);

  while (q.size() > 1)
  {
    q.pop();
    q.push(q.front());
    q.pop();
  }
  cout << q.front() << "\n";
}
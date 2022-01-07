// N-Queen
#include <bits/stdc++.h>
using namespace std;
int n, cnt;
bool used[32];
bool used_right[32];
bool used_left[32];
void func(int y)
{
  if (y == n)
  {
    cnt++;
    return;
  }
  for (int x = 1; x <= n; x++)
  {
    // x + y 가 같으면 right_diag, x - y가 같으면 left_diag가 같다. (-index 방지용 x - y + n)
    if (used[x] || used_right[x + y] || used_left[y - x + n])
      continue;
    used[x] = true;
    used_right[x + y] = true;
    used_left[y - x + n] = true;
    func(y + 1);
    used[x] = false;
    used_right[x + y] = false;
    used_left[y - x + n] = false;
  }
}
int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> n;
  func(0);
  cout << cnt;
}
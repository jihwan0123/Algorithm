// 11729. 하노이 탑 이동 순서
#include <bits/stdc++.h>
using namespace std;
void hanoi(int n, int before, int mid, int after)
{
  // n==1이면 종료
  if (n == 1)
  {
    cout << before << ' ' << after << '\n';
    return;
  }

  hanoi(n - 1, before, after, mid);       // n-1개의 원판을 1번에서 2번으로 옮긴다.
  cout << before << ' ' << after << '\n'; // 1개 남은 원판을 1에서 3으로 옮긴다.
  hanoi(n - 1, mid, before, after);       // n-1개의 원판을 2번에서 3번으로 옮긴다.
}

int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  int N;
  cin >> N;
  cout << (1 << N) - 1 << '\n';
  hanoi(N, 1, 2, 3);
}
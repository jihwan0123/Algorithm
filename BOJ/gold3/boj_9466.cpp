// 9466. 텀 프로젝트
#include <bits/stdc++.h>
using namespace std;
#define MAX 100001
int arr[MAX];
int state[MAX]; // 사이클이면 -1
int n, t, ans;

void dfs(int start, int cur) // start : 시작값, cur : 현재값
{
  state[cur] = start; // start로 변경
  int nxt = arr[cur]; // 다음값
  // 시작과 nxt가 같으면 사이클
  if (start == state[nxt])
  {
    // 사이클 값들 모두 -1로 변경
    while (state[nxt] != -1)
    {
      state[nxt] = -1;
      nxt = arr[nxt];
    }
    return;
  }
  // 사이클이 아닌 값을 만나면 어차피 사이클이 안되니 종료
  if (state[nxt] != 0)
    return;
  // nxt에 대해 반복
  dfs(start, nxt);
}

int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> t;
  while (t--)
  {
    ans = 0;
    cin >> n;
    for (int i = 1; i <= n; i++)
      cin >> arr[i];

    for (int i = 1; i <= n; i++)
      if (state[i] == 0)
        dfs(i, i);

    // 사이클 카운트
    for (int i = 1; i <= n; i++)
    {
      if (state[i] != -1)
        ans++;
      state[i] = 0;
    }

    cout << ans << "\n";
  }
}
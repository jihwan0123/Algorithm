// 15664. N과 M (10)
#include <bits/stdc++.h>
using namespace std;
int n, m;
int arr[10];
int ans[10];

void func(int k, int cur) {
  if (k == m) {
    for (int i = 0; i < m; i++) {
      cout << ans[i] << ' ';
    }
    cout << '\n';
    return;
  }
  int tmp = 0;
  for (int i = cur; i < n; i++) {
    if (tmp != arr[i]) { // dfs중에 k번째 수가 arr[i]인 경우는 1번만 출력되도록
      ans[k] = arr[i];
      tmp = arr[i];
      func(k + 1, i + 1);
    }
  }
}
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> n >> m;
  for (int i = 0; i < n; i++)
    cin >> arr[i];
  sort(arr, arr + n);
  func(0, 0);
}

/*
처음에 출력할 때 배열을 따로 만들어서 바로 앞의 출력을 저장해서 비교했는데
8 4
1 1 1 1 2 2 2 2 의 경우
1 1 1 2
1 1 2 2
1 1 1 2 와 같은 경우가 발생
dfs 들어가기 전에 비교해야함
*/
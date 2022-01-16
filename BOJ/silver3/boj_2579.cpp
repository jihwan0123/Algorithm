// 2579. 계단 오르기
#include <bits/stdc++.h>
using namespace std;
int arr[302];
int d[302]; // d[i] : i 번째까지 밟지 않는 계단의 합
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n;
  cin >> n;
  int total = 0;
  for (int i = 1; i <= n; i++) {
    cin >> arr[i];
    total += arr[i];
  }
  d[1] = arr[1];
  d[2] = arr[2];
  d[3] = arr[3];
  for (int i = 4; i < n; i++)
    // i-3번째를 밟지 않거나, i-2번째를 밟지 않아야 i 번째 밟지 않을 수 있다.
    d[i] = min(d[i - 2], d[i - 3]) + arr[i];

  // n번째를 밟으려면, n-1, n-2번째를 밟지 않아야함
  cout << total - min(d[n - 1], d[n - 2]);
}

/*
int arr[302];
int d[302][3]; // d[i][j] : j개의 연속된 계단을 밟고, i번째 계단일때 합
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n;
  cin >> n;
  for (int i = 1; i <= n; i++)
    cin >> arr[i];

  if (n == 1) {
    cout << arr[1];
    return 0;
  }
  d[1][1] = arr[1];
  d[1][2] = 0;
  d[2][1] = arr[2];
  d[2][2] = arr[1] + arr[2];
  for (int i = 3; i <= n; i++) {
    d[i][1] = max(d[i - 2][1], d[i - 2][2]) + arr[i];
    d[i][2] = d[i - 1][1] + arr[i];
  }

  cout << max(d[n][1], d[n][2]);
}
*/
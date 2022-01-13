// 15688. 수 정렬하기 5
#include <bits/stdc++.h>
using namespace std;
int arr[2000002];
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n;
  cin >> n;
  // vector<int> nums;
  // while (n--) {
  //   int x;
  //   cin >> x;
  //   nums.push_back(x);
  // }
  // sort(nums.begin(), nums.end());
  // for (int a : nums)
  //   cout << a << '\n';

  // counting sort
  for (int i = 0; i < n; i++) {
    int x;
    cin >> x;
    arr[x + 1000000]++;
  }
  for (int i = 0; i < 2000002; i++)
    while (arr[i]--)
      cout << i - 1000000 << '\n';
}
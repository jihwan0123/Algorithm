#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int arr[10] = {3, 2, 7, 116, 62, 235, 1, 23, 55, 77};
  int n = 10;

  /* 선택정렬
  for (int i = n - 1; i > 0; i--) {
    int mxidx = 0;
    for (int j = n - 1; j <= i; j++) {
      if (arr[mxidx] < arr[j])
        mxidx = j;
    }
    swap(arr[mxidx], arr[i]);
  }
  // max_element 사용
  for (int i = n - 1; i > 0; i--) {
    swap(*max_element(arr, arr + i + 1), arr[i]);
    for (int i = 0; i < 10; i++)
      cout << arr[i] << ' ';
    cout << '\n';
  }
   */

  // 버블정렬
  for (int i = 0; i < n; i++)
    for (int j = 0; j < n - 1; j++) {
      if (arr[j] > arr[j + 1])
        swap(arr[j], arr[j + 1]);
      for (int i = 0; i < 10; i++)
        cout << arr[i] << ' ';
      cout << '\n';
    }
}

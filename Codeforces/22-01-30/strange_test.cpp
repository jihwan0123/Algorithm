// C. Strange Test 
#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int t;
  cin >> t;
  while(t--){
    int a, b;
    cin >> a >> b;
    int ans = b - a;
    // or 연산은 1번만 해야 최소
    for (int i=a; i<b; i++){
      int c = i|b;
      ans = min(ans, (i-a)+(c-b)+1);
    }
    for (int i=b+1; i<=a+b; i++){
      int c = a|i;
      ans = min(ans, (i-b)+(c-i)+1);
    }
    cout << ans << '\n';
  }
}
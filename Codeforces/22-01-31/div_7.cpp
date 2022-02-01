// A. Div. 7
#include <bits/stdc++.h>
using namespace std;
void func(string s){
  int x = s.size();
  if (x==1) {
    cout << 7 << '\n';
    return;
  }
  for (int i=1; i<x; i++){
    for (int j=0; j<=9; j++){
      string tmp = s.substr(0,i) + to_string(j) + s.substr(i+1,x);
      int tp = stoi(tmp);
      if (tp % 7 == 0) {
        cout << tmp << '\n';
        return;
      }
    }
  }
}
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int t;
  cin >> t;
  while(t--) {
    string s;
    cin >> s;
    if (stoi(s)%7 ==0) {
      cout << s << '\n';
      continue;
    }
    func(s);
  }
}
#include <bits/stdc++.h>
using namespace std;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int c;
  cin >> c;
  cout << fixed;
  cout.precision(3);
  while(c--) {
    int n;
    cin >> n;
    vector<int> scores;
    int total = 0;
    for (int i=0; i<n; ++i) {
      int x;
      cin >> x;
      scores.push_back(x);
      total += x;
    }
    double avg = total / static_cast<double>(n);
    int cnt = 0;
    while(!scores.empty()) {
      if ((double)scores.back() > avg) cnt++;
      scores.pop_back();
    }
    cout << (100 * cnt / static_cast<double>(n)) << "%\n";
  }
}
// 11651. 좌표 정렬하기 2
#include <bits/stdc++.h>
using namespace std;

#define X first
#define Y second

bool compare(pair<int, int> a, pair<int, int> b) {
  if (a.Y == b.Y)
    return a.X < b.X;
  return a.Y < b.Y;
}

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n;
  cin >> n;
  vector<pair<int, int>> dots;
  for (int i = 0; i < n; i++) {
    int x, y;
    cin >> x >> y;
    dots.push_back({x, y});
  }

  sort(dots.begin(), dots.end(), compare);
  for (int i = 0; i < n; i++) {
    cout << dots[i].X << ' ' << dots[i].Y << '\n';
  }
}
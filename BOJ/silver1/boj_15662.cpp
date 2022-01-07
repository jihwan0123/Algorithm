// 15662. 톱니바퀴(2)
#include <bits/stdc++.h>
using namespace std;
int t;
string board[1002];
void rotate(int x, int dir)
{
  string tmp = "";
  if (dir == -1) // 반시계
  {
    for (int i = 1; i < 8; i++)
      tmp.push_back(board[x][i]);
    tmp.push_back(board[x][0]);
    board[x] = tmp;
  }
  else // 시계
  {
    tmp.push_back(board[x][7]);
    for (int i = 0; i < 7; i++)
      tmp.push_back(board[x][i]);
    board[x] = tmp;
  }
}
void func(int x, int dir, vector<pair<int, int>> &rotate_topni)
{
  int s = x;
  int e = x;
  int sd = dir;
  int ed = dir;
  while (s > 1)
  {
    if (board[s][6] != board[s - 1][2])
    {
      sd *= -1;
      s--;
      rotate_topni.push_back({s, sd});
    }
    else
      break;
  }
  while (e < t)
  {
    if (board[e][2] != board[e + 1][6])
    {
      ed *= -1;
      e++;
      rotate_topni.push_back({e, ed});
    }
    else
      return;
  }
}
int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> t;
  for (int i = 1; i <= t; i++)
    cin >> board[i];
  int k;
  cin >> k;
  while (k--)
  {
    int x, dir;
    cin >> x >> dir;
    vector<pair<int, int>> topnis;
    topnis.push_back({x, dir});
    func(x, dir, topnis);
    for (auto topni : topnis)
      rotate(topni.first, topni.second);
  }
  int cnt = 0;
  for (int i = 1; i <= t; i++)
    if (board[i][0] == '1')
      cnt++;
  cout << cnt << '\n';
}
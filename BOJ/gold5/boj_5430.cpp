// 5430. AC
#include <bits/stdc++.h>
using namespace std;
int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  int t;
  cin >> t;
  while (t--)
  {
    deque<int> dq;
    string p, x;
    int n;
    cin >> p >> n >> x;
    string num = "0";
    bool rev = false;
    bool error = false;
    // , 로 구분
    for (int i = 1; i < (int)x.size() - 1; i++)
    {
      if (x[i] == ',')
      {
        dq.push_back(stoi(num));
        num = "0";
      }
      else
      {
        num += x[i];
      }
    }
    // 마지막 숫자 추가
    if (num != "0")
      dq.push_back(stoi(num));

    // 입력 수행
    for (char c : p)
    {
      // R이면 reverse
      if (c == 'R')
        rev = !rev;
      // D면 pop
      else if (c == 'D')
      {
        if (dq.empty())
        {
          error = true;
          break;
        }
        if (rev)
          dq.pop_back();
        else
          dq.pop_front();
      }
    }
    if (error)
    {
      cout << "error\n";
    }
    else
    {
      cout << '[';
      if (rev)
      {
        for (int j = dq.size() - 1; j >= 0; j--)
        {
          if (j == 0)
            cout << dq[j];
          else
            cout << dq[j] << ',';
        }
      }
      else
      {
        for (int j = 0; j < dq.size(); j++)
        {
          if (j == (int)dq.size() - 1)
            cout << dq[j];
          else
            cout << dq[j] << ',';
        }
      }
      cout << "]\n";
    }
  }
}
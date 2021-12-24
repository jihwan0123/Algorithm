// 2493. 탑
#include <bits/stdc++.h>
using namespace std;
int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);

  int n;
  cin >> n;
  stack<pair<int, int>> s; // (탑 번호, 탑 높이)

  for (int i = 1; i <= n; i++)
  {
    int d;
    cin >> d;

    // 스택 비어있으면 0 출력
    if (s.empty())
    {
      s.push({i, d});
      cout << 0 << " ";
    }
    else
    {
      while (1) // 더 큰 값 찾을때까지 반복
      {
        // stack의 높이가 현재 탑의 높이보다 크면
        if (s.top().second > d)
        {
          // 출력하고 stack에 삽입
          cout << s.top().first << " ";
          s.push({i, d});
          break;
        }
        // 낮으면 pop해서 버리고 다음값 검사
        else
          s.pop();

        if (s.empty()) // 스택이 빌때까지 큰 값이 없으면 0 출력 후 현재값 삽입
        {
          cout << 0 << " ";
          s.push({i, d});
          break;
        }
      }
    }
  }
  cout << "\n";
}
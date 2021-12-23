// 1406. 에디터
#include <bits/stdc++.h>
using namespace std;
int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  // 입력
  string input;
  cin >> input;

  // 명령 개수
  int m;
  cin >> m;

  list<char> lst;
  for (auto i : input)
    lst.push_back(i);
  auto cursor = lst.end();

  while (m--)
  {
    char op;
    cin >> op;
    if (op == 'L')
    {
      // 커서가 맨 앞이면 무시
      if (cursor != lst.begin())
        cursor--;
    }
    else if (op == 'D')
    {
      // 커서가 맨 뒤면 무시
      if (cursor != lst.end())
        cursor++;
    }
    else if (op == 'B')
    {
      // 커서가 맨 앞이면 무시
      if (cursor != lst.begin())
        // 커서 왼쪽 삭제
        cursor = lst.erase(--cursor);
    }
    else if (op == 'P')
    {
      // 커서 위치에 c 추가
      char c;
      cin >> c;
      lst.insert(cursor, c);
    }
  }
  for (auto ans : lst)
    cout << ans;
}
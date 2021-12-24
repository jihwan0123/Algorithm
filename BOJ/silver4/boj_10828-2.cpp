// 10828. 스택
#include <bits/stdc++.h>
using namespace std;

const int MX = 1000005;
int s[MX];
int pos = 0;

void push(int x)
{
  s[pos++] = x;
}

void pop()
{
  pos--;
}

int top()
{
  return s[pos - 1];
}

int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);

  int n;
  cin >> n;

  while (n--)
  {
    string command;
    cin >> command;
    if (command == "push")
    {
      int data;
      cin >> data;
      push(data);
    }
    else if (command == "pop")
    {
      if (pos <= 0)
        cout << -1 << "\n";
      else
      {
        int x = top();
        cout << x << "\n";
        pop();
      }
    }
    else if (command == "size")
      cout << pos << "\n";
    else if (command == "empty")
    {
      if (pos <= 0)
        cout << 1 << "\n";
      else
        cout << 0 << "\n";
    }
    else if (command == "top")
      if (pos <= 0)
        cout << -1 << "\n";
      else
        cout << top() << "\n";
  }
}
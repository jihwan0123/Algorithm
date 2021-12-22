// 10808. 알파벳 개수
#include <bits/stdc++.h>
using namespace std;

int arr[27];

int main(void)
{
  ios::sync_with_stdio(0);
  cin.tie(0);
  string s;
  cin >> s;
  for (int i = 0; i < s.size(); i++)
    arr[s[i] - 'a']++;

  for (int i = 0; i < 26; i++)
    cout << arr[i] << " ";
}
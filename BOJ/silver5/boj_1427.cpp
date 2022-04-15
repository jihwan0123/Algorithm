#include <bits/stdc++.h>
using namespace std;
int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    string s;
    cin >> s;
    vector<char> v;
    for (int i=0; i<s.size(); i++) {
        v.push_back(s[i]);
    }
    sort(begin(v), end(v), greater<>());
    for (auto& i : v) cout << i;
}
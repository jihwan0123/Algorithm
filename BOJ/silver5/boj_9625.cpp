#include <bits/stdc++.h>
using namespace std;
pair<int,int> d[46];
int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int k;
    cin >> k;
    d[0] = {1, 0};
    d[1] = {0, 1};
    for (int i=2; i<=k; i++) {
        d[i].first = d[i-1].second;
        d[i].second = d[i-1].first + d[i-1].second;
    }
    cout << d[k].first << ' ' << d[k].second;
}
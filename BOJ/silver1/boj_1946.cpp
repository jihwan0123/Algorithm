#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second
int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<pair<int,int>> v;
        for (int i=0; i<n; i++) {
            int a,b;
            cin >> a >> b;
            v.push_back({a,b});
        }
        sort(begin(v), end(v));
        int cnt = 1;
        int minV = v[0].Y;
        for (int i=1;i<n;i++) {
            if (v[i].Y < minV) {
                minV = v[i].Y;
                cnt++;
            }
        }
        cout << cnt << '\n';
    }
}
#include <bits/stdc++.h>
using namespace std;
int d[10001][3]; // d[i][n] : i번째 n개 연속인 경우
int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;
    vector<int> v{0};
    for (int i=0; i<n; i++) {
        int x; cin >> x;
        v.push_back(x);
    }

    if (n < 3) {
        cout << accumulate(v.begin(), v.begin()+n+1,0);
        return 0;
    }
    else {
        d[1][1] = v[1];
        d[1][2] = v[1];

        d[2][0] = v[1];
        d[2][1] = v[2];
        d[2][2] = v[1]+v[2];
    }

    for (int i=3;i<=n;i++) {
        d[i][0] = max(max({d[i-1][0], d[i-1][1], d[i-1][2]}), d[i-2][0]);
        d[i][1] = d[i-1][0] + v[i];
        d[i][2] = d[i-1][1] + v[i];
    }
    for (int i=0; i<=v.size(); i++) {
        cout << d[i][0] << ' ' << d[i][1] << ' '<< d[i][2] << endl;
    }
    cout << max({d[n][0], d[n][1], d[n][2]});
}
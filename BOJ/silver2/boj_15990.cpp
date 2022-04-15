#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const int MOD = 1'000'000'009;
ll d[100001][4]; // d[n][i] : n을 만들때 i로 끝나는 개수
int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;
    d[1][1] = d[2][2] = 1; // 1 : 1, 2: 2
    d[3][1] = d[3][2] = d[3][3] = 1; // 3: 2+1, 1+2, 3
    for (int i=4; i<100001; i++) {
        d[i][1] = (d[i-1][2] + d[i-1][3]) % MOD;
        d[i][2] = (d[i-2][1] + d[i-2][3]) % MOD;
        d[i][3] = (d[i-3][1] + d[i-3][2]) % MOD;
    }
    while (t--) {
        int n;
        cin >> n;
        cout << (d[n][1] + d[n][2] + d[n][3]) % MOD << '\n';
    }
}
#include <bits/stdc++.h>
using namespace std;
int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;
    int cnt{0};
    for (int i=1; i<=n; i++) {
        for (int j=i; j<=n; j++) {
            if ((j*j) == (i*i + n)) cnt++;
        }
    }
    cout << cnt;
}
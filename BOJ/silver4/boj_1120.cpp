#include <bits/stdc++.h>
using namespace std;
int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    string a, b;
    cin >> a >> b;
    int ans = 0;
    int cnt = 0;
    for (int i=0; i<=(b.length()-a.length()); i++) {
        cnt = 0;
        for (int j=0; j<a.length(); j++) 
            if (a[j] == b[i+j]) cnt++;
        ans = max(cnt, ans);
    }
    cout << a.length() - ans;
}
// boj_1052.cpp
// 물병

#include <iostream>

using namespace std;

int n, k, ans;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n >> k;

    // k보다 작으면 추가 안해도 됨
    if (n <= k) {
        cout << 0 << "\n";
        return 0;
    }

    while (true) {
        int cnt = 0;
        int x = n;

        // 2로 나누면서 몇개로 합쳐지는지 체크
        while (x > 0) {
            if (x & 1) {
                cnt++;
            }
            x /= 2;
        }

        if (cnt <= k) {
            cout << ans << "\n";
            break;
        }

        // 1개 추가하면서 체크
        ans++;
        n++;
    }

    return 0;
}
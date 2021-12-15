// boj_4095.cpp
// 최대 정사각형

#include <iostream>
#include <algorithm>
using namespace std;

int n, m;
int arr[1001][1001];
int dp[1001][1001];

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    while (true) {
        cin >> n >> m;
        int ans = 0;

        if (n == 0 && m == 0) break;

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                cin >> arr[i][j];
                dp[i][j] = 0;
            }
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (arr[i][j] == 1) {
                    dp[i][j] = min(dp[i - 1][j - 1], min(dp[i][j - 1], dp[i - 1][j])) + 1;
                    ans = max(dp[i][j], ans);
                }
            }
        }

        cout << ans << "\n";

    }

    return 0;
}

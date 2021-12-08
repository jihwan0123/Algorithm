// boj_13707.cpp
// 합분해 2

#include <iostream>
#define MOD int(1e9)

using namespace std;

int n, k;
long long dp[5001];

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n >> k;
    dp[0] = 1;
    while (k--){
        for (int i = 1; i <=n; i++) {
            dp[i] = (dp[i - 1] + dp[i]) % MOD;
        }
    }


    cout << dp[n];

}
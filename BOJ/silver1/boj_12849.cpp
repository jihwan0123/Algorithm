// boj_12849.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
// 본대 산책

#include <iostream>
#include <cstring>
#define ll long long
#define MOD 1000000007LL
int D;
using namespace std;

ll DP[8] = { 1,0,0,0,0,0,0,0 };

// 이동
void move(ll *DP) {
    ll tmp[8];
    memset(tmp, 0, sizeof(ll) * 8);

    tmp[0] = DP[1] + DP[2];
    tmp[1] = DP[0] + DP[2] + DP[3];
    tmp[2] = DP[0] + DP[1] + DP[3] + DP[4];
    tmp[3] = DP[1] + DP[2] + DP[4] + DP[5];
    tmp[4] = DP[2] + DP[3] + DP[5] + DP[6];
    tmp[5] = DP[3] + DP[4] + DP[7];
    tmp[6] = DP[4] + DP[7];
    tmp[7] = DP[5] + DP[6];

    for (int i = 0; i < 8; i++) {
        tmp[i] %= MOD;
    }
    memcpy(DP, tmp, sizeof(ll) * 8);
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> D;

    // D번 반복
    for (int i = 0; i < D; i++) {
        move(DP);
    }

    cout << DP[0];

    return 0;
}
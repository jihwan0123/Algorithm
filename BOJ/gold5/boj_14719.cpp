// boj_14719.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
// 빗물

#include <iostream>
using namespace std;

int H, W;
int height[501];
int ans;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> H >> W;
    for (int i = 0; i < W; i++) {
        cin >> height[i];
    }
    
    // 양 끝인 0, W-1에는 빗물이 고일 수 없으므로 1 ~ W-2까지
    for (int i = 1; i < W - 1; i++) {
        int left = height[i];
        int right = height[i];
        // 왼쪽 중 최댓값 탐색
        for (int j = 0; j < i; j++) {
            left = max(left, height[j]);
        }
        // 오른쪽 중 최댓값 탐색
        for (int j = i+1; j < W; j++) {
            right = max(right, height[j]);
        }
        // 양쪽중에 더 낮은곳부터 현재높이까지 = 현재칸에 고이는 빗물의 양
        ans += min(left, right) - height[i];
    }
    
    cout << ans;


    return 0;
}
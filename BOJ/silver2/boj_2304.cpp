// boj_2304.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
// 창고 다각형

#include <iostream>
using namespace std;

int n;
int l, h;
int height[1001]; // 높이 저장
int maxH, maxL; // 최대 높이일때 높이와 인덱스값
int width; // 최대 가로값
int ans; // 면적

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n;
    for (int i = 1; i <= n; i++) {
        cin >> l >> h;
        // 최대값 저장
        if (h > maxH) {
            maxH = h;
            maxL = l;
        }
        width = max(l, width);
        // l일때 높이 h
        height[l] = h;
    }

    // 지붕 왼쪽일때, height[i+1]이 height[i]보다 작으면 height[i]로 바꾼다.
    for (int i = 1; i < maxL; i++) {
        if (height[i + 1] < height[i]) {
            height[i + 1] = height[i];
        }
    }
    // 지붕 오른쪽일땐 거꾸로
    for (int j = width; j > maxL; j--) {
        if (height[j - 1] < height[j]) {
            height[j - 1] = height[j];
        }
    }
    // 전체 면적 구하기
    for (int k = 1; k <= width; k++) {
        ans += height[k];
    }
    cout << ans;

    return 0;
}
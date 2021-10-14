// boj_17404.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#include <iostream>
#include <algorithm>

using namespace std;

#define MAX_VALUE 1e6
int n;
int RGB[3][1001][3];

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> n;

	for (int i = 1; i <= n; i++) {
		cin >> RGB[0][i][0] >> RGB[1][i][0] >> RGB[2][i][0];
		// RGB[end][n][start] : start(시작컬러)에서 시작해서 end(현재컬러)까지 최소비용
		RGB[0][i][1] = RGB[0][i][2] = RGB[0][i][0];
		RGB[1][i][1] = RGB[1][i][2] = RGB[1][i][0];
		RGB[2][i][1] = RGB[2][i][2] = RGB[2][i][0];
	}

	// 1번 집일때, 같은 번호 아닌건 MAX 값으로 변경
	// 1번집 R로 시작
	RGB[0][1][1] = MAX_VALUE;
	RGB[0][1][2] = MAX_VALUE;
	// 1번집 G로 시작
	RGB[1][1][0] = MAX_VALUE;
	RGB[1][1][2] = MAX_VALUE;
	// 1번집 B로 시작
	RGB[2][1][0] = MAX_VALUE;
	RGB[2][1][1] = MAX_VALUE;



	for (int k = 2; k <= n; k++) {
		for (int l = 0; l < 3; l++) {
			RGB[0][k][l] += min(RGB[1][k - 1][l], RGB[2][k - 1][l]);
			RGB[1][k][l] += min(RGB[0][k - 1][l], RGB[2][k - 1][l]);
			RGB[2][k][l] += min(RGB[0][k - 1][l], RGB[1][k - 1][l]);
		}
	}

	int ans = MAX_VALUE;
	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			// 시작과 끝 같은경우 제외
			if (i == j) continue;
			ans = min(ans, RGB[i][n][j]);
		}
	}
	cout << ans;

	return 0;
}
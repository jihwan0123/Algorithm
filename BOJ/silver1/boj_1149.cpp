// boj_1149.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
// RGB거리

#include <iostream>
#include <algorithm>

using namespace std;

int n;
int RGB[3][1001];

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> n;

	for (int i = 1; i <= n; i++) {
		cin >> RGB[0][i] >> RGB[1][i] >> RGB[2][i];
	}

	// 앞이 다른경우 중에 더 작은거 더해서 갱신
	for (int k = 2; k <= n; k++) {
		RGB[0][k] += min(RGB[1][k - 1], RGB[2][k - 1]);
		RGB[1][k] += min(RGB[0][k - 1], RGB[2][k - 1]);
		RGB[2][k] += min(RGB[0][k - 1], RGB[1][k - 1]);
	}

	// 마지막에서 작은거 출력
	cout << min({ RGB[0][n], RGB[1][n], RGB[2][n] });

	return 0;
}
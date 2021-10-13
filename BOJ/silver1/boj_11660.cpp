// boj_11660.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
// 구간 합 구하기 5

/* 가로만 생각한 경우 368ms
#include <iostream>
using namespace std;

int n, m;
int arr[1025][1025];

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> n >> m;

	for (int i = 1; i <= n; i++) {
		int temp = 0;
		int x = 0;
		for (int j = 1; j <= n; j++) {
			cin >> x;
			temp += x;
			arr[i][j] = temp;
		}
	}
	
	for (int i = 0; i < m; i++) {
		int x1, y1, x2, y2;
		cin >> x1 >> y1 >> x2 >> y2;
		int ans = 0;
		for (int j = x1; j <= x2; j++) {
			ans += (arr[j][y2] - arr[j][y1 - 1]);
		}
		cout << ans << '\n';
	}
}
*/

/* 가로+세로 모두 생각한경우 132ms */
#include <iostream>
using namespace std;

int n, m;
int arr[1025][1025];
int temp;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> n >> m;

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			cin >> temp;
			// arr[i][j] = (1,1)부터 (i, j) 까지 모든 수의 합
			arr[i][j] = arr[i - 1][j] + arr[i][j - 1] - arr[i - 1][j - 1] + temp;
		}
	}

	for (int i = 0; i < m; i++) {
		int x1, y1, x2, y2;
		cin >> x1 >> y1 >> x2 >> y2;
		// 사각형을 그리면, (x1,y1), (x1,y2), (x2,y1), (x2,y2)가 나온다.
		// 제일 큰 사각형(x2,y2)에서 나머지 3개의 사각형들을 빼면 
		// (x1,y1) 부터 (x2,y2) 까지의 합이 나온다.
		cout << arr[x2][y2] - arr[x2][y1-1] - arr[x1-1][y2] + arr[x1-1][y1-1] << '\n';
	}
}

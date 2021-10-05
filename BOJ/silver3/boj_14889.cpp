// boj_14889. 스타트와 링크
#include <iostream>
using namespace std;

int n;
int minV = 987654321;
int arr[20][20];
bool used[20];

void combi(int n, int cnt);

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	// 입력
	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> arr[i][j];
		}
	}

	// 2/n명 뽑기
	for (int i = 0; i <= n/2; i++) {
		used[i] = true;
		combi(i, 1);
		used[i] = false;
	}
	cout << minV;
}

void combi(int cur, int cnt) {
	// 2/n 명 뽑았으면
	if (cnt == n / 2) {
		int a = 0;
		int b = 0;
		// A팀과 B팀 점수 구해서 차이 계산 후 최솟값 갱신
		for (int i = 0; i < n; i++) {
			for (int j = i+1; j < n; j++) {
				if (used[i] && used[j]) {
					a += (arr[i][j] + arr[j][i]);
				}
				else if (!used[i] && !used[j]) {
					b += (arr[i][j] + arr[j][i]);
				}
			}
		}
		minV = min(minV, abs(a-b));
		return;
	}

	// 2/n명 뽑기, cur + 1부터 하면 중복 안됨
	for (int i=cur+1; i < n; i++) {
		if (!used[i]) {
			used[i] = true;
			combi(i, cnt + 1);
			used[i] = false;
		}
	}
}
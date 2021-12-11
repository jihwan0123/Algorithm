// boj_11170.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
// 0의 개수

#include <iostream>
#include <string>


using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int n, m;
		int cnt = 0;
		cin >> n >> m;
		for (int s = n; s <= m; s++) {
			string temp = to_string(s);
			for (auto t : temp) {
				if (t == '0') {
					cnt++;
				}
			}
		}
		cout << cnt << '\n';
	}


	return 0;
}
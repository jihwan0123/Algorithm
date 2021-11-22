// boj_2239.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
// 2239. 스도쿠

#include <iostream>
#include <vector>

using namespace std;

int arr[9][9];
vector<pair<int, int>> blanks;

// 출력
void print_answer() {
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            cout << arr[i][j];
        }
        cout << "\n";
    }
}

// (x,y)에 num 놓을 수 있는지 체크
bool check(int x, int y, int num) {
    // 가로 체크
    for (int i = 0; i < 9; i++) {
        if ((arr[x][i] == num) || (arr[i][y] == num))
            return false;
    }

    // 3*3 체크
    int m = 3 * (x / 3);
    int n = 3 * (y / 3);
    for (int i = m; i < m + 3; i++) {
        for (int j = n; j < n + 3; j++) {
            if (arr[i][j] == num)
                return false;
        }
    }
    return true;
}

// dfs
bool dfs(int cnt) {
    // 빈칸에 다 놨으면 종료
    if (cnt == blanks.size()) {
        print_answer();
        return true;
    }

    int x = blanks[cnt].first;
    int y = blanks[cnt].second;
    // 1부터 9까지 넣어본다.
    for (int n = 1; n < 10; n++) {
        if (check(x, y, n)) {
            // 백트래킹
            arr[x][y] = n;
            if (dfs(cnt + 1)) return true;
            arr[x][y] = 0;
        }
    }
    return false;
}



int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    for (int i = 0; i < 9; i++) {
        string temp;
        cin >> temp;
        for (int j = 0; j < 9; j++) {
            arr[i][j] = temp[j] - '0';
            if (arr[i][j] == 0) {
                blanks.push_back(make_pair(i, j));
            }
        }
    }
    dfs(0);
    return 0;
}
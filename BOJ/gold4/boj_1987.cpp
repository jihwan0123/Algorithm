// boj_1987.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
// 알파벳

#include<iostream>
#include<algorithm>
using namespace std;

int r, c;
int ans;
char arr[21][21];
bool visited[21][21] = {false, };
bool alpha_visited[150] = {false,};

int dx[4] = { 0,0,1,-1 };
int dy[4] = { 1,-1,0,0 };


void dfs(int x, int y, int cnt) {
    ans = max(cnt, ans);
    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if ((nx >= 0) && (nx < c) && (ny >= 0) && (ny < r)) {
            if ((!visited[nx][ny]) && (!alpha_visited[(int)arr[nx][ny]])) {
                alpha_visited[(int)arr[nx][ny]] = true;
                visited[nx][ny] = true;
                dfs(nx, ny, cnt + 1);
                alpha_visited[(int)arr[nx][ny]] = false;
                visited[nx][ny] = false;
            }
        }
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> r >> c;
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            cin >> arr[j][i];
        }
    }

    alpha_visited[(int)arr[0][0]] = true;
    visited[0][0] = true;
    dfs(0, 0, 1);
    cout << ans;
}
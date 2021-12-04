// boj_1743.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
// 음식물 피하기

#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

int n, m, k;
int ans;
int arr[101][101];
bool visited[101][101];
int dx[] = { 0,0,1,-1 };
int dy[] = { 1,-1,0,0 };

void bfs(int a, int b) {
    queue<pair<int, int>> q;
    q.push({ a,b });
    visited[a][b] = true;
    int cnt = 0;
    
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        cnt++;
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx > 0 && nx <= n && ny > 0 && ny <= m && !visited[nx][ny] && arr[nx][ny] == 1) {
                visited[nx][ny] = true;
                q.push({ nx, ny });
            }
        }
    }
    ans = max(cnt, ans);
    return;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n >> m >> k;

    for (int i = 0; i < k; i++) {
        int x, y;
        cin >> x >> y;
        arr[x][y] = 1;
    }

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (!visited[i][j] && arr[i][j] == 1) {
                bfs(i, j);
            }
        }
    }

    cout << ans;
}

// boj_17836.cpp
// 공주님을 구해라!

#include <iostream>
#include <queue>
#include <tuple>

using namespace std;

int n, m, t;
int arr[101][101];
int visited[101][101][2];
int dx[] = { 0,0,1,-1 };
int dy[] = { -1,1,0,0 };

int bfs(int a, int b) {
    queue<tuple<int, int, int>> q;
    q.push({ a,b,0 });

    while (!q.empty()) {
        int x = get<0>(q.front());
        int y = get<1>(q.front());
        int z = get<2>(q.front());
        q.pop();

        // n,m까지 갔으면 종료
        if (x == n && y == m) {
            return visited[x][y][z];
        }

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (1 <= nx && nx <= n && 1 <= ny && ny <= m && visited[nx][ny][z] == 0) {
                // 그람을 들고 있으면
                if (arr[nx][ny] == 1 && z == 1) {
                    visited[nx][ny][z] = visited[x][y][z] + 1;
                    q.push({ nx, ny, z });
                }
                // 그람을 주웠으면 visited[][][1]로 변경
                else if (arr[nx][ny] == 2) {
                    visited[nx][ny][1] = visited[x][y][0] + 1;
                    q.push({ nx, ny, 1 });
                }
                // 그냥 벽이면 z 그대로 이동
                else if (arr[nx][ny] == 0 && visited[nx][ny][z] == 0) {
                    visited[nx][ny][z] = visited[x][y][z] + 1;
                    q.push({ nx, ny, z });
                }
                // t시간 초과하면 종료
                if (visited[nx][ny][z] > t) {
                    return -1;
                }
            }
        }
    }

    return -1;
}


int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n >> m >> t;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            cin >> arr[i][j];
        }
    }
    int ans = bfs(1,1);

    if (ans == -1) {
        cout << "Fail";
    }
    else {
        cout << ans;
    }
}
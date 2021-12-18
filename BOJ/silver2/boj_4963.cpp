// boj_4963.cpp
// 섬의 개수

#include <iostream>
#include <vector>
#include <queue>
#include <cstring>

int w, h;
int lands[51][51];
bool visited[51][51];
int dx[] = { 0,0,1,-1,1,1,-1,-1 };
int dy[] = { 1,-1,0,0,-1,1,1,-1 };

using namespace std;
void bfs(int a, int b) {
    queue<pair<int, int>> q;
    q.push({ a,b });
    visited[a][b] = true;

    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        for (int i = 0; i < 8; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (1 <= nx && nx <= h && 1 <= ny && ny <= w && lands[nx][ny] == 1 && !visited[nx][ny]) {
                visited[nx][ny] = true;
                q.push({ nx,ny });
            }
        }
    }
}


int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    while (true) {
        int ans = 0;

        // 배열 초기화
        memset(lands, 0, sizeof(lands));
        memset(visited, false, sizeof(visited));

        cin >> w >> h;

        // 0 0 이면 종료
        if (w == 0 && h == 0) {
            return 0;
        }

        vector<pair<int, int>> temp;

        for (int i = 1; i <= h; i++) {
            for (int j = 1; j <= w; j++) {
                cin >> lands[i][j];
                if (lands[i][j] == 1)
                    temp.push_back({ i,j });
            }
        }

        // 1인 위치만 탐색
        for (auto t : temp)
        {
            int a = t.first;
            int b = t.second;
            // 방문안했으면 bfs
            if (!visited[a][b]) {
                ans++;
                bfs(a, b);
            }
        }

        cout << ans << "\n";
    }
}
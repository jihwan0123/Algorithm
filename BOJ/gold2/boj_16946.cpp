// boj_16946.cpp
// 벽 부수고 이동하기 4

#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
#define MAX 1001

using namespace std;

int n, m;
int arr[MAX][MAX]; // 입력
int ans[MAX][MAX]; // 정답
pair<int,int> visited[MAX][MAX]; // pair = (인접 칸의 개수, area 구분)
vector<pair<int, int>> walls; // 벽 위치 저장
int chk = 1;

int dx[] = { 0,0,1,-1 };
int dy[] = { -1,1,0,0 };

void bfs(int a, int b) {
    queue<pair<int, int>> q; // bfs 탐색용
    queue<pair<int, int>> change; // 최대값으로 교체하기 위해 좌표 저장
    q.push({ a,b });
    change.push({ a,b });
    int max_cnt = 1; // 인접한 칸의 수
    visited[a][b] = {1, chk};
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (1 <= nx && nx <= n && 1 <= ny && ny <= m && visited[nx][ny].first == 0 && arr[nx][ny] == 0) {
                visited[nx][ny].first = visited[x][y].first + 1;
                max_cnt++;
                change.push({ nx,ny });
                q.push({ nx, ny });
            }
        }
    }
    // 같은 area안에 있는 값들 모두 최대값으로 갱신
    while (!change.empty()) {
        int x = change.front().first;
        int y = change.front().second;
        change.pop();
        visited[x][y].first = max_cnt;
        visited[x][y].second = chk;
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n >> m;

    // 입력 받으면서 벽 위치 저장
    for (int i = 1; i <= n; i++) {
        string temp;
        cin >> temp;
        for (int j = 0; j < m; j++) {
            arr[i][j+1] = temp[j] - '0';
            ans[i][j + 1] = arr[i][j + 1];
            if (arr[i][j+1] == 1) {
                walls.push_back({ i,j+1 });
            }
        }
    }

    // bfs돌면서 pair에 (인접한 칸의 개수, area 구분용 chk) 저장
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (arr[i][j] == 0 && visited[i][j].first == 0) {
                bfs(i, j);
                chk++;
            }
        }
    }
    
    // 벽 돌면서 인접 4칸 체크
    for (auto w : walls) {
        int x = w.first;
        int y = w.second;
        int cnt = 1;
        vector<int> used;
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (1 <= nx && nx <= n && 1 <= ny && ny <= m && arr[nx][ny] == 0) {
                bool check = true;
                // 인접한 칸 중에서 같은 area가 있는지 체크
                for (int j = 0; j < used.size();j++) {
                    if (used[j] == visited[nx][ny].second) {
                        check = false;
                        break;
                    }
                }
                // 이미 체크한 area가 아니면, cnt 더한 후 ans에 저장
                if (check) {
                    cnt += visited[nx][ny].first;
                    used.push_back(visited[nx][ny].second);
                }
            }
        }
        ans[x][y] = cnt;
    }

    // 출력
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            cout << ans[i][j] % 10;
        }
        cout << "\n";
    }

}
// boj_14502.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#include <iostream>
#include <queue>
#include <vector>
#include <cstring>
using namespace std;

int arr[8][8];
int arr_origin[8][8];
int n, m;
int ans = 0;
int free_cells = 0;
vector<pair<int, int>> virus_list;
vector<pair<int, int>> free_list;

int dx[4] = {0,1,-1,0};
int dy[4] = {1,0,0,-1};

int bfs(int x, int y) {
    queue<pair<int, int>> q;
    q.push(make_pair(x,y));
    int a = 0;
    int b = 0;
    int cnt = 0;
    while (!q.empty()) {
        pair<int, int> cur = q.front();
        q.pop();
        a = cur.first;
        b = cur.second;
        cnt++;
        for (int i = 0; i < 4; i++) {
            int nx = a + dx[i];
            int ny = b + dy[i];
            if ((0 <= nx) && (nx < n) && (0 <= ny) && (ny < m) && (arr[nx][ny] == 0)) {
                arr[nx][ny] = 2;
                q.push(make_pair(nx, ny));
            }
        }
    }
    return cnt-1;
}


void make_walls(int cnt) {
    // 3개 벽 세웠으면 bfs로 확인
    if (cnt == 3) {
        int temp = 0; 
        for (auto virus : virus_list) {
            // 바이러스 퍼진 개수 체크
            temp += bfs(virus.first, virus.second);
        }
        // 빈칸 - 바이러스 퍼진 개수 - 벽으로 바꾼 3칸 = 안전지역
        ans = max(free_cells - temp - 3, ans);
        // 원본 복사
        memcpy(arr, arr_origin, sizeof(arr));
        return;
    }
    else {
        // 빈 칸 위치 돌면서 3개 고르기
        for (auto free : free_list) {
            int i = free.first;
            int j = free.second;
            if (arr[i][j] == 1)
                continue;
            arr[i][j] = 1;
            arr_origin[i][j] = 1;
            make_walls(cnt + 1);
            arr[i][j] = 0;
            arr_origin[i][j] = 0;
        }
    }
    return;
}


int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> arr[i][j];
            arr_origin[i][j] = arr[i][j];
            if (arr[i][j] == 0) { // 빈 칸 갯수와 좌표 저장
                free_cells++;
                free_list.push_back(make_pair(i, j));
            }
            else if (arr[i][j] == 2) { // 바이러스 좌표 저장
                virus_list.push_back(make_pair(i, j));
            }
        }
    }
    make_walls(0);
    cout << ans;

    return 0;
}
// boj_21610.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
// 마법사 상어와 비바라기 

#include <iostream>
#include <queue>
#include <cstring>
using namespace std;

int n, m, ans;
int arr[51][51];
bool is_removed[51][51];
int d[100];
int s[100];

int dx[9] = {0, 0, -1, -1, -1, 0, 1, 1, 1};
int dy[9] = {0, -1, -1, 0, 1, 1, 1, 0, -1};
int dx2[4] = {1,1,-1,-1};
int dy2[4] = {1,-1,1,-1};
queue<pair<int, int>> clouds;

void move_cloud(int a, int b) {
    // 구름 전체 이동
    while (!clouds.empty()) {
        int cloud_x = clouds.front().first;
        int cloud_y = clouds.front().second;
        clouds.pop();
        // a방향으로 b만큼 이동
        int nx = cloud_x + (b * dx[a]);
        int ny = cloud_y + (b * dy[a]);
        // index 맞추기
        if (nx > n) {
            nx = nx % n;
            if (nx == 0) {
                nx = n;
            }
        }
        else if (nx < 1) {
            nx = n - abs(nx % n);
        }

        if (ny > n) {
            ny = ny % n;
            if (ny == 0) {
                ny = n;
            }
        }
        else if (ny < 1) {
            ny = n - abs(ny % n);
        }
        is_removed[nx][ny] = true; // 구름제거
    }

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (is_removed[i][j]) {
                arr[i][j]++; // 비내리기
                clouds.push(make_pair(i, j)); // 물복사 버그 할 곳
            }
        }
    }
    // 물복사 버그
    while (!clouds.empty()) {
        int x = clouds.front().first;
        int y = clouds.front().second;
        clouds.pop();
        int cnt = 0;
        for (int i = 0; i < 4; i++){
            int nx = x + dx2[i];
            int ny = y + dy2[i];
            if ((0 < nx) && (nx <= n) && (0 < ny) && (ny <= n) && (arr[nx][ny] > 0)) {
                cnt++;
            }
        }
        arr[x][y] += cnt;
    }
    // 구름 생성
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if ((arr[i][j] >= 2) && (!is_removed[i][j])) {
                clouds.push(make_pair(i, j));
                arr[i][j] -= 2;
            }
        }
    }
    return;
}


int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> m;
    clouds.push(make_pair(n, 1));
    clouds.push(make_pair(n, 2));
    clouds.push(make_pair(n-1, 1));
    clouds.push(make_pair(n-1, 2));
    
    // 입력
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            cin >> arr[i][j];
        }
    }
    for (int k = 0; k < m; k++) {
        cin >> d[k] >> s[k];
    }
    
    // m번 명령 실행
    for (int i = 0; i < m; i++) {
        move_cloud(d[i], s[i]); // 명령 실행
        memset(is_removed, false, sizeof(is_removed)); // 구름 제거 배열 초기화
    }
    // 구름 갯수 세기
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (arr[i][j] > 0) {
                ans += arr[i][j];
            }
        }
    }
    cout << ans;
}
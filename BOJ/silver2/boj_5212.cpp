// boj_5212.cpp
// 지구 온난화

#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

int r, c;
char map[11][11];

vector<pair<int, int>> ground;
vector<pair<int, int>> sea;

int dx[] = { 0,0,1,-1 };
int dy[] = { 1,-1,0,0 };

int min_r, max_r, min_c, max_c;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> r >> c;

    // 땅 저장
    for (int i = 1; i <= r; i++) {
        for (int j = 1; j <= c; j++) {
            cin >> map[i][j];
            if (map[i][j] == 'X') {
                ground.push_back({ i,j });
            }
        }
    }

    // 50년 후 바다로 변하는 곳 찾기
    for (auto g : ground) {
        int x = g.first;
        int y = g.second;
        int cnt = 0;
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (1 <= nx && nx <= r && 1 <= ny && ny <= c) {
                if (map[nx][ny] == '.')
                    cnt++;
            }
            else {
                cnt++;
            }
        }
        if (cnt >= 3) {
            sea.push_back({ x,y });
            continue;
        }
    }

    for (auto s : sea) {
        map[s.first][s.second] = '.';
    }

    // 최대 직사각형 찾기
    min_r = r;
    min_c = c;
    max_r = max_c = 1;

    for (int i = 1; i <= r; i++) {
        for (int j = 1; j <= c; j++) {
            if (map[i][j] == 'X') {
                min_r = min(min_r, i);
                min_c = min(min_c, j);
                max_r = max(max_r, i);
                max_c = max(max_c, j);
            }
        }
    }

    // 출력
    for (int i = min_r; i <= max_r; i++) {
        for (int j = min_c; j <= max_c; j++) {
            cout << map[i][j];
        }
        cout << "\n";
    }
}
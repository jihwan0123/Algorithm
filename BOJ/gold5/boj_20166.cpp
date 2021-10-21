// boj_20166.cpp 
// 문자열 지옥에 빠진 호석

#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
#include <map>

using namespace std;

int N, M, K;
int nx, ny;
int MAX_LENGTH;
int dx[8] = { 0,0,-1,1,1,1,-1,-1 };
int dy[8] = { 1,-1,0,0,1,-1,1,-1 };
char arr[11][11];
vector<string> god;
map<string, int> mp;
string s;

void dfs(int x, int y) {
    // 찾는 문자열 최대길이보다 길면 종료
    if (s.length() > MAX_LENGTH) return;

    // map에 s가 있으면 일치하면 +1
    auto iter = mp.find(s);
    if (iter != mp.end()) {
        iter->second++;
    }

    // 8방향으로 dfs 진행
    for (int i = 0; i < 8; i++) {
        nx = x + dx[i];
        ny = y + dy[i];
        if (nx < 0) nx += N;
        else if (nx >= N) nx -= N;
        if (ny < 0) ny += M;
        else if (ny >= M) ny -= M;
        s.push_back(arr[nx][ny]);
        dfs(nx, ny);
        s.pop_back();
    }
}


int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> N >> M >> K;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> arr[i][j];
        }
    }

    // 신이 좋아하는 문자열 저장
    for (int i = 0; i < K; i++) {
        string x;
        cin >> x;
        god.push_back(x);
        mp.insert(make_pair(x, 0));
        int s = x.size();
        MAX_LENGTH = max(MAX_LENGTH, s);
    }

    // 각 좌표마다 dfs 시작해서 개수 체크
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            s.push_back(arr[i][j]);
            dfs(i, j);
            s.pop_back();
        }
    }

    // map에 저장된 개수 차례로 출력
    for (int i = 0; i < K; i++) {
        cout << mp[god[i]] << "\n";
    }

}
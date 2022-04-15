#include <bits/stdc++.h>
using namespace std;

int arr[201][201];
int dx[] = {0,0,1,-1};
int dy[] = {1,-1,0,0};

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, k;
    cin >> n >> k;
    queue<pair<int,int>> q;
    vector<pair<int,pair<int,int>>> tmp;

    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            cin >> arr[i][j];
            if (arr[i][j] > 0) tmp.push_back({arr[i][j],{i,j}});
        }
    }
    sort(tmp.begin(), tmp.end(), [](
        pair<int,pair<int,int>> a, pair<int,pair<int,int>> b) {return a.first > b.first;});
    while(!tmp.empty()) {
        q.push(tmp.back().second);
        tmp.pop_back();
    }
        

    int s, x, y;
    cin >> s >> x >> y;
    int cnt{0};
    while(!q.empty()) {
        int a, b;
        tie(a,b) = q.front();
        q.pop();
        for (int i=0; i<4; i++) {
            int nx = a + dx[i];
            int ny = b + dy[i];
            if (0 > nx || nx >= n || 0 > ny || ny >= n) continue;
            if (arr[nx][ny] != 0) continue;
            arr[nx][ny] = arr[a][b];
            tmp.push_back({arr[nx][ny],{nx, ny}});
        }
        if (q.empty()) {
            sort(tmp.begin(), tmp.end(), [](
                pair<int,pair<int,int>> a, pair<int,pair<int,int>> b) {return a.first > b.first;});
            while(!tmp.empty()) {
                q.push(tmp.back().second);
                tmp.pop_back();
            }
            cnt++;
        }
        if (cnt >= s) break;
    }
    cout << arr[x-1][y-1];
}
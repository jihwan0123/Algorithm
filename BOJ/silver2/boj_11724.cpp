#include <iostream>
#include <queue>
#include <vector>
using namespace std;

bool arr[1001][1001];
bool visited[1001];
int n, m, cur;

vector<int> adj[1001]; // [[] [] [] [] [] [] ... []]
queue<int> q; // []

void dfs(int num);
void bfs(int num);

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> m;
    int cnt = 0;

    if (m == 0) {
        cout << 0;
        return 0;
    }
    if (m == n * (n - 1) / 2) {
        cout << 1;
        return 0;
    }

    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }


    for (int j = 1; j <= n; j++) {
        if (!visited[j]) {
            // bfs(j);
            dfs(j);
            cnt += 1;
        }
    }
    cout << cnt;
}

void dfs(int x) {
    visited[x] = true;
    for (int i: adj[x]) {
        if (!visited[i]) {
            dfs(i);
        }
    }
}

void bfs(int x) {
    q.push(x);
    visited[x] = true;
    while (!q.empty()) {
        cur = q.front();
        q.pop(); // pop은 return 없음
        for (int i: adj[cur]) {
            if (!visited[i]) {
                q.push(i);
                visited[i] = true;
            }
        }
    }
}
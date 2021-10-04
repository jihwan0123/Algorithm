#include <iostream>
using namespace std;

int arr[1000];
int visited[1000];
void dfs(int n);

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        int n, ans = 0;
        cin >> n;
        for (int j = 1; j <= n; j++) {
            cin >> arr[j];
            visited[j] = 0;
        }
        for (int k = 1; k <= n; k++) {
            if (visited[k] == 0) {
                ans += 1;
                dfs(k);
            }
        }
        cout << ans << '\n';
    }
}

void dfs(int n) {
    visited[n] = 1;

    int x;
    x = arr[n];
    if (visited[x] == 0) {
        dfs(x);
    }
    else {
        return;
    }
}
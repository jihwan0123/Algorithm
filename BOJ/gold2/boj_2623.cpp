// boj_2623.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
// 음악프로그램

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int N, M;
vector<int> graph[1001];
int indegree[1001];
vector<int> res;

void topology_sort() {
    queue<int> q;

    for (int i = 1; i <= N; i++) {
        if (indegree[i] == 0) {
            q.push(i);
        }
    }

    while (!q.empty()) {
        int now = q.front();
        q.pop();
        res.push_back(now);

        for (int j : graph[now]) {
            indegree[j]--;
            if (indegree[j] == 0) {
                q.push(j);
            }
        }
    }

    // 정렬 불가능하면 0
    if (res.size() != N) {
        cout << 0;
        return;
    }

    for (int r: res) {
        cout << r << '\n';
    }
    
    return;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> N >> M;

    for (int i = 0; i < M; i++) {
        int num, prev, cur;
        cin >> num;
        for (int j = 0; j < num; j++) {
            cin >> cur;
            if (j == 0) {
                prev = cur;
            }
            else {
                graph[prev].push_back(cur);
                indegree[cur]++;
                prev = cur;  
            }
        }
    }

    topology_sort();

    return 0;
}
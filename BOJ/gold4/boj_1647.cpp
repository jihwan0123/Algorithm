#include<iostream>
#include<vector>
#include<algorithm>
#include<numeric>

using namespace std;

int n, m, answer;
int parent[100001];
vector <pair<int, pair<int, int>>> edges;
vector<int> v;

// 부모찾기
int find_parent(int x)
{
    if (x == parent[x]) return x;
    return parent[x] = find_parent(parent[x]);
}

// 연결하기
void union_find(int x, int y)
{
    x = find_parent(x);
    y = find_parent(y);

    if (x == y) return;
    parent[y] = x;
}

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    // 입력
    cin >> n >> m;
    for (int i = 0; i < m; i++)
    {
        int a, b, c;
        cin >> a >> b >> c;
        edges.push_back(make_pair(c, make_pair(a, b)));
    }

    // 가중치 작은것부터 정렬
    sort(edges.begin(), edges.end());

    // 각자 자기 자신한테 연결
    for (int i = 1; i <= n; i++) {
        parent[i] = i;
    }

    // 간선 전체 반복하면서
    for (int i = 0; i < edges.size(); i++)
    {
        int weight = edges[i].first;
        int first_node = edges[i].second.first;
        int second_node = edges[i].second.second;
        
        // 두 노드가 사이클을 이루는지 체크
        if (find_parent(first_node) != find_parent(second_node)) {
            // 연결
            union_find(first_node, second_node);
            // 가중치 저장
            v.push_back(weight);
        }
    }

    // 제일 큰것 제외하고 더한다.
    cout << accumulate(v.begin(), v.end()-1, 0);

    return 0;
}
#include <string>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;
int visited[20001];
vector<int> v[20001];
int maxV;

void bfs(int s){
    queue<int> q;
    q.push(s);
    
    while(!q.empty()){
        int cur = q.front();
        q.pop();
        for (auto i: v[cur]){
            if (visited[i] == 0 && i != 1) {
                visited[i] = visited[cur] + 1;
                q.push(i);
                maxV = max(maxV, visited[i]);
            } 
        }
    }
}

int solution(int n, vector<vector<int>> edge) {
    int answer = 0;
    for (auto e: edge){
        v[e[0]].push_back(e[1]);
        v[e[1]].push_back(e[0]);
    }
    bfs(1);
    
    for (int i=1; i<=n; i++){
        if(visited[i] == maxV){
            answer++;
        }
    }
    return answer;
}
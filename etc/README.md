# C++ 정리

[바킹독의 실전 알고리즘 강의](https://www.youtube.com/playlist?list=PLtqbFd2VIQv4O6D6l9HcD732hdrnYb6CY) 보면서 기초부터 다시 정리



### STL (Standard Template Library)

- STL을 함수 인자로 넘길 때
  - ```cpp
    void func1 (vector<int> v){
        v[10] = 7;
    }
    int main(void) {
        vector<int> v(100);
        func1(v);
        cout << v[10]; // 0
    }
    
  - **STL을 함수인자로 보내면 복사본을 넘기기 때문에 원본이 바뀌지 않는다.**
  
  - ```cpp
    bool cmp1(vector<int> v1, vector<int> v2, int idx){
        return v1[idx] > v2[idx];
    }
    bool cmp2(vector<int>& v1, vector<int>& v2, int idx){
        return v1[idx] > v2[idx];
    }
    ```
  
    - cmp1은 n개의 원소를 복사하기 때문에 시간복잡도가 O(n)이 된다.
    - cmp2는 참조자(&)를 이용하여 원본을 참조하기 때문에 O(1)



### 표준입출력

- 공백이 포함된 문자열을 받아야 하는 경우 (getline 사용)

```cpp
// 1. scanf의 옵션
char a1[10];
scanf("%[^\n\]", a1);

// 2. gets 함수 (보안상의 이유로 C++14 이상에서는 제거됨)
char a2[10];
gets(a2);
puts(a2);

// 3. getline 함수
string s;
getline(cin, s);
cout << s;
```

- cin, cout에서는 `ios::sync_with_stdio(0), cin.tie(0)` 를 넣어야 시간초과를 막을 수 있다.
  - C++ stream과 C stream의 동기화를 끊는 것
  - `cin.tie(0)` : 원래 입력 받기 전에 cout버퍼를 비우지만 문제풀이에서는 입출력 순서가 중요하지 않으므로 버퍼를 비우지 않도록 하는 코드

- endl : 개행문자 출력 후 버퍼 비우기 때문에 사용금지



### 배열의 성질

> 배열 : 메모리 상에 원소를 연속하게 배치한 자료구조

1. O(1)에 k번째 원소를 확인 / 변경 가능
2. 추가적으로 소모되는 메모리의 양(=overhead)가 거의 없음
3. Cache hit rate가 높음
4. 메모리 상에 연속한 구간을 잡아야 해서 할당에 제약이 걸림

- 임의의 위치의 원소 확인 / 변경 / 추가 O(1)
- 마지막 원소 제거 : O(1)
- 임의의 위치의 원소 추가/제거 : O(n)
  - 원소를 하나씩 밀어야함



- **사용 팁**

```cpp
int a[21];
int b[21][21];

// 1. memset (cstring 헤더)
// 실수할 여지가 많아서 비추천
memset(a, 0, sizeof a);
memset(b, 0, sizeof b);

// 2. for
for (int i = 0; i < 21; i++){
    a[i] = 0;
}
for (int i = 0; i < 21; i++){
    for (int j = 0; j < 21; j++){
        b[i][j] = 0;
    }
}

// 3. fill
fill(a, a+21, 0);
for (int i = 0; i < 21; i++)
    fill(b[i], b[i]+21, 0);
```



### vector

```cpp
#include <bits/stdc++.h>
using namespace std;

int main(void) {
  vector<int> v1(3, 5); // {5,5,5};
  cout << v1.size() << '\n'; // 3
  v1.push_back(7); // {5,5,5,7};

  vector<int> v2(2); // {0,0};
  v2.insert(v2.begin()+1, 3); // {0,3,0};

  vector<int> v3 = {1,2,3,4}; // {1,2,3,4}
  v3.erase(v3.begin()+2); // {1,2,4};

  vector<int> v4; // {}
  v4 = v3; // {1,2,4}
  cout << v4[0] << v4[1] << v4[2] << '\n';
  v4.pop_back(); // {1,2}
  v4.clear(); // {}
}
```

- insert, erase : O(n)
- push_back, pop_back : O(1)
- push_front, pop_front : O(n)
- `=` 사용시 deep copy 발생



```cpp
vector<int> v1 = {1,2,3,4,5,6};

// 1. range-based for loop (since C++11)
for (int e : v1)
    cout << e << ' ';
// for (int& e) 라고 쓰면 원본을 for문 안에서 바꿀 수 있음

// 2. not bad
for (int i=0; i < v1.size(); i++)
    cout << v1[i] << ' ';

// 3. WRONG
for (int i=0; i <= v1.size()-1; i++)
    cout << v1[i] << ' ';
```

- vector의 size 메소드는 unsigned int 반환하기 때문에 (unsigned int)0 - (int)1 은 -1이 아니라 overflow가 발생한다.



### [연결리스트](https://www.youtube.com/watch?v=C6MX5u7r72E)

- 성질

1. k번째 원소를 확인/변경하기 위해 O(k)가 필요
2. 임의의 위치에 원소를 추가/임의 위치의 원소 제거는 O(1)
3. 원소들이 메모리 상에 연속해있지 않아 Cache hit rate가 낮지만 할당이 다소 쉬움

- 종류

1. 단일 연결 리스트
   - 다음 원소만 저장
2. 이중 연결 리스트
   - 이전 원소까지 저장 (메모리를 더 씀)
3. 원형 연결 리스트
   - 처음과 끝이 연결되어 있음



|                                  | 배열 | 연결 리스트 |
| :------------------------------: | :--: | :---------: |
|        k번째 원소의 접근         | O(1) |    O(k)     |
|    임의 위치에 원소 추가/제거    | O(n) |    O(1)     |
|         메모리 상의 배치         | 연속 |   불연속    |
| 추가적으로 필요한 공간(Overhead) |  -   |    O(n)     |



#### STL list

- iterator가 주소 역할
- c++ 11 이상에서는 `auto t = L.begin()`
- erase 는 제거한 다음 위치 반환

```cpp
#include <bits/stdc++.h>
using namespace std;

int main(void) {
  list<int> L = {1,2}; // 1 2
  list<int>::iterator t = L.begin(); // t는 1을 가리키는 중
  L.push_front(10); // 10 1 2
  cout << *t << '\n'; // t가 가리키는 값 = 1을 출력
  L.push_back(5); // 10 1 2 5
  L.insert(t, 6); // t가 가리키는 곳 앞에 6을 삽입, 10 6 1 2 5
  t++; // t를 1칸 앞으로 전진, 현재 t가 가리키는 값은 2
  t = L.erase(t); // t가 가리키는 값을 제거, 그 다음 원소인 5의 위치를 반환
                  // 10 6 1 5, t가 가리키는 값은 5
  cout << *t << '\n'; // 5
    
  // c++ 11 이상
  for(auto i : L) cout << i << ' ';
  cout << '\n';
  // c++ 11 미만
  for(list<int>::iterator it = L.begin(); it != L.end(); it++)
    cout << *it << ' ';
}
```



#### 손코딩 문제

1. 원형 연결 리스트 내의 임의의 노드 하나가 주어졌을 때 해당 List의 길이를 효율적으로 구하는 방법?
   - 동일한 노드가 나올때까지 계속 다음 노드로 가면 됨.
     - 공간복잡도 O(1)
     - 시간복잡도 O(n)
2. 중간에 만나는 두 연결리스트의 시작점들이 주어졌을 때 만나는 지점을 구하는 방법?
   - 일단 두 시작점 각각에 대해 끝까지 진행하여 각 길이를 구한다.
   - 그 후, 두 시작점으로 돌아와서 더 긴쪽을 앞으로 당겨서 두 시작점이 만날 때까지 동시에 한칸씩 당기면 된다.
     - 공간복잡도 O(1)
     - 시간복잡도 O(A+B)
3. 주어진 연결 리스트 안에 사이클이 있는지 판단하라
   - Floyd's cycle-finding algorithm
   - 한칸씩 이동하는 커서와 두칸씩 이동하는 커서를 동일한 시작점에서 출발하면 사이클이 있으면 무조건 만나게 된다.
     - 공간복잡도 O(1)
     - 시간복잡도 O(n)



### [스택](https://www.youtube.com/watch?v=0DsyCXIN7Wg)

- 정의와 성질
  - 한쪽 끝에서만 원소를 넣거나 뺄 수 있는 자료구조
  - FILO (First-In-Last-Out)
  - 원소의 추가/제거/상단 원소 확인 O(1)
  - 제일 상단이 아닌 나머지 원소는 확인/변경 원칙적으로 불가능

```cpp
#include <bits/stdc++.h>
using namespace std;

int main(void) {
  stack<int> S;
  S.push(10); // 10
  S.push(20); // 10 20
  S.push(30); // 10 20 30
  cout << S.size() << '\n'; // 3
  if(S.empty()) cout << "S is empty\n";
  else cout << "S is not empty\n"; // S is not empty
  S.pop(); // 10 20
  cout << S.top() << '\n'; // 20
  S.pop(); // 10
  cout << S.top() << '\n'; // 10
  S.pop(); // empty
  if(S.empty()) cout << "S is empty\n"; // S is empty
  cout << S.top() << '\n'; // runtime error 발생
}
```

- push, pop. top, empty, size



#### [큐](https://www.youtube.com/watch?v=D_fwSy5tRAY&list=PLtqbFd2VIQv4O6D6l9HcD732hdrnYb6CY&index=7&t=5s)

- 정의와 성질
  - FIFO (First-In-First-Out)
  - 원소의 추가, 제거 O(1)
  - 제일 앞, 뒤 원소 확인 O(1)
  - 제일 앞 뒤가 아닌 나머지 원소들의 확인/변경이 원칙적으로 불가능
- head, tail이 MAX일때 0으로 바꿔주면 원형 큐
- STL queue
  - push, pop, front, back, empty, size



#### [덱](https://www.youtube.com/watch?v=0mEzJ4S1d8o&list=PLtqbFd2VIQv4O6D6l9HcD732hdrnYb6CY&index=8&t=2s)

- 정의와 성질
  - Double Ended Queue
  - 양쪽 끝에서 삽입과 삭제가 가능한 자료구조
  - 원소 추가/제거 O(1)
  - 제일 앞 뒤의 원소확인 O(1)
  - 제일 앞/뒤가 아닌 나머지 원소들의 확인/변경이 원칙적으로 불가능
    - STL deque에서는 인덱스로 원소 접근 가능
- head, tail의 초기값이 배열의 중간값
- STL deque
  - push_front, push_back, pop_front, pop_back
  - insert, erase, index접근 가능 (vector와 유사함)



#### [BFS](https://www.youtube.com/watch?v=ftOmGdm95XI&list=PLtqbFd2VIQv4O6D6l9HcD732hdrnYb6CY&index=10)

- 너비 우선 탐색(Breadth First Search)
- 다차원 배열에서 각 칸을 방문할 때 너비를 우선으로 방문하는 알고리즘


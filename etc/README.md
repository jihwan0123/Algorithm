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
- 큐 사용



#### [DFS](https://www.youtube.com/watch?v=93jy2yUYfVE&list=PLtqbFd2VIQv4O6D6l9HcD732hdrnYb6CY&index=11)

- 깊이 우선 탐색 (Depth First Search)
- 다차원 배열에서 각 칸을 방문할 때 깊이를 우선으로 방문하는 알고리즘
- 스택 사용



#### [재귀](https://www.youtube.com/watch?v=8vDDJm5EewM&list=PLtqbFd2VIQv4O6D6l9HcD732hdrnYb6CY&index=12&t=709s)

- 하나의 함수에서 자기 자신을 다시 호출해 작업을 수행하는 알고리즘
- **재귀 함수의 조건**
  - 특정 입력에 대해서는 자기 자신을 호출하지 않고 종료되어야 함 (base condition)
  - 모든 입력은 base condition으로 수렴해야 함
- **재귀에 대한 정보**
  - 함수의 인자로 어떤 것을 받고 어디까지 계산 후 자기 자신에게 넘겨줄 지 명확하게 정해야 함
  - 모든 재귀 함수는 반복문만으로 동일한 동작을 하는 함수를 만들 수 있음
  - 재귀는 반복문으로 구현했을 때에 비해 코드가 간결하지만 메모리/시간에서는 손해를 봄
  - 한 함수가 자기 자신을 여러 번 호출하면 비효율적일 수 있음
  - 재귀함수가 자기 자신을 부를 때 스택 영역에 계속 누적이 됨 (메모리 구조)



#### [백트래킹](https://www.youtube.com/watch?v=Enz2csssTCs&list=PLtqbFd2VIQv4O6D6l9HcD732hdrnYb6CY&index=13&t=162s)

- 현재 상태에서 가능한 모든 후보군을 따라 들어가며 탐색하는 알고리즘

- [STL next_permutation](https://www.cplusplus.com/reference/algorithm/next_permutation/)

  - algorithm 헤더에 있음
  
  - ```cpp
    int a[3] = {1,2,3};
    do {
        for (int i = 0; i < 3; i++)
            cout << a[i];
        cout << '\n';
    } while (next_permutation(a,a+3))
    /*
    123
    132
    213
    231
    312
    321
    */
    ```

  - 마지막이어서 다음 순열이 존재하지 않으면 false 반환

  - 사전순으로 반환, 중복이 있어도 사전순 결과 반환

    - 5,2,3 => ({5,2,3}, {5,3,2})

  - 조합이 필요하다면?
  
    - ```cpp
      int b[4] = {0, 0, 1, 1};
      do
      {
          for (int i = 0; i < 4; i++)
              if (b[i] == 0)
                  cout << i + 1;
          cout << '\n';
      } while (next_permutation(b, b + 4));
      /*
        12
        13
        14
        23
        24
        34
      */
      ```
  
    - 다음과 같이 사용 가능



#### [정렬 I](https://www.youtube.com/watch?v=59fZkZO0Bo4&list=PLtqbFd2VIQv4O6D6l9HcD732hdrnYb6CY&index=15)

- 선택 정렬
  - 최댓값 or 최솟값 찾아서 들어갈 자리에 정렬
  - O(n^2)

```cpp
int arr[10] = {3, 2, 7, 116, 62, 235, 1, 23, 55, 77};
int n = 10;
for (int i = n - 1; i > 0; i--) {
  int mxidx = 0;
  for (int j = 1; j <= i; j++) {
    if (arr[mxidx] < arr[j])
      mxidx = j;
  }
  swap(arr[mxidx], arr[i]);
}

for (int i = n - 1; i > 0; i--) {
  swap(*max_element(arr, arr + i + 1), arr[i]);
}
```

- 버블 정렬
  - 인접한 두 원소 비교
  - O(n^2)

```cpp
for (int i=0;i<n;i++)
    for (int j=0;j<n-1-i;j++)
        if (arr[j] > arr[j+1])
            swap(arr[j], arr[j+1]);
```



- 병합정렬 (Merge sort)
  - O(n*logn)
  - 리스트를 2개로 나눠서(분할) 정렬한 후 합친다(합병). (재귀)
  - Stable sort
    - 정렬 후에도 순서가 유지되는 성질
- 퀵정렬 (Quick sort)
  - O(n*logn), 최악의 경우 O(n^2)
  - 재귀적으로 구현
  - pivot을 잡아서 pivot 왼쪽엔 작은원소, 오른쪽엔 큰원소 저장
  - 추가적인 공간 없이(in-place sort) 배열 안에서의 자리바꿈만으로 해결이 되기 때문에 cache hit rate가 높음

|                                   | Merge sort | Quick Sort                                                  |
| --------------------------------- | ---------- | ----------------------------------------------------------- |
| 시간복잡도                        | O(NlogN)   | 평균 O(NlogN), 최악 O(N^2) 평균적으로 <br />Merge 보다 빠름 |
| 추가적으로 필요한 공간 (Overhead) | O(N)       | O(1)                                                        |
| Stable Sort 여부                  | O          | X                                                           |

#### [정렬 II](https://www.youtube.com/watch?v=dq5t1woLJMw&list=PLtqbFd2VIQv4O6D6l9HcD732hdrnYb6CY&index=16&t=4s)

- Counting Sort

  - 수의 범위가 어느 정도 한정적일 때에만 사용 가능 (1000만 이하)
  - `arr[i]` 에 i 가 나온 횟수 저장 후 나온만큼 순서대로 출력

- Radix Sort

  - 자릿수를 이용해서 정렬을 수행하는 알고리즘
  - Counting sort 활용하는 방법
  - 1의자리 -> 10의자리 -> 100의자리 ... 순서로 정렬
  - 시간복잡도 O(DN)

  

- Comparision Sort

  - 원소들끼리 비교하는 정렬
  - bubble, merge, quick sort

- Non-comparison Sort

  - 원소들끼리 비교 x
  - counting, radix sort



- **STL sort**

  - quick sort 기반으로 하지만, 재귀의 깊이가 너무 깊어지면 O(N logN)으로 처리함 (**Introspective sort**)

  - 기본적으로 unstable sort

  - pair, tuple에서는 제일 앞의 원소를 비교, 같으면 그 다음 비교 하는 방식이 기본

  - ```cpp
    int a[5] = {1, 4, 5, 2, 7};
    sort(a, a+5);
    vector<int> b = {1,4,5,2,7};
    sort(b.begin(), b.end()); // or sort(b.begin(), b.begin()+5);
    // stable_sort로 stable sort 가능
    
    // int 형을 5로 나눈 나머지순으로, 5로 나눈 나머지가 같다면 크기 순으로
    bool cmp(int a, int b){
        if (a%5 != b%5) return a%5 < b%5;
        return a < b;
    }
    sort(b.begin(),b.end(),cmp);
    ```
  
  - 주의사항

    - 비교 함수는 두 값이 같을 때 (혹은 우선순위가 같을 때) false를 반환

    - 비교 함수의 인자로 STL 혹은 클래스 객체를 전달 시 reference를 사용

      - ```cpp
        bool cmp(const string &a, const string &b){
            return a.back() < a.back();
        }
        ```
  
        

#### [다이나믹 프로그래밍](https://www.youtube.com/watch?v=5leTtB3PQu0&list=PLtqbFd2VIQv4O6D6l9HcD732hdrnYb6CY&index=17)

- 여러 개의 하위 문제를 먼저 푼 후 그 결과를 쌓아올려 주어진 문제를 해결하는 알고리즘
- DP를 푸는 과정

1. 테이블 정의하기
2. 점화식 찾기
3. 초기값 정하기



1463번 : 1로 만들기

1. 테이블 정의
   - D[i] = i 를 1로 만들기 위해 필요한 연산 사용 횟수의 최솟값
2. 점화식 찾기
   - D[12] = ?
   - 3으로 나누거나 (D[12] = D[4] + 1)
   - 2로 나누거나(D[12] = D[6] + 1)
   - 1을 빼거나 (D[12] = D[11]  + 1)
   - D[12] = MIN(D[4] + 1, D[6] + 1, D[11] + 1)
3. 초기값 정하기
   - D[1] = 0



#### [그리디](https://www.youtube.com/watch?v=De0Qg-2O80c&list=PLtqbFd2VIQv4O6D6l9HcD732hdrnYb6CY&index=18&t=704s)

> 지금 가장 최적인 답을 근시안적으로 택하는 알고리즘 = 관찰을 통해 탐색 범위를 줄이는 알고리즘

이상적인 풀이 흐름

1. 관찰을 통해 탐색 범위를 줄이는 방법을 고안
2. 탐색 범위를 줄여도 올바른 결과를 낸다는 사실을 수학적으로 증명
3. 구현



#### [수학](https://www.youtube.com/watch?v=2RCJApSVxRI&list=PLtqbFd2VIQv4O6D6l9HcD732hdrnYb6CY&index=19&t=20s)

- **소수**
  
  - 1과 자기 자신으로만 나누어지는 수
  - 약수가 2개인 수
  - 소수 판정법
    - 2부터 n-1까지의 수로 나누어지지 않는 수 = O(n)
    
    - 합성수 N에서 1을 제외한 가장 작은 약수는 sqrt(n) 이하이다.  = O(sqrt(n))
    
    - ```cpp
      bool isprime(int n){
        if (n==1) return 0;
        for (int i=2; i*i<=n; i++)
          if (n%i == 0) return 0;
        return 1;
      }
      ```



- **합성수**
  
  - 1과 자기 자신을 제외한 다른 약수를 가진 수
  - 1은 소수도 합성수도 아니다.
- 범위 내에서의 소수 판정법 - 에라토스테네스의 체
  - 최적화시 시간복잡도 : O(N lglg N)
  
  - ```cpp
    vector<int> sieve(int n){
      vector<int> primes;
      vector<bool> state(n+1, true);
      state[1] = false;
      for (int i=2; i*i<=n; i++){
        if (!state[i]) continue;
        for (int j=i*i; j<=n; j+=i)
          state[j] = false;
      }
      for (int i=2; i<=n; i++)
        if (state[i]) primes.push_back(i);
      return primes;
    }
    ```



- 약수 = 어떤 수를 나누어떨어지게 하는 수
  - 18의 약수 : 1,2,3,6,9,18 (1,2,3을 구하면 나머지는 18에서 나누면 구해진다)

```cpp
vector<int> divisor(int n) {
    vector<int> div;
    for (int i=1; i*i<=n; i++){
        if (n%i == 0) div.push_back(i);
    }
    for (int j=(int)div.size()-1; j>=0; j--){
        if (div[j] * div[j] == n) continue;
        div.push_back(n/ div[j]);
    }
    return div;
}
```



- **최대공약수 (Greatest Common Divisor)** = 두 자연수의 공통된 약수 중 가장 큰 약수

  - 유클리드 호제법

  - GCD(A,B) = GCD(B, r)

  - GCD(20, 12) = GCD(12, 8) = GCD(8, 4) = GCD(4, 0) = 4

  - ```cpp
    int gcd(int a, int b){
        if (a==0) return b;
        return gcd(b%a, a);
    }
    ```

  - [numeric library](https://en.cppreference.com/w/cpp/numeric/gcd)에 있음

- **최소공배수(LCM)**

  - A x B = GCD(A, B) x LCM(A,B)

  - ```cpp
    int lcm(int a, int b){
        return a / gcd(a,b) * b;
    }
    ```



- **연립 합동방정식**

  - 6명씩 조를 짰을 때 3명이 남는다.

  - 5명씩 조를 짰을 때 2명이 남는다.

  - 학생은 30명 미만

    ```cpp
    int chk() {
        for (int i=3; i<30; i+=6){
            if (i%5 == 2) return i;
    	}
        return -1;
    }
    ```

  - 중국인의 나머지 정리 (대회용 풀이)



- 순서를 고려하지 않고 뽑는 경우 : 조합
  - `nCk = n! / ((n-k)! k!)`
- 순서를 고려하는 경우 : 순열
  - `nPr = n! / (n-r)!`

- `nCk = n-1Ck + n-1Ck-1`


#### [해시](https://www.youtube.com/watch?v=1-k-D2AYY0I&list=PLtqbFd2VIQv4O6D6l9HcD732hdrnYb6CY&index=22)

- insert, erase, find, update 모두 O(1)

해시함수
- 임의 길이의 데이터를 고정된 길이의 데이터로 대응시키는 함수

해시테이블

충돌
- `0000 0000 0000 5135, 9999 9999 9999 5135` 처럼 뒷4자리가 같은 경우

충돌 회피 방법
- Chaining
  - 각 인덱스마다 연결 리스트를 둬서 충돌 회피하는 방법
  - 실제 STL에서 사용하는 방식
  - 이상적인 상황에서는 O(1) 이지만, 충돌이 빈번할수록 성능이 저하되고, 모든 키의 해시 값이 같은 최악의 상황에서는 O(N)

- Open addressing
  - `(0000 0000 0000 3333 , Kim)` = 3333번지
  - `(6278 5651 9104 3333, Lee)` = 3334
  - `(7298 1127 6004 3334, Bae)` = 3335
  - 같은 방식으로 저장 후 3333 find시 3333부터 일치하는지 확인하면서 주소 하나씩 이동하면서 체크
  - erase시 삭제한 칸에 원래 값이 있었지만 제거된 상태라고 명시 (insert시 만나면 삽입)
  - Linear Probing
    - 충돌 발생 시 오른쪽으로 1칸씩 이동하는 방식
    - 장점 : Cache hit rate가 높다.
    - 단점 : Clustering이 생겨 성능에 영향을 줄 수 있다. (군집이 커질수록 성능 저하)
  - Quadratic probing
    - 충돌 발생 시 오른쪽으로 1,3,5 칸씩 이동하는 방식
    - 장점
      - Cache hit rate가 나쁘지 않다.
      - Clustering을 어느 정도 회피할 수 있다.
    - 단점
      - 해시 값이 같을 경우 여전히 Clustering이 발생한다.
  - Doubling Hashing
    - 충돌 발생 시 이동할 칸의 수를 새로운 해시 함수로 계산하는 방식
    - 장점 : Clustering을 효과적으로 회피할 수 있다.
    - 단점 : Cache hit rate가 매우 낮다.

- STL
> unordered_set, unordered_multiset, unordered_map
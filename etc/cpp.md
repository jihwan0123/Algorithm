# C++

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


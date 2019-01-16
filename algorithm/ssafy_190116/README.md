# Computer Language

- Type
- 제어
  - 순차구조 (x=10)
  - 선택구조 (if)
  - 반복구조 (for)  



# 자료구조

- 선형 자료구조
  - 배열
  - 스택
  - 큐
  - 문자열  
- 비선형 자료구조 
  - 트리
    - 표현 방식
    	- 1차 배열
    	- 링크드 리스트
    - 순회(Traversal)
    	- preorder : root -> left -> right
    	- inorder : left -> root -> right
    	- postorder : left -> right -> root
    - 이진트리, 이진탐색트리, 최소신장트리(MST)  
  - 그래프
    - 표현 방식
      - 인접 행렬
      - 인접 리스트
    - 순회(Traversal)
      - DFS : 깊이 우선탐색
      - BFS : 너비 우선탐색
    - 최단경로, 외판원 문제(TSP)  



# 알고리즘

- 완전검색 (브루트-포스 알고리즘)
  - 순열(중복)
    - ![image](https://user-images.githubusercontent.com/30791915/51221013-f80fcb80-197a-11e9-8ca9-b7e1e3b41591.png)
  - 조합(중복)
    - ![image](https://user-images.githubusercontent.com/30791915/51220983-d9113980-197a-11e9-81c5-5c600c304199.png)
  - 부분집합
    - ex) 배낭 문제(knapsack)  
- 그리디 알고리즘
- 분할정복 알고리즘
- 백트래킹 알고리즘
  - 상태공간트리 + DFS, 가지치기
- 동적 계획법(DP)
  - 재귀적 DP
  - 반복적 DP
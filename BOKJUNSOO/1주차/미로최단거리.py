def solution(maps:list)->int:
    # BFS가 최단거리를 보장한다!
    # maps 라는 객체가 주어져도 bfs내에서 힙에 저장된 maps를 참조 가능
    def bfs(x,y):
        """
        특정 시작점부터 BFS 완전 탐색을 진행하는 함수
        """
        from collections import deque
        queue = deque()
        n = len(maps)
        m = len(maps[0])
        dx = [0,0,-1,1]
        dy = [1,-1,0,0]
        queue.append((x,y))
        # 큐가 빌때가지 진행
        while queue:
            x, y = queue.popleft()
            # 큐에서 원소가 하나 나올때 마다 4방향을 모두 탐색한다
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >=n  or ny >=m:
                    continue
                if maps[nx][ny] == 0:
                    continue
                # 갈 수 있는 길이라면 queue에 추가
                if maps[nx][ny] == 1:
                    queue.append((nx,ny))
                    # 다음 가는 방향의 값을 지금 내가 가지고 있는 값보다 1 높힌다
                    # 사실상 1이 아닌 값이 되기 때문에 방문처리가 되는 셈이다.
                    maps[nx][ny] = maps[x][y] + 1
        if maps[n-1][m-1] == 1:
            return -1
        return maps[n-1][m-1]
    answer = bfs(0,0)
    return answer

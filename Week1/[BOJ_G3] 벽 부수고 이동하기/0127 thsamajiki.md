```
* 풀이

1. BFS 이용
2. 북동남서 4방향
3. 벽을 부순 여부 확인
    - 벽을 부순 적이 있을 때
        - 벽이 아니고 방문한 적이 없다면 큐에 정보를 넣는다.
    - 벽을 부순 적이 없을 때
        - 벽이라면 벽을 부수고 큐에 값을 넣는다.
        - 벽이 아니면 큐에 값을 넣는다.
4. x = n, y = m에 도달했는지 체크

    

* 후기

3차원 visited를 생각해내기란 쉽지 않았다...
```
```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Point {
    int x;
    int y;
    int distance;
    boolean destroyedWall;

    public Point(int x, int y, int distance, boolean destroyedWall) {
        this.x = x;
        this.y = y;
        this.distance = distance;
        this.destroyedWall = destroyedWall;
    }
}

public class Main {
    static int n, m, answer = Integer.MAX_VALUE;
    static int[] dx = { -1, 0, 1,  0 };
    static int[] dy = { 0,  1, 0, -1 };
    static int[][] map;
    static boolean[][][] visited;

    public int solution(int x, int y) {
        Queue<Point> q = new LinkedList<>();
        q.offer(new Point(x, y, 1, false));

        while (!q.isEmpty()) {
            Point now = q.poll();

            if (now.x == n && now.y == m) {
                answer = now.distance;
                return answer;
            } else {
                for (int i = 0; i < 4; i++) {
                    int nextX = now.x + dx[i];
                    int nextY = now.y + dy[i];
                    int nextDistance = now.distance + 1;

                    if (nextX < 1 || nextX > n || nextY < 1 || nextY > m) continue;

                    if (now.destroyedWall) {
                        if (map[nextX][nextY] == 0 && !visited[nextX][nextY][1]) {
                            visited[nextX][nextY][1] = true;
                            q.offer(new Point(nextX, nextY, nextDistance, true));
                        }
                    } else {
                        if (map[nextX][nextY] == 1) {
                            visited[nextX][nextY][1] = true;
                            q.offer(new Point(nextX, nextY,nextDistance, true));
                        } else if (!visited[nextX][nextY][0]) {
                            visited[nextX][nextY][0] = true;
                            q.offer(new Point(nextX, nextY, nextDistance,false));
                        }
                    }
                }
            }
        }

        return -1;
    }

    public static void main(String[] args) throws IOException {
        Main main = new Main();

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        map = new int[n + 1][m + 1];
        for (int i = 1; i <= n; i++) {
            String row = br.readLine();
            for (int j = 1; j <= m; j++) {
                map[i][j] = row.charAt(j - 1) - '0';
            }
        }

        visited = new boolean[n + 1][m + 1][2];

        visited[1][1][0] = true;
        System.out.println(main.solution(1, 1));
    }
}
```

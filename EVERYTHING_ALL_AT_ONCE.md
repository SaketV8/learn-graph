# 🌸 Recursion Practice

## 📂 DFS and BFS on Graphs

<details>
<summary>📄 bfs-of-graph.cpp</summary>


<h3 align="center"> ⚡ bfs-of-graph.cpp </h3>

```cpp
// https://www.geeksforgeeks.org/problems/bfs-traversal-of-graph/1

class Solution {
  public:
  
    using vi = vector<int>;
    using vvi = vector<vi>;
    using vb = vector<bool>;
    
    
    // implemented using queue
    void bfsOfGraph(vvi &adj, int u, vb &visited, vi &result) {
        queue<int> que;
        
        que.push(u); // put in queue and mark it visited
        visited[u] = true;
        result.push_back(u);
        
        // now, bfs code
        while(!que.empty()) {
            int u = que.front();
            que.pop();
            
            for(auto &v: adj[u]) {
                if(!visited[v]) {
                    que.push(v); // put in queue and mark it visited
                    visited[v] = true;
                    result.push_back(v);
                }
            }
        }
        
    }
        
    vector<int> bfs(vector<vector<int>> &adj) {
        int n = adj.size();
        
        vi result;
        vb visited(n, false);
        
        bfsOfGraph(adj, 0, visited, result);
        return result;
        
    }
};
```
</details>

<details>
<summary>📄 dfs-of-graph.cpp</summary>


<h3 align="center"> ⚡ dfs-of-graph.cpp </h3>

```cpp
// https://www.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1

class Solution {
  public:
  
    using vi = vector<int>;
    using vvi = vector<vi>;
    using vb = vector<bool>;
    
    void dfsOfGraph(vvi& adj, int u, vb &visited, vi &result) {
        if(visited[u]) {
            return;
        }
        
        visited[u] = true;
        
        result.push_back(u);
        
        for(int &v: adj[u]) {
            if(!visited[v]) {
                dfsOfGraph(adj, v, visited, result);
            }
        }
    }
    
    vector<int> dfs(vector<vector<int>>& adj) {
        int n = adj.size();
        
        vi result;
        vb visited(n, false);
        
        dfsOfGraph(adj, 0, visited, result);
        
        return result;
    }
};
```
</details>


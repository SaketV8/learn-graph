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
class Node {
public:
    Node(int _name, int _stops, int _cost): name(_name), cost(_cost), stops(_stops) {}
    int name;
    int cost;
    int stops;
};

class Edge {
public:
    Edge(int _from, int _to, int _cost):from(_from), to(_to), cost(_cost) {}
    int from;
    int to;
    int cost;
};

class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int K) {
        vector<vector<Edge>> graph(n, vector<Edge>());
        for(auto& f: flights) {
            Edge e(f[0], f[1], f[2]);
            graph[f[0]].push_back(e);
        }
        
        vector<bool> visited(n, false);
        
        auto compare = [](Node lhs, Node rhs) { return lhs.cost > rhs.cost; };
        priority_queue<Node, vector<Node>, decltype(compare)> pq(compare);
        
        Node src_node(src, -1, 0);
        pq.push(src_node);
        
        while(!pq.empty()) {
            Node node = pq.top(); pq.pop();
            if (node.name == dst) {
                return node.cost;
            }
            for(auto e: graph[node.name]) {
                if (!visited[e.to] && node.stops + 1 <= K) {
                    Node nei(e.to, node.stops + 1, node.cost + e.cost);
                    pq.push(nei);
                }
            }
            visited[node.name] = true;
        }
        return -1;
    }
};
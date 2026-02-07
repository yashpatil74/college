#include <iostream>
#include <string>
#include <stack>
#include <queue>

using namespace std;

class Node {
    int id;
    string name;
    Node* next;

public:
    Node(int i, string n) {
        id = i;
        name = n;
        next = NULL;
    }
    friend class graph;
};

class graph {
    Node* head[20]; 
    int n;       
    string names[20];

public:
    graph() {
        cout << "Enter number of users: ";
        cin >> n;
        for (int i = 0; i < n; i++) {
            head[i] = NULL;
            cout << "Enter name for ID " << i << ": ";
            cin >> names[i];
        }
    }

    void addEdge() {
        int u, v;
        cout << "Enter edge (ID1 ID2) or -1 -1 to stop: ";
        while (cin >> u >> v && u != -1) {
            Node* newNode = new Node(v, names[v]);
            newNode->next = head[u];
            head[u] = newNode;

            newNode = new Node(u, names[u]);
            newNode->next = head[v];
            head[v] = newNode;
        }
    }

    void display() {
        cout << "\nAdjacency List:\n";
        for (int i = 0; i < n; i++) {
            cout << names[i] << " (" << i << ") -> ";
            Node* temp = head[i];
            while (temp) {
                cout << temp->name << " ";
                temp = temp->next;
            }
            cout << endl;
        }
    }

    void dfs_rec(int v, bool visited[]) {
        visited[v] = true;
        cout << names[v] << " ";
        Node* temp = head[v];
        while (temp) {
            if (!visited[temp->id])
                dfs_rec(temp->id, visited);
            temp = temp->next;
        }
    }

    void bfs(int start) {
        bool visited[20] = {false};
        queue<int> q;

        visited[start] = true;
        q.push(start);

        cout << "\nBFS Traversal: ";
        while (!q.empty()) {
            int v = q.front();
            q.pop();
            cout << names[v] << " ";

            Node* temp = head[v];
            while (temp) {
                if (!visited[temp->id]) {
                    visited[temp->id] = true;
                    q.push(temp->id);
                }
                temp = temp->next;
            }
        }
        cout << endl;
    }
};

int main() {
    graph g;
    g.addEdge();
    g.display();

    bool visited[20] = {false};
    cout << "\nRecursive DFS Traversal: ";
    g.dfs_rec(0, visited);

    g.bfs(0);

    return 0;
}
#include<iostream>
#include<stack>
using namespace std;

class Node {
    int vertex;
    int id;
    string name;
    Node *next;
    friend class Graph; 
};

class Graph {
    private:
        Node* head[20];
        int n;
        int visited[20];

    public:
        Graph() {
            cout << "Enter number of vertices: ";
            cin >> n;
            for (int i = 0; i < n; i++) {
                head[i] = new Node();  
                head[i]->next = NULL;
                head[i]->vertex = i; 
                visited[i] = 0;
            }
        }

        void Create() {
            char ans;

            for(int i = 0; i < n; i++) {
                Node* temp = head[i];
                string name;
                cout << "Enter name: " << i << ": ";
                cin >> name;
                temp->name = name;
                
                do {
                    int v;
                    cout << "Enter vertex connected to " << i << ": ";
                    cin >> v;
                    if(v == i) {
                        cout << "Self loop\n";
                    }
                    else {
                        Node* curr = new Node();
                        curr->vertex = v; 
                        curr->next = NULL;
                        temp->next = curr;
                        temp = temp->next;
                    }
                    cout << "Do you want to continue (y/n): ";
                    cin >> ans;
                } while(ans=='y' || ans=='Y');
            }
        }

        void DFS(int v) {
            visited[v] = 1;
            cout << v << " ";
            for(Node* temp = head[v]->next; temp != NULL; temp = temp->next) {
                if(visited[temp->vertex] == 0) {
                    DFS(temp->vertex);
                }
            }
        }

        void DFSTraversal() {
            for(int i = 0; i < n; i++) {
                visited[i] = 0;
            }
            for(int i = 0; i < n; i++) {
                if(visited[i] == 0) {
                    DFS(i);
                }
            }
        }

        void DFSNonRecursive(int start) {
            stack<int> s;
            s.push(start);
            visited[start] = 1;

            while(!s.empty()) {
                int v = s.top();
                s.pop();
                cout << v << " ";

                for(Node* temp = head[v]->next; temp != NULL; temp = temp->next) {
                    if(visited[temp->vertex] == 0) {
                        visited[temp->vertex] = 1;
                        s.push(temp->vertex);
                    }
                }
            }
        }

        void DFSNonRecursiveTraversal() {
            for(int i = 0; i < n; i++) {
                visited[i] = 0;
            }
            for(int i = 0; i < n; i++) {
                if(visited[i] == 0) {
                    DFSNonRecursive(i);
                }
            }
        }
};

int main() {
    Graph g;
    g.Create();
    cout << "DFS Traversal (Recursive): ";
    g.DFSTraversal();
    cout << "\n";
    cout << "DFS Traversal (Non-Recursive): ";
    g.DFSNonRecursiveTraversal();
    cout << "\n";
    return 0;
}
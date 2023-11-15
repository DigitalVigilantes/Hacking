#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

int main() {
    int E, M, D;
    cin >> E >> M >> D;

    vector<unordered_set<int>> likePairs(E + 1), dislikePairs(E + 1);

    for (int i = 0; i < M; ++i) {
        int X, Y;
        cin >> X >> Y;
        likePairs[X].insert(Y);
        likePairs[Y].insert(X);
    }

    for (int i = 0; i < D; ++i) {
        int U, V;
        cin >> U >> V;
        dislikePairs[U].insert(V);
        dislikePairs[V].insert(U);
    }

    vector<vector<int>> groups(E / 3);
    for (int i = 0; i < E / 3; ++i) {
        int I, J, K;
        cin >> I >> J >> K;
        groups[i] = {I, J, K};
    }

    int violations = 0;
    for (const auto& group : groups) {
        for (int i = 0; i < 3; ++i) {
            for (int j = i + 1; j < 3; ++j) {
                int stud1 = group[i];
                int stud2 = group[j];
                if (likePairs[stud1].count(stud2)) {
                    violations++;
                }
                if (dislikePairs[stud1].count(stud2)) {
                    violations++;
                }
            }
        }
    }

    cout << violations << endl;

    return 0;
}

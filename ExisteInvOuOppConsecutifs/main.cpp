#include <iostream>
using namespace std;
bool existeInvOuOppConsecutifs(int T[], int n) {
    for (int i = 0; i < n - 1; i++) {
        if ((T[i] + T[i + 1] == 0) || (T[i] * T[i + 1] == -1)) {
            return true;
        }
    }
    return false;
}

int main() {
    int n;
    cout << "Entrer le nombre d'�l�ments du tableau: ";
    cin >> n;

    int T[n];
    cout << "Entrer les " << n << " �l�ments: \n";
    for (int i = 0; i < n; i++) {
        cin >> T[i];
    }

    if (existeInvOuOppConsecutifs(T, n)) {
        cout << "Vrai\n";
    } else {
        cout << "Faux\n";
    }

    return 0;
}

#include<iostream>
#include<string>
using namespace std;

bool run = true;
bool isRNA = true;
int score = 0;
string original = "TCAG ";
string flipped = "AGUC ";
string sequence;
string answer;
int maxScore = 0;
string userIn;
int main() {
    cout << "Transcribe to mRNA! Type \'stop\' at any time to quit." << endl;
    while (run) {
        sequence = "";
        answer = "";
        userIn = "";
        for (int b=0;b<3;b++) {
            for (int c=0;c<3;c++) {
                sequence = sequence + original[rand() % 3];
            }
            if (b < 2) {
                sequence = sequence + " ";
            }
        }
        for (int d=0;d<sequence.length();d++) {
            answer = answer + flipped[original.find(sequence[d])];
        }
        cout << sequence << endl;
        
        cin >> userIn;
        if (userIn == answer || userIn + " " == answer) {
            score++;
            maxScore++;
            cout << "Correct! Score: " << score << endl;
        } else if (userIn == "stop") {
            run = false;
            cout << "Exiting program" << endl;
        } else {
            cout << "Incorrect. Correct answer: " << answer << endl;
            maxScore++;
            if (userIn.find("T") != -1) {
                cout << "Remember, mRNA doesn\'t have T\'s!'" << endl;
            }
        }
    }
    cout << "Your final score is: " << score << " out of " << maxScore << endl;
    cout << "%" << " correct: " << float(score)/float(maxScore)*100 << "%" << endl;
    if (score == maxScore) {
        cout << "Well done!" << endl;
    } else if (score == 0) {
        cout << "Coward." << endl;
    }
    return 0;
}

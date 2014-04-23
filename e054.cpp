//Project Euler Problem 54, 19.04.2014 Valentin Voelkl

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;





class poker_hand {
    public:
        vector <int> cards;
        //vector<string> sort(int * cards[2][5]);
        //int assign_value(vector<string>);
        int is_sequence();
        //int value = assign_value(cards)
        void add_card(string value, string suit);
        void print_cards();
        void sort();
};

void poker_hand::add_card(int card) {
    cards.push_back(card);
}

void poker_hand::sort() {
    sort(cards.begin(), cards.end());
}
    
int poker_hand::is_sequence() {
    //int diff = 0;
    for(int i = 0; i<cards.size()-1;i++){
        if(( cards[i] % 100  - cards[i+1] % 100) != 1){
            return 0;
            }
        }
    return 1;
}

bool poker_hand::same_suit(){
    int s = cards[0] % 4;
    for(int i =1; i<cards.size();i++){
        if ((cards[i] % 4 ) != s){
            return 0;
        }
    }
    return 1;
}

int poker_hand::count_pairs() {
    int v;
    int num_pairs = 0;
    for (int j = 0; j < cards.size()-1; j++) {
        v = cards[i] % 100;
        for (int i = 1; i<cards.size();i++) {
            if(v == (cards[i+1] % 100)){
                num_pairs++;
                i++;
            }  
        }
    }
    return num_pairs;
}

int poker_hand::count_kind() {
    int kind = 0;
    int maxkind = 0;
    for (int i = 0; i<cards.size();i++) {
        if (cards[i] % 100 == cards[i+1] % 100) {
            kind++;
        }
        else {
        if (kind > maxkind) {
            maxkind = kind;
            } 
        }
    }
    return maxkind;
}

int main(){
    int Player_1_wins;
    int _c;
    string line;
    ifstream poker_file;
    poker_file.open("poker.txt");
    poker_hand p1(); poker_hand p2();
    if (poker_file.is_open())
  {
    while ( getline (poker_file,line) ){
        

        for(int i=0; i < 29; i = i + 2){
            _c = 0;
            switch(line[i]){
                case '2': _c = 200;
                case '3': _c = 300;
                case '4': _c = 400;
                case '5': _c = 500;
                case '6': _c = 600;
                case '7': _c = 700;
                case '8': _c = 800;
                case '9': _c = 900;
                case 'J': _c = 1000;
                case 'Q': _c = 1100;
                case 'K': _c = 1200;
                case 'A': _c = 1300;
                }
            switch(line[i+1]){
                case 'D': _c += 0;
                case 'C': _c += 1;
                case 'S': _c += 2;
                case 'H': _c += 3;
                }

            cout<<_c<<endl;
            if(i < 15){
                p1.add_card(_c);
            }
            else{
                p2.add_card(_c);
            }
            //string v(line[i]);
            //string s(line[i+1]);
            //p1.add_card(v, s);
            //cout<<line[i]<<endl;
        }
        p1.sort(); p2.sort();
        Player_1_wins += p1.calc() > p2.calc();

        //poker_hand p1(line);
        //p1.print_cards();
        //cout<<line<<endl;
        }
    }

    return 0;
}



#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class poker_hand {
public:
  vector<int> cards;
  vector<int> pair_values;
  long unsigned int value;
  int is_sequence();
  bool same_suit();
  int count_pairs();
  void eval_pairs();
  int count_kind();
  int eval_kind();
  void calculate();
  void add_card(int card);
  void sort_hand();
  void clear_hand();
};

void poker_hand::clear_hand() {
  cards.clear();
  pair_values.clear();
  value = 0;
}

void poker_hand::add_card(int card) { cards.push_back(card); }

void poker_hand::sort_hand() { sort(cards.begin(), cards.end()); }

int poker_hand::is_sequence() {
  for (unsigned int i = 0; i < cards.size() - 1; i++) {
    if ((cards[i] / 100 - cards[i + 1] / 100) != -1) {
      return 0;
    }
  }
  return 1;
}

bool poker_hand::same_suit() {
  int s = cards[0] % 4;
  for (unsigned int i = 1; i < cards.size(); i++) {
    if ((cards[i] % 4) != s) {
      return 0;
    }
  }
  return 1;
}

int poker_hand::count_pairs() {
  int v;
  int num_pairs = 0;
  for (unsigned int i = 0; i < cards.size(); i++) {
    v = cards[i] / 100;
    if (v == (cards[i + 1] / 100)) {
      num_pairs++;
      i++;
    }
  }
  return num_pairs;
}
void poker_hand::eval_pairs() {
  int v;
  for (unsigned int i = 0; i < cards.size() - 1; i++) {
    v = cards[i] / 100;
    if (v == (cards[i + 1] / 100)) {
      pair_values.push_back(v);
      i++;
    }
  }
  sort(pair_values.begin(), pair_values.end());
}

int poker_hand::count_kind() {
  int kind = 1;
  int maxkind = 0;
  for (unsigned int i = 0; i < cards.size(); i++) {
    if (cards[i] / 100 == cards[i + 1] / 100) {
      kind++;
    } else {
      if (kind > maxkind) {
        maxkind = kind;
      }
      kind = 1;
    }
  }
  return maxkind;
}

int poker_hand::eval_kind() {
  int maxr = 0;
  int kind = 1;
  int maxkind = 0;
  int r = 0;
  for (unsigned int i = 0; i < cards.size(); i++) {
    if (cards[i] / 100 == cards[i + 1] / 100) {
      kind++;
      r = cards[i] / 100;
    } else {
      if (kind > maxkind) {
        maxr = r;
        maxkind = kind;
      }
      kind = 1;
    }
  }
  return maxr;
}

void poker_hand::calculate() {
  const long unsigned int offset = 100000000000000;
  // Royal Flush
  if (is_sequence() && same_suit() && cards.back() / 100 == 14) {
    value = offset * 13;
  }
  // Straight Flush
  else if (is_sequence() && same_suit()) {
    value = offset * 12;
    // get highest card
    value += offset / 100 * (cards.back() / 100);
  }
  // Four of a kind
  else if (count_kind() == 4) {
    value = offset * 11;
    value += eval_kind() * offset / 100;
    for (unsigned int i = 0; i < cards.size(); i++) {
      value += (cards[i] / 100);
    }
  }
  // Full House
  else if (count_kind() == 3 && count_pairs() == 2) {
    value = offset * 10;
    value += eval_kind() * offset / 100;
    eval_pairs();
    value += pair_values[0] * offset / 100 / 100;
  }
  // Flush
  else if (same_suit()) {
    value = offset * 9;
    long unsigned int off = offset;
    for (unsigned int i = cards.size(); i > 0; i--) {
      off = off / 100;
      value += off * (cards[i] / 100);
    }
  }
  // Straight
  else if (is_sequence()) {
    value = offset * 8;
    value += (cards.back() / 100) * offset / 100;
  }
  // Three of a kind
  else if (count_kind() == 3) {
    value = offset * 7;
    value += eval_kind() * offset / 100;
    long unsigned int off = offset / 100;
    for (unsigned int i = cards.size(); i > 0; i--) {
      off = off / 100;
      value += off * (cards[i] / 100);
    }
  }
  // Two Pairs
  else if (count_pairs() == 2) {
    value = offset * 6;
    eval_pairs();
    value += offset / 100 * pair_values[1] + offset / 100 / 100 * pair_values[0];
    for (unsigned int i = cards.size(); i > 0; i--) {
      value += (cards[i] / 100);
    }
  // One Pair
  } else if (count_pairs() == 1) {
    value = offset * 5;
    eval_pairs();
    value += offset / 100 * pair_values[0];
    long unsigned int off = offset / 100;
    for (unsigned int i = cards.size(); i > 0; i--) {
      off = off / 100;
      value += off * (cards[i] / 100);
    }
  // Highest Card
  } else {
    value = 0;
    long unsigned int off = offset / 100;
    for (unsigned int i = cards.size(); i > 0; i--) {
      off = off / 100;
      value += off * (cards[i] / 100);
    }
  }
}

int solve() {
  int Player_1_wins = 0;
  int _c;
  char _s;
  string line;
  ifstream poker_file;
  poker_file.open("e054poker.txt");
  poker_hand p1;
  poker_hand p2;
  if (poker_file.is_open()) {
    while (getline(poker_file, line)) {

      for (int i = 0; i < 29; i = i + 3) {
        _c = 0;
        _s = (char)line[i];
        switch (_s) {
        case '2':
          _c = 200;
          break;
        case '3':
          _c = 300;
          break;
        case '4':
          _c = 400;
          break;
        case '5':
          _c = 500;
          break;
        case '6':
          _c = 600;
          break;
        case '7':
          _c = 700;
          break;
        case '8':
          _c = 800;
          break;
        case '9':
          _c = 900;
          break;
        case 'T':
          _c = 1000;
          break;
        case 'J':
          _c = 1100;
          break;
        case 'Q':
          _c = 1200;
          break;
        case 'K':
          _c = 1300;
          break;
        case 'A':
          _c = 1400;
          break;
        }
        switch (line[i + 1]) {
        case 'D':
          _c += 0;
          break;
        case 'C':
          _c += 1;
          break;
        case 'S':
          _c += 2;
          break;
        case 'H':
          _c += 3;
          break;
        }

        if (i < 15) {
          p1.add_card(_c);
        } else {
          p2.add_card(_c);
        }
      }
      p1.sort_hand();
      p2.sort_hand();
      p1.calculate();
      p2.calculate();
      Player_1_wins += p1.value > p2.value;
      p1.clear_hand();
      p2.clear_hand();
    }
  }
  return Player_1_wins;
}

#include "boilermain.cpp"

#include <unordered_set>
#include <bitset>
/*** Simple implementation of Conways's Game of Life
* 
* the state is held by 'board' a two dimensional array of booleans
* life := 1, death := 0
* the size of the board is fixed at compile time
* 
***/
template<size_t N>
class GameOfLife {
public:


  void reset() {
    hash_cache.clear();
    counter = 0;
    done = false;

  }

  size_t hasharray() {
    size_t seed = 0;
    for (size_t i = 0; i < N; i++) {
      size_t hash_value = std::hash<std::bitset<N>>{}(board[i]);
      seed ^= hash_value + 0x9e3779b9 + (seed << 6) + (seed >> 2);
    }
    return seed;
  }

  void initialize_glider() {
    for (int i = 0; i < N_CELLS; i++) {
      for (int j = 0; j < N_CELLS; j++) {
        board[i][j] = DEAD;
      }
    }
    board [10][10] = ALIVE;
    board [11][10] = ALIVE;
    board [12][10] = ALIVE;
    std::copy(board.begin(), board.end(), board_new.begin());
  }

  void initialize() {
    for (int i = 0; i < N_CELLS; i++) {
      for (int j = 0; j < N_CELLS; j++) {
        board[i][j] = DEAD;
      }
    }
    std::copy(board.begin(), board.end(), board_new.begin());
  }

  void run() {
    while (!done) {
      this->evolve();
      size_t boardhash = this->hasharray();
      if (hash_cache.find(boardhash) == hash_cache.end()) {
        hash_cache.insert(boardhash);
      } else {
        done = true;
      }
      counter++;
    }
  }

  void initialize_random(float initial_fill_fraction=0.5) {
    std::random_device random_device;
    std::mt19937 random_engine(time(0));
    std::uniform_real_distribution<float> random_distribution(0., 1.);
    for (int i = 1; i < N_CELLS-1; i++) {
      for (int j = 1; j < N_CELLS-1; j++) {
        board[i][j] = random_distribution(random_engine) < initial_fill_fraction;
      }
    }
    std::copy(board.begin(), board.end(), board_new.begin());
  }

  void evolve() {
    // fixed boundary
    for (int i = 1; i < N_CELLS - 1; i++) {
      for (int j = 1; j < N_CELLS - 1; j++) {
        int  neighbors = 0;
        neighbors =  
                    board[i+1][j-1] +
                    board[i+1][j] +
                    board[i+1][j+1] +
                    board[i][j+1] +
                    board[i][j-1] +
                    board[i-1][j+1] +
                    board[i-1][j] +
                    board[i-1][j-1];
        if (board[i][j] == ALIVE) {
          if (neighbors < 2 || neighbors > 3 ) {
            board_new[i][j] = DEAD;
          }
        } else {
          if (neighbors == 3) {
            board_new[i][j] = ALIVE;
          }
        }
      } // j
    } // i
    // move updated board back
    std::copy(board_new.begin(), board_new.end(), board.begin());
  }

  unsigned int count_live_cells() {
    unsigned int num_cells = 0;
    for (int i = 1; i < N_CELLS - 1; i++) {
      for (int j = 1; j < N_CELLS - 1; j++) {
        num_cells += board[i][j];
      }
    }

  return num_cells;
  }
  unsigned int counter = 0;
  static constexpr size_t max_cache_size = 10000;
  std::unordered_set<size_t> hash_cache; 
  static constexpr unsigned int N_CELLS = N;
  std::array<std::bitset<N>, N> board_new;
  std::array<std::bitset<N>, N> board;
  enum GOL {DEAD, ALIVE}; 
  bool done;


private:


};


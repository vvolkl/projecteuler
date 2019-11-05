#include <unordered_set>
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
    return boost::hash_range(&board[0][0], &board[0][0]+(N*N));
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
    std::memcpy(board_new, board, sizeof(board));
  }

  void initialize() {
    for (int i = 0; i < N_CELLS; i++) {
      for (int j = 0; j < N_CELLS; j++) {
        board[i][j] = DEAD;
      }
    }
    std::memcpy(board_new, board, sizeof(board));
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
    std::memcpy(board_new, board, sizeof(board));
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
    std::memcpy(board, board_new, sizeof(board));
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
  bool board_new[N_CELLS][N_CELLS];
  unsigned char board[N_CELLS][N_CELLS];
  enum GOL {DEAD, ALIVE}; 
  bool done;


private:


};


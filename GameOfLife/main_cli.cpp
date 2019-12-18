#include <iostream>
#include <random>
#include "game_of_life_cpp.h"

constexpr int N_CELLS = 100;
constexpr int N_TRIALS =  1000;

int main(int argc, char** argv) {
  std::random_device random_device;
  std::mt19937 random_engine(random_device());
  std::uniform_real_distribution<float> random_distribution(0. ,1.);
  GameOfLife<N_CELLS> gol;
  for (unsigned int i = 0; i < N_TRIALS; i++) {
    // roll dice for fill fraction
    float initial_fill_fraction = random_distribution(random_engine);
    gol.reset();
    gol.initialize_random(initial_fill_fraction);
    gol.counter = 0;
    gol.run();
    // io
    std::cout << N_CELLS << "\t";
    std::cout << initial_fill_fraction << "\t";
    std::cout << gol.counter << "\t";
    std::cout << gol.count_live_cells() << std::endl;
  }
  return 0;
}

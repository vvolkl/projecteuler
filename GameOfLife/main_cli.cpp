#include <iostream>
#include <random>
#include <boost/functional/hash.hpp>
#include "game_of_life_cpp.h"
#include <cstring>
#include <unordered_set>

constexpr int n_boxes = 100;
constexpr int n_trials =  1000;

int main(int argc, char** argv) {
  /*
  float initial_fill_fraction;
  if (argc > 1) {
    initial_fill_fraction = atof(argv[1]);
  } else {
    initial_fill_fraction = 0.5;
  }
  */
  GameOfLife<n_boxes> gol;

  for (unsigned int i = 0; i < n_trials; i++) {
    
    std::random_device random_device;
    std::mt19937 random_engine(random_device());
    std::uniform_real_distribution<float> random_distribution(0. ,1.);
    float initial_fill_fraction = random_distribution(random_engine);
    gol.reset();
    gol.initialize_random(initial_fill_fraction);
    gol.counter = 0;
    gol.run();
    std::cout << n_boxes << "\t";
    std::cout << initial_fill_fraction << "\t";
    std::cout << gol.counter << "\t";
    std::cout << gol.count_live_cells() << std::endl;
  }



  return 0;
}

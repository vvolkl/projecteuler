#include <stdio.h>
#include <array>
#include <string>
#include "SDL2/SDL.h"

#include "LTimer.h"

#include "game_of_life_cpp.h"

constexpr int window_width = 840;
constexpr int window_height = 840;

constexpr int total_window_width = 1240;
constexpr int total_window_height = 840;
constexpr int window_margin = 20;
constexpr int box_margin = 2;
constexpr int N_CELLS = 100;
constexpr int box_width = (window_width - window_margin - N_CELLS * box_margin) / N_CELLS;
constexpr int plot_offset = 2* window_margin + N_CELLS*(box_margin + box_width);

constexpr int SCREEN_FPS = 60;
constexpr int SCREEN_TICKS_PER_FRAME = 1000 / SCREEN_FPS;
constexpr int plot_scale = 4;
constexpr bool do_vsync = true;



int main () { 
  //////////////// Game of Life Setup
  std::vector<SDL_Point> cell_counts;
  float initial_fill_fraction = 0.3;
  GameOfLife<N_CELLS> gol;
  gol.initialize();
  gol.initialize_random(initial_fill_fraction);
  // ............. Game of Life Setup

  //////////////////////// SDL Setup
  SDL_Init(SDL_INIT_VIDEO);
  SDL_Window* window =
      SDL_CreateWindow("Game Of Life", 
                       SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, 
                       total_window_width, total_window_height,
                       SDL_WINDOW_SHOWN);
  if (NULL == window)
    printf("Error  %s", SDL_GetError());
  SDL_Renderer* renderer; 
  if (do_vsync)  
    renderer = SDL_CreateRenderer( window, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC );
  else
    renderer = SDL_CreateRenderer( window, -1, SDL_RENDERER_ACCELERATED );
  if(NULL == renderer)
    printf( "Renderer could not be created! SDL Error: %s\n", SDL_GetError() );
  //....................... SDL Setup
  
  /////////////////////// Init and draw grid
  SDL_SetRenderDrawColor( renderer, 0x44, 0x44, 0x44, 0x44 );
  SDL_RenderFillRect(renderer, NULL);
  SDL_SetRenderDrawColor( renderer, 0x66, 0x66, 0x66, 0x66 );
  std::array<SDL_Rect*, N_CELLS*N_CELLS> rect_arr;
  for (int i = 0; i < N_CELLS; i++) {
    for (int j = 0; j < N_CELLS; j++) {
      rect_arr[i*N_CELLS + j] = new SDL_Rect{window_margin + i*box_margin + i*box_width,
                                             window_margin + j*box_margin + j*box_width,
                                             box_width,
                                             box_width};
      SDL_RenderFillRect(renderer, rect_arr[i*N_CELLS + j]);
    }
  }
  //..................... Init and draw grid

  //////////////////////// Game loop
  SDL_RenderPresent( renderer );
  SDL_Color textColor = { 0, 0, 0, 255 };
  LTimer fpsTimer;
  LTimer capTimer;
  std::string timeText;
  int countedFrames = 0;
  fpsTimer.start();
  SDL_Event e;
  bool quit = false;  
  while (!quit) {
    capTimer.start();
    while(SDL_PollEvent(&e)) { 
      if (e.type == SDL_QUIT) {
        quit = true;
      }

    }

    SDL_RenderClear( renderer );
    SDL_SetRenderDrawColor( renderer, 0x44, 0x44, 0x44, 0x44 );
    // GOL board
    SDL_RenderFillRect(renderer, NULL);
    for (int i = 0; i < N_CELLS; i++) {
      for (int j = 0; j < N_CELLS; j++) {
        if (!gol.board[i][j])
          SDL_SetRenderDrawColor( renderer, 0x66, 0x66, 0x66, 0x66 );
        else 
          SDL_SetRenderDrawColor( renderer, 0x27, 0x95, 0x0C, 0x66 );
        SDL_RenderFillRect(renderer, rect_arr[i*N_CELLS + j]);
      }
    }
    
    //line plot
    cell_counts.emplace_back(SDL_Point{(plot_offset + (countedFrames %(total_window_width - plot_offset)))/plot_scale,
                                        ( total_window_height - static_cast<int>(gol.count_live_cells())/2)/plot_scale});
    SDL_SetRenderDrawColor( renderer, 0x27, 0x95, 0x0C, 0x66 );
    SDL_RenderSetScale(renderer, plot_scale, plot_scale);
    SDL_RenderDrawPoints(renderer, &(cell_counts.front()), cell_counts.size());
    SDL_RenderSetScale(renderer, 1,1);
    
    SDL_RenderPresent( renderer );
     countedFrames++;
     gol.evolve();
     //If frame finished early
     int frameTicks = capTimer.getTicks();
     if (frameTicks < SCREEN_TICKS_PER_FRAME) {
         SDL_Delay( SCREEN_TICKS_PER_FRAME - frameTicks );
     }
     // Once per second, do some stuff
     if (countedFrames % 60 == 0) {
       //printf( "frameticks %i\n", SCREEN_TICKS_PER_FRAME - frameTicks);
       printf( "live cells %i\n", gol.count_live_cells());
       printf("x, y: %i, %i\n", plot_offset + (countedFrames % (total_window_width - plot_offset)), total_window_height - gol.count_live_cells());
    }
  } //............................................. game loop
  return 0;
}

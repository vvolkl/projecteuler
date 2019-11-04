#include <FL/Fl.H>
#include <FL/Fl_Double_Window.H>
#include <FL/Fl_Box.H>
#include <FL/Fl_Bitmap.H>
#include <FL/fl_draw.H>
#include <boost/functional/hash.hpp>

#include <math.h>
#include <stdio.h>
#include <time.h>
#include <iostream>
#include <random>
#include <cstring>
#include <random>
#include <unordered_set>

#include "game_of_life_cpp.h"


constexpr int CIRC_COLOR = 0;
constexpr int TICK_COLOR = 50;
constexpr int BG_COLOR = 45;
constexpr int window_width = 840;
constexpr int window_height = 840;
constexpr int margin = 20;
constexpr int box_margin = 1;
constexpr int n_boxes = 200;
constexpr int box_width = (window_width - 1* margin - n_boxes * box_margin) / n_boxes;




class GameOfLifeWindow : public Fl_Box {

public:

  GameOfLifeWindow(int X,int Y,int W,int H,float initial_fill_fraction,const char*L=0) : Fl_Box(X,Y,W,H,L) {
    box(FL_FLAT_BOX);
    color(BG_COLOR);
    Fl::add_timeout(1, Timer_CB, (void*)this);
    gol.initialize();
    gol.initialize_random(initial_fill_fraction);
}

void draw() {
    // tell base widget to draw its background
    Fl_Box::draw();
    fl_color(CIRC_COLOR);
    for (int i = 0; i < n_boxes; i++) {
      for (int j = 0; j < n_boxes; j++) {
        // draw game of life
        fl_draw_box(FL_FLAT_BOX, 
          margin + i * box_width + i * box_margin, 
          margin + j * box_width + j * box_margin, 
          box_width, 
          box_width, 
          gol.board[i][j] * 2);
      }
    }
    // draw timer text string
    static long start = time(NULL);
    long tick =    time(NULL)  - start;
    char secs[80]; sprintf(secs, "%02ld:%02ld", tick/60, tick%60);
    fl_color(0,0,0);
    fl_font(FL_HELVETICA,16);
    fl_draw(secs, x(), y()+h());
    // game of life update 
    gol.evolve();
    if (hash_cache.find(gol.hasharray()) == hash_cache.end()) {
      hash_cache.insert(gol.hasharray());
    } else {
      std::cout << "done" << std::endl;
      done = true;
    }
    

    counter ++;
  }

  static void Timer_CB(void *userdata) {
    GameOfLifeWindow *o = (GameOfLifeWindow*)userdata;
    if ((*o).done == false) {
      o->redraw();
      Fl::repeat_timeout(0.04, Timer_CB, userdata);
    }
  }

  GameOfLife<n_boxes> gol;

private:

  unsigned char board_display[2*n_boxes][2*n_boxes];
  unsigned int counter = 0;
  std::unordered_set<size_t> hash_cache; 
  bool done = false;

};

int main(int argc, char** argv) {
  Fl_Double_Window win(window_width, window_height);
  float initial_fill_fraction;
  if (argc > 1) {
    initial_fill_fraction = atof(argv[1]);
  } else {
    initial_fill_fraction = 0.5;
  }
  GameOfLifeWindow gol(0, 0, win.w(), win.h(), initial_fill_fraction);
  win.show();
  return(Fl::run());
}

all: ftlk sdl cli

ftlk:
	fltk-config --compile main_fltk.cpp; mv main_fltk gol_fltk.out
cli:
	g++ main_cli.cpp -o gol_cli.out
sdl:
	g++ `sdl2-config --libs --cflags` main_sdl.cpp -o gol_sdl.out

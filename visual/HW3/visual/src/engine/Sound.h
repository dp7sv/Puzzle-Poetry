#ifndef SOUND_H
#define SOUND_H

#include <SDL2/SDL.h>

using namespace std;

class Sound{ 

public:
	Sound();
	~Sound();

	void playSFX();
	void playMusic();
	void loadMusic(const char* filepath);

private:
	SDL_AudioSpec wavSpec, wavHave;
	Uint32  wavLength;
	Uint8 *wavBuffer;
	SDL_AudioDeviceID deviceId;
	
};

#endif
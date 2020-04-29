#ifndef ANIMATIONS_H
#define ANIMATIONS_H

#include <string>

using namespace std;
class Animation{
public:
	Animation();
	Animation(string basepath, int startIndex, int numFrames, int frameRate,bool loop);
	string basepath;
	bool loop;
	int numFrames, frameRate, startIndex, endIndex;
private:

};

#endif
#include "Animations.h"

Animation::Animation(){

}

Animation::Animation(string basepath, int startIndex, int numFrames, int frameRate,bool loop){
	basepath = basepath;
	numFrames = numFrames;
	startIndex = startIndex;
	frameRate = frameRate;
	loop = loop;
}
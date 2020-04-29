#include "AnimatedSprite.h"

AnimatedSprite::AnimatedSprite(){

}

AnimatedSprite::AnimatedSprite(string id){
	id = id;
}

AnimatedSprite::AnimatedSprite(string id, string filepath){
	SDL_Surface* image = IMG_Load(filepath.c_str());
	images.push_back(image);
	id = id;
	curFrame = 0;
	DisplayObject::setImage(image);
}

AnimatedSprite::~AnimatedSprite(){
	int i = 0;
	for(vector<SDL_Surface*>::iterator it = images.begin(); it != images.end(); it++){
		if(i == curFrame){
			continue;
		}
		i++;
		SDL_FreeSurface(*it);
	}images.clear();
	for(unordered_map<string,Animation*>::iterator it2 = animationMap.begin(); it2 != animationMap.end();it2++){
		delete it2->second;
	}
}

void AnimatedSprite::addAnimation(string basepath, string animName, int numFrames, int frameRate, bool loop){
	Animation * a = new Animation(basepath,numFrames,images.size(),frameRate,loop);
	animationMap.emplace(animName,a);
	a->numFrames = numFrames;
	a->frameRate = frameRate;
	a->startIndex = images.size();
	a->endIndex = curFrame + numFrames - 1;
	loop = loop;
	for(int i=1; i<numFrames+1;i++){
		SDL_Surface* image = IMG_Load((basepath + "_" + to_string(i) + ".png").c_str());
		images.push_back(image);
	}
}

Animation* AnimatedSprite::getAnimation(string animName){
	return animationMap[animName];
}

void AnimatedSprite::play(string animName){
	
	Animation* a = getAnimation(animName);
	numFrames = a->numFrames;
	frameRate = a->frameRate;
	loop = a->loop;
	startIndex = a->startIndex;
	curFrame = startIndex;
	endIndex = a->endIndex;
	start = std::clock();
	playing = true;
}

void AnimatedSprite::replay(){
	curFrame = startIndex;
}

void AnimatedSprite::stop(){
	playing = false;
	curFrame = 0;
	DisplayObject::setImage(images[curFrame]);
}

void AnimatedSprite::setFrameRate(int rate){
	frameRate = rate;
}

void AnimatedSprite::update(set<SDL_Scancode> pressedKeys){
	if(playing){
		std::clock_t end = std::clock();
		double duration = (( end - start ) / (double) CLOCKS_PER_SEC)*1000;
		if(duration > frameRate){
			start = end;
			if(curFrame < endIndex){
				curFrame++;
				DisplayObject::setImage(images[curFrame]);
			}else{
				if(loop){
					replay();
					return;
				}stop();
			}
		}
	}
}

void AnimatedSprite::draw(AffineTransform &at){
	Sprite::draw(at);
}
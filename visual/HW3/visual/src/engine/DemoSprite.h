#ifndef DEMOSPRITE_H
#define DEMOSPRITE_H

#include "Sprite.h"

using namespace std;

class DemoSprite : public Sprite{

public:

	DemoSprite();
	DemoSprite(string id, string filepath);
	DemoSprite(string id, int red, int green, int blue);

	virtual void update(set<SDL_Scancode> pressedKeys);
	virtual void draw(AffineTransform &at);

private:

};

#endif

#include "DemoSprite.h"

DemoSprite::DemoSprite() {

}

DemoSprite::DemoSprite(string id, string filepath) :
		Sprite(id, filepath) {

}

DemoSprite::DemoSprite(string id, int red, int green, int blue) :
		Sprite(id, red, green, blue) {

}

void DemoSprite::update(set<SDL_Scancode> pressedKeys) {

	for (SDL_Scancode code : pressedKeys) {
		switch (code) {

		case SDL_SCANCODE_DOWN: {
			Sprite::translateDown();
			break;
		}
		case SDL_SCANCODE_UP: {
			Sprite::translateUp();
			break;
		}
		case SDL_SCANCODE_LEFT: {
			Sprite::translateLeft();
			break;
		}
		case SDL_SCANCODE_RIGHT: {
			Sprite::translateRight();
			break;
		}
		case SDL_SCANCODE_Q: {
			Sprite::scaleOut();
			break;
		}
		case SDL_SCANCODE_W: {
			Sprite::scaleIn();
			break;
		}
		}
	}
	Sprite::update(pressedKeys);

}

void DemoSprite::draw(AffineTransform &at) {
	Sprite::draw(at);
}

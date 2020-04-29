#include "Sprite.h"

Sprite::Sprite(){

}

Sprite::Sprite(string id, string filepath) : DisplayObjectContainer(id,filepath){

}

Sprite::Sprite(string id, int red, int green, int blue) : DisplayObjectContainer(id,red,green,blue){

}

void Sprite::update(set<SDL_Scancode> pressedKeys){
//	cout << "sprite";
}

void Sprite::draw(AffineTransform &at){
	DisplayObjectContainer::draw(at);
}
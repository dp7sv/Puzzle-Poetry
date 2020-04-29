#include <SDL2/SDL.h>
#include <SDL2/SDL_image.h>
#include <iostream>
#include "DisplayObject.h"
#include "DisplayObjectContainer.h"
#include "Scene.h"
#include "Sprite.h"
#include "AnimatedSprite.h"
#include "MyGame.h"

using namespace std;

MyGame::MyGame() : Game(1200, 1000){
	myCamera = Camera::getCamera();
	character = new Scene();
	character->scale(3);
	myCamera->addScene(character);
	this->scene = "./resources/research/out.txt";

	character->loadScene(scene);

}

MyGame::~MyGame(){
//	std::ofstream o("./resources/scenes/test.txt");
//	o << "2 1" << std::endl;
//	o << "0 " << "Scene" << " "<< "0" << " " << "0" << " "<< "0" << " "<< "0" << " "<< "true" << " "<< "false"  << " "<< "0" << " "<< "0" << std::endl;
//	o << "3 " << character->id << " "<< character->imgPath << " " << character->red << " "<< character->green << " "<< character->blue << " "<< std::boolalpha << character->vis << " "<< std::boolalpha << character->isRGB << " "<< character->w << " "<< character->h << std::endl;
//	o << "Scene" << " " << character->id << std::endl;
	//cerr << character->numChildren();
}


void MyGame::update(set<SDL_Scancode> pressedKeys){

	Game::update(pressedKeys);
	DisplayObjectContainer::update(pressedKeys);
	myCamera->update(pressedKeys);

	int x = myCamera->x;
	int y = myCamera->y;

	int cs = 15;

	//these need to be set
	int xmin = -10000;
	int ymin = -10000;
	int xmax = 10000;
	int ymax = 10000;

	//bounds can also be done like this
	if(x>400&&x<500&&y>400&&y<500){
		myCamera->setZoom(250,250);
	}else{
		myCamera->setZoom(500,500);
	}

	for(SDL_Scancode code : pressedKeys){
		switch(code){

			case SDL_SCANCODE_DOWN:
			{
				//character->translateDown();
				if(y<ymax)
					myCamera->pan(0,cs);
				break;
			}case SDL_SCANCODE_UP:
			{
				//character->translateUp();
				if(y>ymin)
				myCamera->pan(0,-cs);
				break;
			}case SDL_SCANCODE_LEFT:
			{
				//character->translateLeft();
				if(x<xmax)
				myCamera->pan(-cs,0);
				break;
			}case SDL_SCANCODE_RIGHT:
			{
				//character->translateRight();
				if(x>xmin)
				myCamera->pan(cs,0);
				break;
			}
			case SDL_SCANCODE_Q:
			 {
			 	//character->scaleOut();
				 myCamera->zoom(2, 2);
			 	break;
			 }case SDL_SCANCODE_W:
			 {
			 	//character->scaleIn();
				myCamera->zoom(.5, .5);
			 	break;
			 }
			//case SDL_SCANCODE_A:
			// {
			// 	character->rotateCW();
			// 	break;
			// }case SDL_SCANCODE_S:
			// {
			// 	character->rotateCCW();
			// 	break;
			// }
			// case SDL_SCANCODE_I: 
			// {
			// 	character->movePivotUp();
			// 	break;
			// }case SDL_SCANCODE_J:
			// {
			// 	character->movePivotLeft();
			// 	break;
			// }case SDL_SCANCODE_K:
			// {
			// 	character->movePivotDown();
			// 	break;
			// }case SDL_SCANCODE_L:
			// {
			// 	character->movePivotRight();
			// 	break;

			// }case SDL_SCANCODE_Z:
			// {
			// 	character->increaseAlpha();
			// 	break;
			// }case SDL_SCANCODE_X:
			// {
			// 	character->decreaseAlpha();
			// 	break;
			// }

			case SDL_SCANCODE_P:
			{
				effect.playMusic();
				break;
			}
		}
	}

}

void MyGame::draw(AffineTransform &at){
	Game::draw(at);
//	myCamera->draw(at);
	SDL_RenderClear(Game::renderer);
	myCamera->draw(at);
	DisplayObjectContainer::draw(at);
	SDL_RenderPresent(Game::renderer);
}

#include "DisplayObject.h"
#include <string>
#include <SDL2/SDL.h>
#include <SDL2/SDL_image.h>
#include "Game.h"
#include <iostream>
#include <algorithm>

DisplayObject::DisplayObject(){
	image = NULL;
	texture = NULL;
	curTexture = NULL;
	vis = true;
	alpha = 255;
	position.x = 0;
	position.y = 0;
	pivot.x = 0; pivot.y = 0;
}

DisplayObject::DisplayObject(string id, string filepath){
	this->id = id;
	this->imgPath = filepath;

	loadTexture(filepath);
}

DisplayObject::DisplayObject(string id, int red, int green, int blue){
	isRGB = true;
	this->id = id;

	this->red = red;
	this->blue = blue;
	this->green = green;

	this->loadRGBTexture(red, green, blue);
}

DisplayObject::~DisplayObject(){
	if(image != NULL) SDL_FreeSurface(image);
	if(texture != NULL) SDL_DestroyTexture(texture);
	
}

void DisplayObject::loadTexture(string filepath){
	image = IMG_Load(filepath.c_str());
	if (image == NULL){
		printf("Bad filepath. \n");
	}
	texture = SDL_CreateTextureFromSurface(Game::renderer, image);
	setTexture(texture);
	w = image->w;
	h = image->h;
	vis = true;
	alpha = 255;
	position.x = 0;
	position.y = 0;
	pivot.x = 0; pivot.y = 0;
}

void DisplayObject::setImage(SDL_Surface* img){
	image = img;
	if(texture != NULL) SDL_DestroyTexture(texture);
	texture = SDL_CreateTextureFromSurface(Game::renderer, image);
	setTexture(texture);
	w = image->w;
	h = image->h;
}

void DisplayObject::loadRGBTexture(int red, int green, int blue){
	image = SDL_CreateRGBSurface(0, 100, 100, 32, 0, 0, 0, 0x000000ff);
	SDL_FillRect(image, NULL, SDL_MapRGB(image->format, red, green, blue));
	texture = SDL_CreateTextureFromSurface(Game::renderer, image);
	SDL_SetTextureBlendMode( texture, SDL_BLENDMODE_BLEND );
	setTexture(texture);
}

void DisplayObject::setTexture(SDL_Texture* t){
	this->curTexture = t;
}

void DisplayObject::decreaseAlpha(){
	alpha -= 10;
	alpha = alpha < 0 ? 0 : alpha;
	SDL_SetTextureAlphaMod(curTexture,alpha);
}

void DisplayObject::increaseAlpha(){
	alpha += 10;
	alpha = alpha > 255 ? 255 : alpha;
	SDL_SetTextureAlphaMod(curTexture,alpha);
}

void DisplayObject::setAlpha(int a){
	alpha = a;
}

void DisplayObject::toggleVisibility(){
	vis = !vis;
}

void DisplayObject::makeVisible(){
	vis = true;
}

void DisplayObject::makeInvisible(){
	vis = false;
}

void DisplayObject::movePivotLeft(){
	pivot.x -= 2;
}

void DisplayObject::movePivotRight(){
	pivot.x += 2;
}

void DisplayObject::movePivotUp(){
	pivot.y -= 2;
}

void DisplayObject::movePivotDown(){
	pivot.y += 2;
}

void DisplayObject::translateRight(){
	position.x += speed;
}

void DisplayObject::translateLeft(){
	position.x -= speed;
}

void DisplayObject::translateUp(){
	position.y -= speed;
}

void DisplayObject::translateDown(){
	position.y += speed;
}

void DisplayObject::moveTo(int x, int y){
	position.x = x;
	position.y = y;
}

void DisplayObject::movePivot(int x, int y){
	pivot.x = x;
	pivot.y = y;
}

void DisplayObject::scaleIn(){
	scaleX *= .9;
	scaleY *= .9;
}

void DisplayObject::scaleOut(){
	scaleX *= 1.1;
	scaleY *= 1.1;
}

void DisplayObject::scale(double s){
	scaleX *= s;
	scaleY *= s;
}

void DisplayObject::setScale(double x, double y){
	scaleX = x;
	scaleY = y;
}

void DisplayObject::setRotation(double angle){
	rotationAmount = angle*PI/180;
}

void DisplayObject::setRotationValue(double angle){
	rotation = angle*PI/180;
}

double DisplayObject::getRotation(){
	return rotationAmount;
}

void DisplayObject::rotateCW(){
	rotation += rotationAmount;
}

void DisplayObject::rotateCCW(){
	rotation -= rotationAmount;
}

double DisplayObject::dist(SDL_Point &a, SDL_Point &b){
	return sqrt((b.y-a.y)*(b.y-a.y) + (b.x-a.x)*(b.x-a.x));
}

SDL_Point DisplayObject::getPivot(){
	return this->pivot;
}

SDL_Point DisplayObject::getPosition(){
	return this->position;
}

void DisplayObject::setSpeed(int s){
	speed = s;
}

void DisplayObject::applyTransformations(AffineTransform &at){
	at.translate(position.x,position.y);
	at.rotate(rotation);
	at.scale(scaleX,scaleY);
}

void DisplayObject::reverseTransformations(AffineTransform &at){
	at.scale(1/scaleX,1/scaleY);
	at.rotate(-rotation);
	at.translate(-position.x,-position.y);
}

void DisplayObject::update(set<SDL_Scancode> pressedKeys){

}

void DisplayObject::draw(AffineTransform &at){

	if(curTexture != NULL){
		if(!vis){return;}

		applyTransformations(at);
		at.translate(-pivot.x,-pivot.y);
		
		SDL_Point topL = at.transformPoint(0,0);
		SDL_Point topR = at.transformPoint(w,0);
		SDL_Point bottomR = at.transformPoint(w,h);

		SDL_Point pOrigin;
		pOrigin.x = 0; pOrigin.y = 0;
		
		int distAdj = dist(topL,topR);
		int distOpp = dist(topR,bottomR);
		SDL_Rect dstrect = { topL.x, topL.y, distAdj, distOpp};

		double angle = atan2(topR.y-topL.y,topR.x-topL.x)*180/PI;

		SDL_RenderCopyEx(Game::renderer, curTexture, NULL, &dstrect, angle, &pOrigin, SDL_FLIP_NONE);	
		
		at.translate(pivot.x,pivot.y);
		reverseTransformations(at);

	}
}





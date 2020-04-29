#include <SDL2/SDL.h>
#include <SDL2/SDL_image.h>
#include <cmath>
#include "AffineTransform.h"
#include <iostream>
#include <cmath>

/**
 * Affine Transforms
 * 
 * */	
AffineTransform::AffineTransform(){
	transform = identity();
}

AffineTransform::~AffineTransform(){
	cleanMatrix(transform);
}

void AffineTransform::cleanMatrix(double** m){
	for(int i=0; i<3; i++)
		delete m[i];
	delete m;
}

/* Returns the identity matrix as an array */ 
double** AffineTransform::identity(){
	double** id = new double*[3];
	for(int i=0; i<3; i++){
		id[i] = new double[3];
		for(int j=0; j<3; j++){
			if(i == j) id[i][j] = 1.0;
			else id[i][j] = 0.0;
		}
	}
	return id;
}

/* Takes a point in the local coordinate system and transforms it to global space given this AffineTransform */ 
SDL_Point AffineTransform::transformPoint(int x, int y){	
	//TODO in future assignment
	SDL_Point temp;

	//check
	temp.x = (transform[0][0]*x) + (transform[0][1]*y) + transform[0][2];
	temp.y = (transform[1][0]*x) + (transform[1][1]*y) + transform[1][2];
	return temp;
}

/* Add another transform to this one, is basically just matrix multiply */
void AffineTransform::concatenate(AffineTransform &at){
	//TODO in future assignment
	double** newIdentity = identity();
	for(int i=0;i<3;i++){
		for(int j=0;j<3;j++){
			newIdentity[i][j] = 0;
			for(int k=0;k<3;k++){
				newIdentity[i][j] += transform[i][k] * at.transform[k][j];
			}
		}
	}

	cleanMatrix(transform);
	transform = newIdentity;
}

/* Move points in the x and y direction */
void AffineTransform::translate(int x, int y){
	//TODO in future assignment
	AffineTransform at = AffineTransform();
	at.transform[0][2] = x;
	at.transform[1][2] = y;
	concatenate(at);
}

/* rotate points by r radians */
void AffineTransform::rotate(double r){
	//TODO in future assignment
	AffineTransform at = AffineTransform();
	at.transform[0][0] = cos(r);
	at.transform[0][1] = -sin(r);
	at.transform[1][0] = sin(r);
	at.transform[1][1] = cos(r);
	concatenate(at);
}

/* scale in the x and y direction accordingly */
void AffineTransform::scale(double x, double y){
	//TODO in future assignment
	AffineTransform at = AffineTransform();
	at.transform[0][0] = x;
	at.transform[1][1] = y;
	concatenate(at);
}

double AffineTransform::getScaleX(){
	//TODO in future assignment
	return transform[0][0];
}

double AffineTransform::getScaleY(){
	//TODO in future assignment
	return transform[1][1];
}
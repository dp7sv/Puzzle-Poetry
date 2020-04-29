#ifndef CAMERA_H
#define CAMERA_H

#include "DisplayObject.h"
#include "DisplayObjectContainer.h"

class Camera{ 

public:
	Camera();
	~Camera();

	int x = 0;
	int y = 0;
	int viewportWidth = 500;
	int viewportHeight = 500;

	static Camera* getCamera();

	void addScene(DisplayObject* child);
	void removeScene(DisplayObject* child);

	void pan(int dx, int dy);
	void zoom(double x, double y);

	void setLocation(int newX, int newY);
	void setZoom(double w, double h);

	void update(set<SDL_Scancode> pressedKeys);
	void draw(AffineTransform &at);


private:

	static Camera* camera;
	DisplayObjectContainer* container;
	
};


#endif

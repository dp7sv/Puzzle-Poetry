#ifndef SCENE_H
#define SCENE_H

#include "DisplayObjectContainer.h"
#include "Sprite.h"
#include "DemoSprite.h"
#include <string>
#include <vector>
#include <fstream>

using namespace std;

class Scene : public DisplayObjectContainer{

public:
	Scene();

	/* Load scene from a file */
	void loadScene(string sceneFilePath);

	/*Save scene to a file, used for testing*/
	void saveScene(string sceneFilePath);

	virtual void update(set<SDL_Scancode> pressedKeys);
	virtual void draw(AffineTransform &at);

	const string paths[12] = { "./resources/research/blue.png",
				"./resources/research/gold.png", "./resources/research/green.png",
				"./resources/research/indigo.png", "./resources/research/lime.png",
				"./resources/research/orange.png", "./resources/research/pink.png",
				"./resources/research/purple.png", "./resources/research/red.png",
				"./resources/research/teal.png", "./resources/research/white.png",
				"./resources/research/yellow.png" };

	std::ifstream i;

private:

};

#endif

#include "Scene.h"
#include <iostream>
//#include "json.hpp"
//#include "jsonConversions.h"
// for convenience

Scene::Scene() :
		DisplayObjectContainer() {
	//just calling parent constructor
}

/* Load scene from a file */
void Scene::loadScene(string sceneFilePath) {
	i.open(sceneFilePath);



}

void Scene::saveScene(string sceneFilePath) {
//code retrieved from https://github.com/nlohmann/json
//	json j = this;
//	std::ofstream o(sceneFilePath);
//	o << std::setw(4) << j << std::endl;
}

void Scene::update(set<SDL_Scancode> pressedKeys) {
	DisplayObjectContainer::update(pressedKeys);
	auto find = pressedKeys.find(SDL_SCANCODE_SPACE);
	if (find != pressedKeys.end()) {
		children.clear();
		for (int j = 0; j < 12; j++) {
			long temp;
			i >> hex >> temp;
			for (int k = 6; k--; k += 0) {
				for (int l = 10; l--; l += 0) {
					if (temp & 1) {
						DisplayObject *tempTile = new DisplayObject("default",
								paths[j]);
						tempTile->moveTo(32 * l, 32 * k);
						addChild(tempTile);
					}
					temp >>= 1;
				}
			}
		}
		SDL_Delay(100);
	}
}
void Scene::draw(AffineTransform &at) {
	DisplayObjectContainer::draw(at);
}

#include "Camera.h"

Camera *Camera::camera = 0;

Camera::Camera() {

}
Camera::~Camera() {

}

Camera* Camera::getCamera() {
	if (camera == 0) {
		camera = new Camera();
		camera->container = new DisplayObjectContainer();
		(camera->container)->id = "camera";
	}
	return camera;
}

void Camera::addScene(DisplayObject *child) {
	container->addChild(child);
}

void Camera::removeScene(DisplayObject *child) {
	container->removeImmediateChild(child);
}

void Camera::pan(int dx, int dy) {
	x += dx;
	y += dy;
}
void Camera::zoom(double x, double y) {
	viewportWidth = (int) (x * viewportWidth);
	viewportHeight = (int) (y * viewportHeight);
}

void Camera::setLocation(int newX, int newY) {
	x = newX;
	y = newY;
}
void Camera::setZoom(double w, double h) {
	viewportWidth = w;
	viewportHeight = h;
}

void Camera::update(set<SDL_Scancode> pressedKeys) {
	container->moveTo(-x, -y);
	container->movePivot(-viewportWidth/2, -viewportHeight/2);
	container->setScale(1.0 * viewportWidth / 500.0,
			1.0 * viewportHeight / 500.0);
	container->update(pressedKeys);
}
void Camera::draw(AffineTransform &at) {
	container->draw(at);
}

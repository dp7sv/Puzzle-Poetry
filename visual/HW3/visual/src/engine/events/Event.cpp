#include "Event.h"

Event::Event(string type, EventDispatcher* source){
	eventType = type;
	source = source;
}

string Event::getType(){
	return eventType;
}

EventDispatcher* Event::getSource(){
	return source;
}

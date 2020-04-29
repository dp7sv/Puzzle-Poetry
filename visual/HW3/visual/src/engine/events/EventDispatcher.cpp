#include "EventDispatcher.h"

EventDispatcher::EventDispatcher(){
	listeners = new std::unordered_map<std::string, std::vector<EventListener*>*>;
}

EventDispatcher::~EventDispatcher(){
	//TODO: Find out if map destructor automatically frees container memory.
	for(auto it = listeners->begin(); it != listeners->end(); ++it){
		vector<EventListener*> *l = it->second;
		for(int i = 0; i < l->size(); i++){
			delete (*l)[i];
		}
		l->clear();
		delete l;
	}
	delete listeners;
}

void EventDispatcher::addEventListener(EventListener* l, string eventType){
	if(!(*listeners)[eventType])
		(*listeners)[eventType] = new std::vector<EventListener*>;
	(*listeners)[eventType]->push_back(l);
}

void EventDispatcher::removeEventListener(EventListener* l, string eventType){
	if(listeners->find(eventType) != listeners->end()){
		vector<EventListener*> *vec = (*listeners)[eventType];
		for (auto it = vec->begin(); it != vec->end(); ++it){
			if(*it == l){
				delete *it;
				vec->erase(it);
				return;
			}
		}
	}

}

bool EventDispatcher::hasEventListener(EventListener* l, string eventType){
	auto it = listeners->find(eventType);
	return it != listeners->end();
}

void EventDispatcher::dispatchEvent(Event* e){
	vector<EventListener*> *l = (*listeners)[e->getType()];

	for (EventListener* listener : *l)
		listener->handleEvent(e);
}
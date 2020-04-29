#include "QuestManager.h"
#include <iostream>

QuestManager::QuestManager(){

}

void QuestManager::handleEvent(Event* e){
	if(e->getType() == "COIN_PICKED_UP"){
		cout << "Quest is complete" << endl;
	}
}
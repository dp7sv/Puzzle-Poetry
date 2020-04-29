#include "Event.h"
#include "Sprite.h"
class Sprite;
class EventDispatcher;
class Coin : public EventDispatcher, public Sprite{
public:
  Coin(string id, string filepath) : Sprite(id, filepath){
    this->pickedUp = new Event("COIN_PICKED_UP", this);

  }
  ~Coin(){
    delete this->pickedUp;
  }

  virtual void dispatchEvent(){
    EventDispatcher::dispatchEvent(pickedUp);
  }
  
private:
  Event *pickedUp;
};

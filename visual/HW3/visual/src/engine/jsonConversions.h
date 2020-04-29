////using json = nlohmann::json;
//
//using nlohmann::json;
//
//#include "DisplayObject.h"
//#include "DisplayObjectContainer.h"
//#include "Scene.h"
//#include "Sprite.h"
//#include "AnimatedSprite.h"
//
////namespace Scene {
//void to_json(json &j, const Scene &p) {
////	j = json { { "id", p.id }, { "imgPath", p.imgPath }, { "red", p.red }, { "green", p.green }, { "blue", p.blue }, { "type", p.type }, { "vis", p.vis }, { "isRGB", p.isRGB }, { "w", p.w }, { "h", p.h }, { "children", p.children } };
//}
//
//void from_json(const json &j, Scene &p) {
//	j.at("id").get_to(p.id);
//	j.at("imgPath").get_to(p.imgPath);
//	j.at("red").get_to(p.red);
//	j.at("green").get_to(p.green);
//	j.at("blue").get_to(p.blue);
//	j.at("type").get_to(p.type);
//	j.at("vis").get_to(p.vis);
//	j.at("isRGB").get_to(p.isRGB);
//	j.at("w").get_to(p.w);
//	j.at("h").get_to(p.h);
//	j.at("children").get_to(p.children);
//}
////}
///*
// //namespace DisplayObject {
// void to_json(json &j, const DisplayObject &p) {
// j = json { { "id", p.id }, { "imgPath", p.imgPath }, { "red", p.red }, { "green", p.green }, { "blue", p.blue }, { "type", p.type }, { "vis", p.vis }, { "isRGB", p.isRGB }, { "w", p.w }, { "h", p.h } };
// }
//
// void from_json(const json &j, DisplayObject &p) {
// j.at("id").get_to(p.id);
// j.at("imgPath").get_to(p.imgPath);
// j.at("red").get_to(p.red);
// j.at("green").get_to(p.green);
// j.at("blue").get_to(p.blue);
// j.at("type").get_to(p.type);
// j.at("vis").get_to(p.vis);
// j.at("isRGB").get_to(p.isRGB);
// j.at("w").get_to(p.w);
// j.at("h").get_to(p.h);
// }
// //}
//
// //namespace DisplayObjectContainer {
// void to_json(json &j, const DisplayObjectContainer &p) {
// j = json { { "id", p.id }, { "imgPath", p.imgPath }, { "red", p.red }, { "green", p.green }, { "blue", p.blue }, { "type", p.type }, { "vis", p.vis }, { "isRGB", p.isRGB }, { "w", p.w }, { "h", p.h }, { "children", p.children } };
// }
//
// void from_json(const json &j, DisplayObjectContainer &p) {
// j.at("id").get_to(p.id);
// j.at("imgPath").get_to(p.imgPath);
// j.at("red").get_to(p.red);
// j.at("green").get_to(p.green);
// j.at("blue").get_to(p.blue);
// j.at("type").get_to(p.type);
// j.at("vis").get_to(p.vis);
// j.at("isRGB").get_to(p.isRGB);
// j.at("w").get_to(p.w);
// j.at("h").get_to(p.h);
// j.at("children").get_to(p.children);
// }
// //}
//
// //namespace Sprite {
// void to_json(json &j, const Sprite &p) {
// j = json { { "id", p.id }, { "imgPath", p.imgPath }, { "red", p.red }, { "green", p.green }, { "blue", p.blue }, { "type", p.type }, { "vis", p.vis }, { "isRGB", p.isRGB }, { "w", p.w }, { "h", p.h }, { "children", p.children } };
// }
//
// void from_json(const json &j, Sprite &p) {
// j.at("id").get_to(p.id);
// j.at("imgPath").get_to(p.imgPath);
// j.at("red").get_to(p.red);
// j.at("green").get_to(p.green);
// j.at("blue").get_to(p.blue);
// j.at("type").get_to(p.type);
// j.at("vis").get_to(p.vis);
// j.at("isRGB").get_to(p.isRGB);
// j.at("w").get_to(p.w);
// j.at("h").get_to(p.h);
// j.at("children").get_to(p.children);
// }
// //}
//
// //namespace AnimatedSprite {
//
// void to_json(json &j, const AnimatedSprite &p) {
// j = json { { "id", p.id }, { "imgPath", p.imgPath }, { "red", p.red }, { "green", p.green }, { "blue", p.blue }, { "type", p.type }, { "vis", p.vis }, { "isRGB", p.isRGB }, { "w", p.w }, { "h", p.h }, { "children", p.children }, { "playing", p.playing }, { "curFrame", p.curFrame }, { "frameRate", p.frameRate }, { "startIndex", p.startIndex }, { "endIndex", p.endIndex }, { "numFrames", p.numFrames }, { "start", p.start }, { "loop", p.loop } };
// }
//
// void from_json(const json &j, AnimatedSprite &p) {
// j.at("id").get_to(p.id);
// j.at("imgPath").get_to(p.imgPath);
// j.at("red").get_to(p.red);
// j.at("green").get_to(p.green);
// j.at("blue").get_to(p.blue);
// j.at("type").get_to(p.type);
// j.at("vis").get_to(p.vis);
// j.at("isRGB").get_to(p.isRGB);
// j.at("w").get_to(p.w);
// j.at("h").get_to(p.h);
// j.at("children").get_to(p.children);
// j.at("playing").get_to(p.playing);
// j.at("curFrame").get_to(p.curFrame);
// j.at("frameRate").get_to(p.frameRate);
// j.at("startIndex").get_to(p.startIndex);
// j.at("endIndex").get_to(p.endIndex);
// j.at("numFrames").get_to(p.numFrames);
// j.at("start").get_to(p.start);
// j.at("loop").get_to(p.loop);
// }
// //}
//
// */

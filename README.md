A blender addon to allow an external xbuf compatible renderer (like a game engine) to be used in blender viewport. The addon provide a generic (renderer agnostic) client that connect to a running server (a game) and display server image into Blender.

License: [GPL](LICENSE.txt)

> The addon is WIP

# Changes in Branch feature-dupligroups
In Blender you can "Duplicate a Group" from another Blender File. This happens when linking in a blender file and selecting a group.
After a group has been linked into blender, you can alt+d to duplicate them.  
This feature will add a UserData `SYS_LOAD_J3O`, which contains the path (relative to the AssetManager) to the blender file containing the Duplicate Group.  
Note that this does not honor what the group consists of, because typically you use this method to link in the whole scene (and thus create a group containing all objects).  
Other ways of linking (e.g. a complete scene) are not support and the UserData needs handling in UserCode but thus does not require changes to the importer.

# Uses Cases

* Preview model with game engine
* Use Blender as level editor for a game (or for a game engine) with realtime rendering (including effects, hud, entities,... not managed by blender)

[![blender external renderer (a game engine)](youtube_img.png)](http://www.youtube.com/watch?v=3pQd65_dkeM)


## Installation

1. download the zip from [releases section](https://github.com/xbuf/blender_io_xbuf/releases)
2. in Blender : User Preferences... > Add-ons > Install from File... (select the downloaded .zip)
3. in Blender : User Preferences... > Add-ons > enable the addon (check box of "Render: Xbuf Render Engine")

## Usage

1. start your xbuf render engine (eg: [jme3_ext's ModelViewer](https://github.com/davidB/jme3_ext_assettools/releases))
2. in Blender : Select "Xbuf Render" in the render list
3. in Blender : Check properties of Render > Xbuf Render Config
  * the connection parameters : host + port
  * the auto redraw : usefull to see animation in viewport, else disable it (note that some other addon like screenshot_key_view have same effects)
  * the path where to store textures and third party files
4. in Blender : Select "Rendered" in the viewport shading button of 3D View
5. in your xbuf compatible render engine :
  * refresh UI if needed (ModelViewer's spatial explorer right-click)
  * display bounding, skeleton,...
  * explore, play animation
  * every action possible by your render

Notes:

* Some properties panel could not be available with Xbuf Render, switch to "Blender Render" to access them (and open an issue, so I'll add them).
* Only animation (action) stored in an NLA's strip are sent to the external render engine.
* The addon includes an exporter for .xbuf (the default format use to send scene to external render engine). But .xbuf need the files store in your assets path to be loaded.

## Setup used for the video-demo

* Blender 2.72b
* [blender_external_renderer 0.3.0](https://github.com/davidB/blender_external_renderer/releases/tag/0.3.0)
* ModelViewer 0.3.0 for jMonkeyEngine from [jme3_ext_assettools](https://github.com/davidB/jme3_ext_assettools/releases/tag/0.3.0)

# Inspirations

* [GameKit](https://github.com/gamekit-developers/gamekit)
* Blender Game Engine
*  Video of [Harts Antler](https://www.youtube.com/channel/UCtHoHRAtqPzTZh52H6dgloQ) like :
  * [pyppet2-webGL-streaming-test1.mp4 - YouTube](https://www.youtube.com/watch?v=_4Qb_2LneJ8)
  * [b2ogre-0.5.5-anim-tracks.mp4 - YouTube](https://www.youtube.com/watch?v=5oVM0Lmeb68)

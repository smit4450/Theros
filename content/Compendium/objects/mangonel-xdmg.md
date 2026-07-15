---
obsidianUIMode: preview
cssclasses:
- json5e-object
tags:
- compendium/src/5e/xdmg
- object/size/large
- object/type/siege-weapon
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Mangonel"
---
# Mangonel
*Source: Dungeon Master's Guide (2024) p. 97*

![](/Compendium/objects/img/mangonel.webp#right)

A Mangonel is a catapult that hurls heavy projectiles in a high arc, so it can hit targets behind walls. Loading a Mangonel requires two [Utilize](/Compendium/rules/actions.md#Utilize) actions, and aiming it requires two more [Utilize](/Compendium/rules/actions.md#Utilize) actions. Then a crew member can take the Mangonel Stone action.
```statblock
"name": "Mangonel"
"size": "Large"
"ac": !!int "15"
"hp": !!int "100"
"stats":
  - !!int "10"
  - !!int "10"
  - !!int "10"
  - !!int "10"
  - !!int "10"
  - !!int "10"
"actions":
  - "desc": "Ranged Attack Roll: +5, range 200/800 ft. (can't hit targets within\
      \ 60 feet of itself). Hit: 27 (5d10) Bludgeoning damage."
    "name": "Mangonel Stone (Requires Load and Aim)"
"source":
  - "XDMG"
"image": "/Compendium/objects/token/mangonel-xdmg.webp"
```
^statblock
---
obsidianUIMode: preview
cssclasses:
- json5e-object
tags:
- compendium/src/5e/xdmg
- object/size/huge
- object/type/siege-weapon
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Trebuchet"
---
# Trebuchet
*Source: Dungeon Master's Guide (2024) p. 97*

A Trebuchet is a catapult that throws its payload in a high arc so it can hit targets behind walls. Loading a Trebuchet requires two [Utilize](/Compendium/rules/actions.md#Utilize) actions, and aiming it requires two more [Utilize](/Compendium/rules/actions.md#Utilize) actions. Then a crew member can take the Trebuchet Stone action.
```statblock
"name": "Trebuchet"
"size": "Huge"
"ac": !!int "15"
"hp": !!int "150"
"stats":
  - !!int "10"
  - !!int "10"
  - !!int "10"
  - !!int "10"
  - !!int "10"
  - !!int "10"
"actions":
  - "desc": "Ranged Attack Roll: +5, range 300/1,200 ft. (can't hit targets within\
      \ 60 feet of itself). Hit: 44 (8d10) Bludgeoning damage."
    "name": "Trebuchet Stone (Requires Load and Aim)"
"source":
  - "XDMG"
"image": "/Compendium/objects/token/trebuchet-xdmg.webp"
```
^statblock
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
- "Cannon"
---
# Cannon
*Source: Dungeon Master's Guide (2024) p. 96*

A Cannon uses gunpowder or arcane power to propel heavy iron balls at destructive speeds. A Cannon is usually attached to a wooden frame with wheels. Loading a Cannon requires the [Utilize](/Compendium/rules/actions.md#Utilize) action, and aiming it requires another [Utilize](/Compendium/rules/actions.md#Utilize) action. Then a crew member can take the Cannonball action.
```statblock
"name": "Cannon"
"size": "Large"
"ac": !!int "19"
"hp": !!int "75"
"stats":
  - !!int "10"
  - !!int "10"
  - !!int "10"
  - !!int "10"
  - !!int "10"
  - !!int "10"
"actions":
  - "desc": "Ranged Attack Roll: +6, range 600/2,400 ft. Hit: 44 (8d10) Bludgeoning\
      \ damage."
    "name": "Cannonball (Requires Load and Aim)"
"source":
  - "XDMG"
"image": "/Compendium/objects/token/cannon-xdmg.webp"
```
^statblock
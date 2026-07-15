---
obsidianUIMode: preview
cssclasses:
- json5e-object
tags:
- compendium/src/5e/xdmg
- object/size/medium
- object/type/siege-weapon
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Lightning Cannon"
---
# Lightning Cannon
*Source: Dungeon Master's Guide (2024) p. 96*

A Lightning Cannon is a small, bronze cannon inlaid with arcane runes and mounted on a heavy tripod device. It launches balls of crackling electricity. Aiming a Lightning Cannon requires the [Utilize](/Compendium/rules/actions.md#Utilize) action, then a crew member can take the Lightning Ball action.
```statblock
"name": "Lightning Cannon"
"size": "Medium"
"ac": !!int "19"
"hp": !!int "30"
"stats":
  - !!int "10"
  - !!int "10"
  - !!int "10"
  - !!int "10"
  - !!int "10"
  - !!int "10"
"actions":
  - "desc": "Ranged Attack Roll: +6, range 300/1,200 ft. Hit: 22 (4d10) Lightning\
      \ damage."
    "name": "Lightning Ball (Requires Aim)"
"source":
  - "XDMG"
"image": "/Compendium/objects/token/lightning-cannon-xdmg.webp"
```
^statblock
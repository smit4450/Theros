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
- "Ram"
---
# Ram
*Source: Dungeon Master's Guide (2024) p. 97*

A Ram consists of a movable gallery equipped with a heavy log suspended from two roof beams by chains. The log is shod in iron and used to batter through doors and barricades. Positioning a Ram requires three [Utilize](/Compendium/rules/actions.md#Utilize) actions. Then a crew member can use the Ram action.

The gallery roof gives the operators [Total Cover](/Compendium/tables/cover-xphb.md) against attacks and other effects from above.
```statblock
"name": "Ram"
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
  - "desc": "Melee Attack Roll: +8, reach 5 ft. Hit: 16 (3d10) Bludgeoning damage."
    "name": "Ram (Requires Position)"
"source":
  - "XDMG"
"image": "/Compendium/objects/token/ram-xdmg.webp"
```
^statblock
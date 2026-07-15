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
- "Ballista"
---
# Ballista
*Source: Dungeon Master's Guide (2024) p. 96*

A Ballista is a massive crossbow that fires heavy bolts. Loading a Ballista requires the [Utilize](/Compendium/rules/actions.md#Utilize) action, and aiming it requires another [Utilize](/Compendium/rules/actions.md#Utilize) action. Then a crew member can take the Ballista Bolt action.
```statblock
"name": "Ballista"
"size": "Large"
"ac": !!int "15"
"hp": !!int "50"
"stats":
  - !!int "10"
  - !!int "10"
  - !!int "10"
  - !!int "10"
  - !!int "10"
  - !!int "10"
"actions":
  - "desc": "Ranged Attack Roll: +6, range 120/480 ft. Hit: 16 (3d10) Piercing\
      \ damage."
    "name": "Ballista Bolt (Requires Load and Aim)"
"source":
  - "XDMG"
"image": "/Compendium/objects/token/ballista-xdmg.webp"
```
^statblock
---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xphb
- monster/cr/
- monster/size/medium
- monster/type/elemental
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Elemental Spirit"
---
# Elemental Spirit
*Source: Player's Handbook (2024) p. 325*
![](/Compendium/bestiary/elemental/img/elemental-spirit.webp#center)

```statblock
"name": "Elemental Spirit"
"size": "Medium"
"type": "elemental"
"alignment": "Neutral"
"ac_class": "11 + the spell's level"
"modifier": !!int "2"
"stats":
  - !!int "18"
  - !!int "15"
  - !!int "17"
  - !!int "4"
  - !!int "10"
  - !!int "16"
"speed": "40 ft., burrow 40 ft. (Earth only), fly 40 ft. (hover; Air only), swim 40\
  \ ft. (Water only)"
"damage_resistances": "lightning, thunder (Air only)"
"damage_immunities": "poison; fire (Fire only)"
"condition_immunities": "[exhaustion](/Compendium/rules/conditions.md#Exhaustion),\
  \ [paralyzed](/Compendium/rules/conditions.md#Paralyzed), [petrified](/Compendium/rules/conditions.md#Petrified),\
  \ [poisoned](/Compendium/rules/conditions.md#Poisoned)"
"senses": "[Darkvision](/Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception\
  \ 10"
"languages": "Primordial, understands the languages you know"
"traits":
  - "desc": "The spirit can move through a space as narrow as 1 inch wide without\
      \ it counting as Difficult Terrain."
    "name": "Amorphous Form (Air, Fire, and Water Only)"
"actions":
  - "desc": "The spirit makes a number of Slam attacks equal to half this spell's\
      \ level (round down)."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* Bonus equals your spell attack modifier, reach 5\
      \ ft. *Hit:* 1d10 + 4 + the spell's level Bludgeoning (Earth only), Cold (Water\
      \ only), Lightning (Air only), or Fire (Fire only) damage."
    "name": "Slam"
"source":
  - "XPHB"
"image": "/Compendium/bestiary/elemental/token/elemental-spirit-xphb.webp"
```
^statblock
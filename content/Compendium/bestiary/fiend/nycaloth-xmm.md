---
title: Nycaloth
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/9
- ttrpg-cli/monster/environment/gehenna
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/fiend/yugoloth
statblock: inline
aliases: ["Nycaloth"]
---
# Nycaloth
*Source: Monster Manual (2024) p. 229*  

![](Compendium/books/monster-manual-2025/img/nycaloth.webp#right)  
## Nycaloth

*Yugoloth of Strategy and Strife*

- **Habitat.** Planar (Gehenna)  
- **Treasure.** [[random-magic-items-armaments|Armaments]]  

Fiendish warmongers, nycaloths relish combat and conquest. These tremendous winged yugoloths teleport around battlefields and into the air to bewilder their foes and attack with constantly shifting, Gehenna-forged axes—mercurial weapons similar to those favored by many yugoloths.

Nycaloths might command groups of mezzoloths and make pacts to serve arcanaloths, ultroloths, fiendish warlords, or wicked mortals. So long as they can indulge their bloodlust, most nycaloths are willing to obey more powerful or cunning creatures. Some even serve competent leaders past the terms of their agreements to achieve long-pursued victories. But masters that lead nycaloths to defeat should fear these proud yugoloths' retribution.

Nycaloths and other yugoloths frequently serve as mercenary forces in extraplanar conflicts that spill onto the Material Plane. Roll on or choose a result from the Yugoloth Incursions table to inspire the plans of a yugoloth war band.

**Yugoloth Incursions**

| dice: 1d4 | Yugoloth Mercenaries Seek To... |
|-----------|---------------------------------|
| 1 | Claim a portal with strategic importance. |
| 2 | Enlist monsters as allies or beasts of war. |
| 3 | Destroy a city harboring enemy cultists. |
| 4 | Liberate an imprisoned fiendish ally. |
^yugoloth-incursions
```statblock
"name": "Nycaloth (XMM)"
"size": "Large"
"type": "fiend"
"subtype": "yugoloth"
"alignment": "Neutral Evil"
"ac": !!int "18"
"hp": !!int "152"
"hit_dice": "16d10 + 64"
"modifier": !!int "4"
"stats":
  - !!int "20"
  - !!int "11"
  - !!int "19"
  - !!int "12"
  - !!int "10"
  - !!int "15"
"speed": "40 ft., fly 60 ft."
"skillsaves":
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+4"
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+4"
"damage_resistances": "cold, fire, lightning"
"damage_immunities": "acid, poison"
"condition_immunities": "[[conditions#Poisoned|poisoned]]"
"senses": "[[senses#Blindsight|Blindsight]] 60 ft., passive Perception\
  \ 14"
"languages": "Abyssal, Infernal; telepathy 60 ft."
"cr": "9"
"traits":
  - "desc": "If the nycaloth dies outside Gehenna, its body dissolves into ichor,\
      \ and it gains a new body instantly, reviving with all its [[hit-points-xphb|Hit Points]]\
      \ somewhere in Gehenna."
    "name": "Fiendish Restoration"
  - "desc": "The nycaloth has [[advantage-xphb|Advantage]]\
      \ on saving throws against spells and other magical effects."
    "name": "Magic Resistance"
"actions":
  - "desc": "The nycaloth makes two Mercurial Axe attacks."
    "name": "Multiattack"
  - "desc": "*Melee  or Ranged Attack Roll:* +9, reach 10 ft. or range 30/90 ft.\
      \ *Hit:* 18 (2d12 + 5) Slashing damage plus 10 (3d6) Force damage. *Hit\
      \ or Miss:* The axe magically returns to the nycaloth's hand immediately after\
      \ a ranged attack."
    "name": "Mercurial Axe"
"bonus_actions":
  - "desc": "The nycaloth has the [[conditions#Invisible|Invisible]]\
      \ condition for 1 minute, and it teleports up to 30 feet to an unoccupied space\
      \ it can see. The condition ends early immediately after it deals damage."
    "name": "Shadowy Teleport"
"source":
  - "XMM"
"image": "Compendium/bestiary/fiend/token/nycaloth-xmm.webp"
```
^statblock
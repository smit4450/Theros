---
title: Banshee
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/environment/any
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Banshee"]
---
# Banshee
*Source: Monster Manual (2024) p. 29*  

![](Compendium/bestiary/undead/img/banshee.webp#right|850)  
## Banshee

*Wailing Harbinger of Death*

- **Habitat.** Any  
- **Treasure.** [Relics](Compendium/tables/random-magic-items-relics.md)  

Heralds of doom and plagues on the living, banshees are spirits obsessed by unresolved bitterness or sorrow. These storied phantoms slay any who glimpse them or hear their baleful wails. Although any tormented soul can arise as a banshee, some elven communities particularly fear them and believe that those who hoard or destroy beauty—natural or otherwise—risk returning as a banshee.

All manner of torments might give rise to a banshee. Roll on or choose a result from the Banshee Sorrows table to inspire how a banshee's torment influences its behavior.

**Banshee Sorrows**

| dice: 1d6 | Torment Compels the Banshee To... |
|-----------|-----------------------------------|
| 1 | Appear prior to a family member's death. |
| 2 | Haunt the site where it was executed. |
| 3 | Lament a lost love and haunt their grave. |
| 4 | Presage a disaster or tragedy. |
| 5 | Seek the return of a stolen treasure. |
| 6 | Slay those more beautiful than it was in life. |
^banshee-sorrows
```statblock
"name": "Banshee (XMM)"
"size": "Medium"
"type": "undead"
"alignment": "Chaotic Evil"
"ac": !!int "12"
"hp": !!int "54"
"hit_dice": "12d8"
"modifier": !!int "2"
"stats":
  - !!int "1"
  - !!int "14"
  - !!int "10"
  - !!int "12"
  - !!int "11"
  - !!int "17"
"speed": "5 ft., fly 40 ft. (hover)"
"saves":
  - "wisdom": !!int "2"
"damage_resistances": "acid, bludgeoning, fire, lightning, piercing, slashing, thunder"
"damage_immunities": "cold, necrotic, poison"
"condition_immunities": "[charmed](Compendium/rules/conditions.md#Charmed), [exhaustion](Compendium/rules/conditions.md#Exhaustion),\
  \ [frightened](Compendium/rules/conditions.md#Frightened), [grappled](Compendium/rules/conditions.md#Grappled),\
  \ [paralyzed](Compendium/rules/conditions.md#Paralyzed), [petrified](Compendium/rules/conditions.md#Petrified),\
  \ [poisoned](Compendium/rules/conditions.md#Poisoned), [prone](Compendium/rules/conditions.md#Prone),\
  \ [restrained](Compendium/rules/conditions.md#Restrained)"
"senses": "[Darkvision](Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception\
  \ 10"
"languages": "Common, Elvish"
"cr": "4"
"traits":
  - "desc": "The banshee magically senses the direction of creatures up to 1 mile\
      \ away that aren't Constructs or Undead."
    "name": "Detect Life"
  - "desc": "The banshee can move through other creatures and objects as if they were\
      \ [Difficult Terrain](Compendium/rules/variant-rules/difficult-terrain-xphb.md).\
      \ It takes 5 (1d10) Force damage if it ends its turn inside an object."
    "name": "Incorporeal Movement"
"actions":
  - "desc": "The banshee makes two Corrupting Touch attacks and uses Horrify."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +5, reach 5 ft. *Hit:* 7 (1d8 + 3) Necrotic\
      \ damage."
    "name": "Corrupting Touch"
  - "desc": "*Wisdom Saving Throw:* DC 13, one creature the banshee can see within\
      \ 60 feet that can see the banshee. *Failure:* The target has the [Frightened](Compendium/rules/conditions.md#Frightened)\
      \ condition until the start of the banshee's next turn. *Success:* The target\
      \ is immune to this banshee's Horrify for 24 hours."
    "name": "Horrify"
  - "desc": "The banshee releases a mournful wail if it isn't in sunlight. *Constitution\
      \ Saving Throw:* DC 13, each creature within 30 feet that can hear the wail\
      \ and isn't a Construct or an Undead. *Failure:* If the target has 25 [Hit Points](Compendium/rules/variant-rules/hit-points-xphb.md)\
      \ or fewer, it drops to 0 [Hit Points](Compendium/rules/variant-rules/hit-points-xphb.md).\
      \ Otherwise, the target takes 10 (3d6) Psychic damage."
    "name": "Deathly Wail (1/Day)"
"source":
  - "XMM"
"image": "Compendium/bestiary/undead/token/banshee-xmm.webp"
```
^statblock
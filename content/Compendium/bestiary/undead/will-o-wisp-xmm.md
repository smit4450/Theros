---
title: "Will-o'-Wisp"
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/2
- monster/environment/forest
- monster/environment/swamp
- monster/environment/urban
- monster/size/tiny
- monster/type/undead
statblock: inline
aliases: ["Will-o'-Wisp"]
---
# Will-o'-Wisp
*Source: Monster Manual (2024) p. 333, FRHoF. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/books/monster-manual-2025/img/will-o-wisp.webp#right)  
## Will-o'-Wisp

*Guide on the Path to Doom*

- **Habitat.** Forest, Swamp, Urban  
- **Treasure.** None  

From a distance, will-o'-wisps look like lanterns bobbing in the dark. Through the windows of abandoned structures or around the bends of treacherous paths, these spirits tempt the curious into peril. Once their prey is vulnerable, will-o'-wisps feed on the life force of those they lay low.

Roll on or choose a result from the Will-o'-Wisp Ambushes table to inspire how a will-o'-wisp imperils its victims.

**Will-o'-Wisp Ambushes**

| dice: 1d6 | The Will-o'-Wisp Tempts Victims Into... |
|-----------|-----------------------------------------|
| 1 | An abandoned structure ready to collapse. |
| 2 | An ambush by hungry ghouls or vampires. |
| 3 | A dreaded ruin that curses those who enter. |
| 4 | The lair of a predator, like a bear or wyvern. |
| 5 | Patches of brown mold or green slime. |
| 6 | Quicksand or pools covered in thin ice. |
^will-o-wisp-ambushes
```statblock
"name": "Will-o'-Wisp (XMM)"
"size": "Tiny"
"type": "undead"
"alignment": "Chaotic Evil"
"ac": !!int "19"
"hp": !!int "27"
"hit_dice": "11d4"
"modifier": !!int "9"
"stats":
  - !!int "1"
  - !!int "28"
  - !!int "10"
  - !!int "13"
  - !!int "14"
  - !!int "11"
"speed": "5 ft., fly 50 ft. (hover)"
"damage_resistances": "acid, bludgeoning, cold, fire, necrotic, piercing, slashing"
"damage_immunities": "lightning, poison"
"condition_immunities": "[[conditions#Exhaustion|exhaustion]],\
  \ [[conditions#Grappled|grappled]], [[conditions#Paralyzed|paralyzed]],\
  \ [[conditions#Petrified|petrified]], [[conditions#Poisoned|poisoned]],\
  \ [[conditions#Prone|prone]], [[conditions#Restrained|restrained]],\
  \ [[conditions#Unconscious|unconscious]]"
"senses": "[[senses#Darkvision|Darkvision]] 120 ft., passive Perception\
  \ 12"
"languages": "Common plus one other language"
"cr": "2"
"traits":
  - "desc": "The wisp can't wear or carry anything."
    "name": "Ephemeral"
  - "desc": "The wisp sheds [[bright-light-xphb|Bright Light]]\
      \ in a 20-foot radius and [[dim-light-xphb|Dim Light]]\
      \ for an additional 20 feet."
    "name": "Illumination"
  - "desc": "The wisp can move through other creatures and objects as if they were\
      \ [[difficult-terrain-xphb|Difficult Terrain]].\
      \ It takes 5 (1d10) Force damage if it ends its turn inside an object."
    "name": "Incorporeal Movement"
"actions":
  - "desc": "*Melee Attack Roll:* +4, reach 5 ft. *Hit:* 11 (2d8 + 2) Lightning\
      \ damage."
    "name": "Shock"
"bonus_actions":
  - "desc": "*Constitution Saving Throw:* DC 10, one living creature the wisp can\
      \ see within 5 feet that has 0 [[hit-points-xphb|Hit Points]].\
      \ *Failure:* The target dies, and the wisp regains 10 (3d6) [[hit-points-xphb|Hit Points]]."
    "name": "Consume Life"
  - "desc": "The wisp and its light have the [[conditions#Invisible|Invisible]]\
      \ condition until the wisp's [[conditions#Concentration|Concentration]]\
      \ ends on this effect, which ends early immediately after the wisp makes an\
      \ attack roll or uses Consume Life."
    "name": "Vanish"
"source":
  - "XMM"
  - "FRHoF"
"image": "Compendium/bestiary/undead/token/will-o-wisp-xmm.webp"
```
^statblock
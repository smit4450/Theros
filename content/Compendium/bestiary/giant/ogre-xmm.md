---
title: Ogre
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/2
- monster/environment/arctic
- monster/environment/desert
- monster/environment/forest
- monster/environment/grassland
- monster/environment/hill
- monster/environment/mountain
- monster/environment/swamp
- monster/environment/underdark
- monster/size/large
- monster/type/giant
statblock: inline
aliases: ["Ogre"]
---
# Ogre
*Source: Monster Manual (2024) p. 231. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/giant/img/ogres.webp#right|850)  
Ogres are 10-foot-tall brutes that overwhelm their foes and take what spoils they please. Ogre raiders ally with other evil forces in return for food, riches, and promises of battle.

## Ogres

*Raging Hulks and Hoarders*

- **Habitat.** Arctic, Desert, Forest, Grassland, Hill, Mountain, Swamp, Underdark  
- **Treasure.** [[random-magic-items-armaments|Armaments]]  

Ogres are selfish raiders and hulking gluttons spawned of hateful supernatural forces. From dismal ruins and bleak hinterlands, they raid vulnerable communities and ambush travelers. Ogres covet food and treasure, and they spitefully destroy art, books, clockwork devices, and other delicate or lovingly made things. Occasionally they kidnap victims to eat later or, more rarely, performers who catch their interest.

Ogres trace their origins to wrathful deities such as Erythnul, Takhisis, and Vaprak. They magically emerge from the earth of lands corrupted by evil gods, sinister magic, or ancient curses. Some bear evidence of the places that spawned them, sporting rocky calluses, mossy growths, or frozen scars.
## Statblock

```statblock
"name": "Ogre (XMM)"
"size": "Large"
"type": "giant"
"alignment": "Chaotic Evil"
"ac": !!int "11"
"hp": !!int "68"
"hit_dice": "8d10 + 24"
"modifier": !!int "-1"
"stats":
  - !!int "19"
  - !!int "8"
  - !!int "16"
  - !!int "5"
  - !!int "7"
  - !!int "7"
"speed": "40 ft."
"senses": "[[senses#Darkvision|Darkvision]] 60 ft., passive Perception\
  \ 8"
"languages": "Common, Giant"
"cr": "2"
"actions":
  - "desc": "*Melee Attack Roll:* +6, reach 5 ft. *Hit:* 13 (2d8 + 4) Bludgeoning\
      \ damage."
    "name": "Greatclub"
  - "desc": "*Melee  or Ranged Attack Roll:* +6, reach 5 ft. or range 30/120 ft.\
      \ *Hit:* 11 (2d6 + 4) Piercing damage."
    "name": "Javelin"
"source":
  - "XMM"
"image": "Compendium/bestiary/giant/token/ogre-xmm.webp"
```
^statblock
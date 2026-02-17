---
title: Dire Worg
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/10
- monster/environment/feywild
- monster/environment/forest
- monster/environment/grassland
- monster/environment/hill
- monster/environment/planar
- monster/size/huge
- monster/type/fey
statblock: inline
aliases: ["Dire Worg"]
---
# Dire Worg
*Source: Monster Manual (2024) p. 335*  

![](Compendium/bestiary/fey/img/dire-worg.webp#right|850)  
Dire worgs are larger than common worgs and possess a supernaturally terrifying howl. They frequently hunt alongside ettins, ogres, and trolls.

## Worgs

*Malicious Lupine Ravagers*

- **Habitat.** Forest, Grassland, Hill, Planar (Feywild)  
- **Treasure.** None  

Sometimes mistaken at first for giant wolves, worgs are vicious hunters. These sapient predators can speak and often taunt their prey, enjoying the taste of fear in their meals.
## Statblock

```statblock
"name": "Dire Worg (XMM)"
"size": "Huge"
"type": "fey"
"alignment": "Neutral Evil"
"ac": !!int "16"
"hp": !!int "147"
"hit_dice": "14d12 + 56"
"modifier": !!int "2"
"stats":
  - !!int "22"
  - !!int "14"
  - !!int "18"
  - !!int "7"
  - !!int "16"
  - !!int "8"
"speed": "50 ft."
"saves":
  - "dexterity": !!int "6"
  - "wisdom": !!int "7"
"skillsaves":
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+11"
"senses": "[[senses#Darkvision|Darkvision]] 120 ft., passive Perception\
  \ 21"
"languages": "Goblin, Sylvan, Worg"
"cr": "10"
"traits":
  - "desc": "The worg has [[advantage-xphb|Advantage]]\
      \ on saving throws against spells and other magical effects."
    "name": "Magic Resistance"
"actions":
  - "desc": "The worg makes three Bite attacks."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +10, reach 5 ft. *Hit:* 15 (2d8 + 6) Piercing\
      \ damage plus 7 (2d6) Poison damage, and the target has the [[conditions#Poisoned|Poisoned]]\
      \ condition until the start of the worg's next turn. While [[conditions#Poisoned|Poisoned]],\
      \ the target can't regain [[hit-points-xphb|Hit Points]]."
    "name": "Bite"
  - "desc": "*Wisdom Saving Throw:* DC 16, each creature within 30 feet that isn't\
      \ a worg. *Failure:* 36 (8d8) Psychic damage, and the target has the [[conditions#Frightened|Frightened]]\
      \ condition until the start of the worg's next turn. *Success:* Half damage\
      \ only."
    "name": "Dreadful Howl (Recharge 5-6)"
"bonus_actions":
  - "desc": "The worg teleports, along with a willing creature of its choice within\
      \ 5 feet of it, up to 30 feet to an unoccupied space it can see."
    "name": "Warp Step"
"source":
  - "XMM"
"image": "Compendium/bestiary/fey/token/dire-worg-xmm.webp"
```
^statblock
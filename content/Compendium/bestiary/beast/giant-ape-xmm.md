---
title: Giant Ape
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/7
- monster/environment/forest
- monster/size/huge
- monster/type/beast
statblock: inline
aliases: ["Giant Ape"]
---
# Giant Ape
*Source: Monster Manual (2024) p. 354. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/beast/img/giant-ape-and-giant-bat.webp#right|850)  
## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [[panther-xmm|Panther]] stat block can also represent a mountain lion, while the [[giant-goat-xmm|Giant Goat]] stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.
![A druid calls on animals o...](Compendium/bestiary/beast/img/animals-hills-and-mountains.webp#center)  
![Aquatic animals swim along...](Compendium/bestiary/beast/img/animals-aquatic.webp#center)  
![Inhabitants of the rain fo...](Compendium/bestiary/beast/img/animals-rainforest.webp#center)  
```statblock
"name": "Giant Ape (XMM)"
"size": "Huge"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "12"
"hp": !!int "168"
"hit_dice": "16d12 + 64"
"modifier": !!int "5"
"stats":
  - !!int "23"
  - !!int "14"
  - !!int "18"
  - !!int "5"
  - !!int "12"
  - !!int "7"
"speed": "40 ft., climb 40 ft."
"skillsaves":
  - "name": "[[skills#Athletics|Athletics]]"
    "desc": "+9"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+4"
  - "name": "[[skills#Survival|Survival]]"
    "desc": "+4"
"senses": "passive Perception 14"
"languages": ""
"cr": "7"
"actions":
  - "desc": "The ape makes two Fist attacks."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +9, reach 10 ft. *Hit:* 22 (3d10 + 6) Bludgeoning\
      \ damage."
    "name": "Fist"
  - "desc": "The ape hurls a boulder at a point it can see within 90 feet. *Dexterity\
      \ Saving Throw:* DC 17, each creature in a 5-foot-radius [[sphere-area-of-effect-xphb|Sphere]]\
      \ centered on that point. *Failure:* 24 (7d6) Bludgeoning damage. If the target\
      \ is a Large or smaller creature, it has the [[conditions#Prone|Prone]]\
      \ condition. *Success:* Half damage only."
    "name": "Boulder Toss (Recharge 6)"
"bonus_actions":
  - "desc": "The ape jumps up to 30 feet by spending 10 feet of movement."
    "name": "Leap"
"source":
  - "XMM"
"image": "Compendium/bestiary/beast/token/giant-ape-xmm.webp"
```
^statblock
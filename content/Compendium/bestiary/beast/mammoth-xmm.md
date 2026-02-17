---
title: Mammoth
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/6
- monster/environment/arctic
- monster/size/huge
- monster/type/beast
statblock: inline
aliases: ["Mammoth"]
---
# Mammoth
*Source: Monster Manual (2024) p. 365. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![A druid calls on animals o...](Compendium/bestiary/beast/img/animals-hills-and-mountains.webp#right|850)  
## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [[panther-xmm|Panther]] stat block can also represent a mountain lion, while the [[giant-goat-xmm|Giant Goat]] stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.
![Aquatic animals swim along...](Compendium/bestiary/beast/img/animals-aquatic.webp#center)  
![Inhabitants of the rain fo...](Compendium/bestiary/beast/img/animals-rainforest.webp#center)  
```statblock
"name": "Mammoth (XMM)"
"size": "Huge"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "13"
"hp": !!int "126"
"hit_dice": "11d12 + 55"
"modifier": !!int "2"
"stats":
  - !!int "24"
  - !!int "9"
  - !!int "21"
  - !!int "3"
  - !!int "11"
  - !!int "6"
"speed": "50 ft."
"saves":
  - "strength": !!int "10"
  - "constitution": !!int "8"
"senses": "passive Perception 10"
"languages": ""
"cr": "6"
"actions":
  - "desc": "The mammoth makes two Gore attacks."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +10, reach 10 ft. *Hit:* 18 (2d10 + 7) Piercing\
      \ damage. If the target is a Huge or smaller creature and the mammoth moved\
      \ 20+ feet straight toward it immediately before the hit, the target has the\
      \ [[conditions#Prone|Prone]] condition."
    "name": "Gore"
"bonus_actions":
  - "desc": "*Dexterity Saving Throw:* DC 18, one creature within 5 feet that has\
      \ the [[conditions#Prone|Prone]] condition. *Failure:* 29\
      \ (4d10 + 7) Bludgeoning damage. *Success:* Half damage."
    "name": "Trample"
"source":
  - "XMM"
"image": "Compendium/bestiary/beast/token/mammoth-xmm.webp"
```
^statblock
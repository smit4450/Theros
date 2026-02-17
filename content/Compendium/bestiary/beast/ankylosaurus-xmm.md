---
title: Ankylosaurus
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/3
- monster/environment/grassland
- monster/size/huge
- monster/type/beast/dinosaur
statblock: inline
aliases: ["Ankylosaurus"]
---
# Ankylosaurus
*Source: Monster Manual (2024) p. 348. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/beast/img/ankylosaurus.webp#right|850)  
## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [[panther-xmm|Panther]] stat block can also represent a mountain lion, while the [[giant-goat-xmm|Giant Goat]] stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.
![A druid calls on animals o...](Compendium/bestiary/beast/img/animals-hills-and-mountains.webp#center)  
![Aquatic animals swim along...](Compendium/bestiary/beast/img/animals-aquatic.webp#center)  
![Inhabitants of the rain fo...](Compendium/bestiary/beast/img/animals-rainforest.webp#center)  
```statblock
"name": "Ankylosaurus (XMM)"
"size": "Huge"
"type": "beast"
"subtype": "dinosaur"
"alignment": "Unaligned"
"ac": !!int "15"
"hp": !!int "68"
"hit_dice": "8d12 + 16"
"modifier": !!int "0"
"stats":
  - !!int "19"
  - !!int "11"
  - !!int "15"
  - !!int "2"
  - !!int "12"
  - !!int "5"
"speed": "30 ft."
"saves":
  - "strength": !!int "6"
"senses": "passive Perception 11"
"languages": ""
"cr": "3"
"actions":
  - "desc": "The ankylosaurus makes two Tail attacks."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +6, reach 10 ft. *Hit:* 9 (1d10 + 4) Bludgeoning\
      \ damage. If the target is a Huge or smaller creature, it has the [[conditions#Prone|Prone]]\
      \ condition."
    "name": "Tail"
"source":
  - "XMM"
"image": "Compendium/bestiary/beast/token/ankylosaurus-xmm.webp"
```
^statblock
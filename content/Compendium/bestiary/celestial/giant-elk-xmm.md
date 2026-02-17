---
title: Giant Elk
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/2
- monster/environment/forest
- monster/environment/grassland
- monster/environment/hill
- monster/size/huge
- monster/type/celestial
statblock: inline
aliases: ["Giant Elk"]
---
# Giant Elk
*Source: Monster Manual (2024) p. 356, FRHoF. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/celestial/img/elk.webp#right|850)  
## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [[panther-xmm|Panther]] stat block can also represent a mountain lion, while the [[giant-goat-xmm|Giant Goat]] stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.
![A druid calls on animals o...](Compendium/bestiary/beast/img/animals-hills-and-mountains.webp#center)  
![Aquatic animals swim along...](Compendium/bestiary/beast/img/animals-aquatic.webp#center)  
![Inhabitants of the rain fo...](Compendium/bestiary/beast/img/animals-rainforest.webp#center)  
```statblock
"name": "Giant Elk (XMM)"
"size": "Huge"
"type": "celestial"
"alignment": "Neutral Good"
"ac": !!int "14"
"hp": !!int "42"
"hit_dice": "5d12 + 10"
"modifier": !!int "6"
"stats":
  - !!int "19"
  - !!int "18"
  - !!int "14"
  - !!int "7"
  - !!int "14"
  - !!int "10"
"speed": "60 ft."
"saves":
  - "strength": !!int "6"
  - "dexterity": !!int "6"
"skillsaves":
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+4"
"damage_resistances": "necrotic, radiant"
"senses": "[[senses#Darkvision|Darkvision]] 90 ft., passive Perception\
  \ 14"
"languages": "Celestial; understands Common, Elvish, and Sylvan but can't speak them"
"cr": "2"
"actions":
  - "desc": "*Melee Attack Roll:* +6, reach 10 ft. *Hit:* 11 (2d6 + 4) Bludgeoning\
      \ damage plus 5 (2d4) Radiant damage. If the target is a Huge or smaller creature\
      \ and the elk moved 20+ feet straight toward it immediately before the hit,\
      \ the target takes an extra 5 (2d4) Bludgeoning damage and has the [[conditions#Prone|Prone]]\
      \ condition."
    "name": "Ram"
"source":
  - "XMM"
  - "FRHoF"
"image": "Compendium/bestiary/celestial/token/giant-elk-xmm.webp"
```
^statblock
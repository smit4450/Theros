---
title: Allosaurus
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/beast/dinosaur
statblock: inline
aliases: ["Allosaurus"]
---
# Allosaurus
*Source: Monster Manual (2024) p. 348. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/beast/img/allosaurus.webp#right)  
## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.
![A druid calls on animals o...](Compendium/bestiary/beast/img/animals-hills-and-mountains.webp#center)  
![Aquatic animals swim along...](Compendium/bestiary/beast/img/animals-aquatic.webp#center)  
![Inhabitants of the rain fo...](Compendium/bestiary/beast/img/animals-rainforest.webp#center)  
```statblock
"name": "Allosaurus (XMM)"
"size": "Large"
"type": "beast"
"subtype": "dinosaur"
"alignment": "Unaligned"
"ac": !!int "13"
"hp": !!int "51"
"hit_dice": "6d10 + 18"
"modifier": !!int "1"
"stats":
  - !!int "19"
  - !!int "13"
  - !!int "17"
  - !!int "2"
  - !!int "12"
  - !!int "5"
"speed": "60 ft."
"skillsaves":
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+5"
"senses": "passive Perception 15"
"languages": ""
"cr": "2"
"actions":
  - "desc": "*Melee Attack Roll:* +6, reach 5 ft. *Hit:* 15 (2d10 + 4) Piercing\
      \ damage."
    "name": "Bite"
  - "desc": "*Melee Attack Roll:* +6, reach 5 ft. *Hit:* 8 (1d8 + 4) Slashing\
      \ damage. If the target is a Large or smaller creature and the allosaurus moved\
      \ 30+ feet straight toward it immediately before the hit, the target has the\
      \ [Prone](Compendium/rules/conditions.md#Prone) condition, and the allosaurus\
      \ can make one Bite attack against it."
    "name": "Claws"
"source":
  - "XMM"
"image": "Compendium/bestiary/beast/token/allosaurus-xmm.webp"
```
^statblock
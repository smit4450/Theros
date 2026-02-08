---
title: Archelon
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/environment/underwater
- ttrpg-cli/monster/size/huge
- ttrpg-cli/monster/type/beast/dinosaur
statblock: inline
aliases: ["Archelon"]
---
# Archelon
*Source: Monster Manual (2024) p. 349. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/beast/img/archelon.webp#right)  
## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.
![A druid calls on animals o...](Compendium/bestiary/beast/img/animals-hills-and-mountains.webp#center)  
![Aquatic animals swim along...](Compendium/bestiary/beast/img/animals-aquatic.webp#center)  
![Inhabitants of the rain fo...](Compendium/bestiary/beast/img/animals-rainforest.webp#center)  
```statblock
"name": "Archelon (XMM)"
"size": "Huge"
"type": "beast"
"subtype": "dinosaur"
"alignment": "Unaligned"
"ac": !!int "17"
"hp": !!int "90"
"hit_dice": "12d12 + 12"
"modifier": !!int "3"
"stats":
  - !!int "18"
  - !!int "16"
  - !!int "13"
  - !!int "4"
  - !!int "14"
  - !!int "6"
"speed": "20 ft., swim 80 ft."
"skillsaves":
  - "name": "[Stealth](Compendium/rules/skills.md#Stealth)"
    "desc": "+5"
"senses": "passive Perception 12"
"languages": ""
"cr": "4"
"traits":
  - "desc": "The archelon can breathe air and water."
    "name": "Amphibious"
"actions":
  - "desc": "The archelon makes two Bite attacks."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +6, reach 5 ft. *Hit:* 14 (3d6 + 4) Piercing\
      \ damage."
    "name": "Bite"
"source":
  - "XMM"
"image": "Compendium/bestiary/beast/token/archelon-xmm.webp"
```
^statblock
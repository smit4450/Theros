---
title: Amphisbaena
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/gos
- monster/cr/1-2
- monster/size/medium
- monster/type/monstrosity
statblock: inline
aliases: ["Amphisbaena"]
---
# Amphisbaena
*Source: Ghosts of Saltmarsh p. 230, Mythic Odysseys of Theros*  

![](Compendium/bestiary/monstrosity/img/amphisbaena.webp#right|850)  
Found in Danger at Dunwater, these strange reptiles have a head at either end of their serpentine bodies, each one equipped with venomous fangs. To move, an amphisbaena uses one head to grip the neck of its other head, forming a hoop that rolls over the ground.
```statblock
"name": "Amphisbaena (GoS)"
"size": "Medium"
"type": "monstrosity"
"alignment": "Unaligned"
"ac": !!int "14"
"hp": !!int "11"
"hit_dice": "2d8 + 2"
"modifier": !!int "4"
"stats":
  - !!int "14"
  - !!int "18"
  - !!int "12"
  - !!int "3"
  - !!int "10"
  - !!int "3"
"speed": "30 ft., swim 30 ft."
"skillsaves":
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+2"
"senses": "[[senses#Blindsight|blindsight]] 10 ft., passive Perception\
  \ 12"
"languages": ""
"cr": "1/2"
"traits":
  - "desc": "The amphisbaena has advantage on Wisdom ([[skills#Perception|Perception]])\
      \ checks and on saving throws against being [[conditions#Blinded|blinded]],\
      \ [[conditions#Charmed|charmed]], [[conditions#Deafened|deafened]],\
      \ [[conditions#Frightened|frightened]], [[conditions#Stunned|stunned]],\
      \ and knocked [[conditions#Unconscious|unconscious]]."
    "name": "Two Heads"
"actions":
  - "desc": "The amphisbaena makes two bite attacks."
    "name": "Multiattack"
  - "desc": "*Melee Weapon Attack:* +6 to hit, reach 5 ft., one target. *Hit:* 6\
      \ (1d4 + 4) piercing damage, and the target must make a DC 11 Constitution\
      \ saving throw, taking 3 (1d6) poison damage on a failed save, or half as\
      \ much damage on a successful one."
    "name": "Bite"
"source":
  - "GoS"
  - "MOT"
"image": "Compendium/bestiary/monstrosity/token/amphisbaena-gos.webp"
```
^statblock
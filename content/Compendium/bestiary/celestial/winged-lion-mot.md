---
title: Winged Lion
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/mot
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/celestial
statblock: inline
aliases: ["Winged Lion"]
---
# Winged Lion
*Source: Mythic Odysseys of Theros p. 214*  

Archons always ride into battle on fearsome winged mounts. Some legends suggest that the mount is actually a physical manifestation of the archon's will, allowing the pair to act with a single mind. The two most common archon mounts are winged bulls and winged lions.
```statblock
"name": "Winged Lion (MOT)"
"size": "Large"
"type": "celestial"
"alignment": "Unaligned"
"ac": !!int "13"
"hp": !!int "114"
"hit_dice": "12d10 + 48"
"modifier": !!int "3"
"stats":
  - !!int "20"
  - !!int "16"
  - !!int "18"
  - !!int "6"
  - !!int "14"
  - !!int "5"
"speed": "60 ft., fly 60 ft."
"senses": "passive Perception 12"
"languages": "understands Celestial but can't speak"
"cr": "4"
"traits":
  - "desc": "If the lion moves at least 20 feet straight toward a creature and then\
      \ hits it with a claw attack on the same turn, that target must succeed on a\
      \ DC 15 Strength saving throw or be knocked [[conditions#Prone|prone]].\
      \ If the target is [[conditions#Prone|prone]], the lion can\
      \ make one bite attack against it as a bonus action."
    "name": "Pounce"
"actions":
  - "desc": "*Melee Weapon Attack:* +7 to hit, reach 5 ft., one target. *Hit:* 16\
      \ (2d10 + 5) piercing damage."
    "name": "Bite"
  - "desc": "*Melee Weapon Attack:* +7 to hit, reach 5 ft., one target. *Hit:* 14\
      \ (2d8 + 5) slashing damage."
    "name": "Claw"
"source":
  - "MOT"
"image": "Compendium/bestiary/celestial/token/winged-lion-mot.webp"
```
^statblock
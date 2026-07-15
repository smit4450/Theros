---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/mot
- monster/cr/1
- monster/size/medium
- monster/type/monstrosity
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Nyx-Fleece Ram"
---
# Nyx-Fleece Ram
*Source: Mythic Odysseys of Theros p. 233*
![](/Compendium/bestiary/monstrosity/img/nyx-fleece-ram.webp#right)

Touched by the gods, Nyx-fleece rams grow remarkable magical wool. This makes the beasts valuable to heroes and scoundrels alike, who would use their wool for either protection or profit. Divine servants guard the few herds of Nyx-fleece rams dwelling among Theros's loftiest peaks, assuring they don't fall into unworthy hands.

```statblock
"name": "Nyx-Fleece Ram"
"size": "Medium"
"type": "monstrosity"
"alignment": "Unaligned"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "27"
"hit_dice": "5d8 + 5"
"modifier": !!int "2"
"stats":
  - !!int "16"
  - !!int "14"
  - !!int "12"
  - !!int "3"
  - !!int "13"
  - !!int "10"
"speed": "40 ft."
"senses": "passive Perception 11"
"languages": ""
"cr": "1"
"traits":
  - "desc": "If the ram moves at least 20 feet straight toward a target and then hits\
      \ it with a ram attack on the same turn, the target takes an extra 5 (2d4) bludgeoning\
      \ damage. If the target is a creature, it must succeed on a DC 13 Strength saving\
      \ throw or be knocked [prone](/Compendium/rules/conditions.md#Prone)."
    "name": "Charge"
  - "desc": "The ram has advantage on saving throws against spells and other magical\
      \ effects."
    "name": "Magic Resistance"
  - "desc": "The ram has advantage on Strength and Dexterity saving throws against\
      \ effects that would knock it [prone](/Compendium/rules/conditions.md#Prone)."
    "name": "Sure-Footed"
"actions":
  - "desc": "*Melee Weapon Attack:* +5 to hit, reach 5 ft., one target. *Hit:* 8 (2d4\
      \ + 3) bludgeoning damage plus 3 (1d6) force damage."
    "name": "Ram"
"source":
  - "MOT"
"image": "/Compendium/bestiary/monstrosity/token/nyx-fleece-ram-mot.webp"
```
^statblock
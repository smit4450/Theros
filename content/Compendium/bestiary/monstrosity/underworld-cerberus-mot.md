---
title: Underworld Cerberus
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/mot
- ttrpg-cli/monster/cr/6
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Underworld Cerberus"]
---
# Underworld Cerberus
*Source: Mythic Odysseys of Theros p. 215*  

![](Compendium/bestiary/monstrosity/img/underworld-cerberus.webp#right|850)  
Three-headed cerberi dwell deep in the Underworld. Terrifying and cunning, they guard portals between the wards of the Underworld, Erebos's greatest treasures, and noteworthy souls who might attempt to escape the realm of the dead. Three-headed cerberi commonly serve demons, but if left to their own devices, they often herd wily souls into labyrinthine Underworld wildernesses, then hunt them for sport.

Feared by the living and the dead, cerberi patrol both banks of the Tartyx River. These multiheaded hounds of the Underworld breathe gouts of molten rock that sear and imprison those who trespass upon the borders of life and death. Most cerberi have a boundless hunger for fresh meat, especially the flesh of humanoids. Villains have been known to exploit that hunger by luring cerberi away from the river and setting them loose on mortal settlements.
```statblock
"name": "Underworld Cerberus (MOT)"
"size": "Large"
"type": "monstrosity"
"alignment": "Lawful Evil"
"ac": !!int "16"
"ac_class": "natural armor"
"hp": !!int "104"
"hit_dice": "11d10 + 44"
"modifier": !!int "1"
"stats":
  - !!int "19"
  - !!int "12"
  - !!int "18"
  - !!int "10"
  - !!int "16"
  - !!int "9"
"speed": "60 ft."
"skillsaves":
  - "name": "[Athletics](Compendium/rules/skills.md#Athletics)"
    "desc": "+7"
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+9"
  - "name": "[Stealth](Compendium/rules/skills.md#Stealth)"
    "desc": "+4"
"damage_immunities": "fire, necrotic"
"condition_immunities": "[blinded](Compendium/rules/conditions.md#Blinded), [charmed](Compendium/rules/conditions.md#Charmed),\
  \ [deafened](Compendium/rules/conditions.md#Deafened), [exhaustion](Compendium/rules/conditions.md#Exhaustion),\
  \ [frightened](Compendium/rules/conditions.md#Frightened), [stunned](Compendium/rules/conditions.md#Stunned)"
"senses": "[truesight](Compendium/rules/senses.md#Truesight) 30 ft., passive Perception\
  \ 19"
"languages": "understands all languages but can't speak"
"cr": "6"
"traits":
  - "desc": "As a bonus action, the cerberus can move up to its speed toward a hostile\
      \ creature that it can see."
    "name": "Aggressive"
  - "desc": "The cerberus can't be [surprised](Compendium/rules/conditions.md#Surprised),\
      \ and it has advantage on saving throws against being knocked [unconscious](Compendium/rules/conditions.md#Unconscious)."
    "name": "Multiheaded"
  - "desc": "The cerberus has advantage on an attack roll against a creature if at\
      \ least one of the cerberus's allies is within 5 feet of the creature and the\
      \ ally isn't [incapacitated](Compendium/rules/conditions.md#Incapacitated)."
    "name": "Pack Tactics"
"actions":
  - "desc": "The cerberus makes three bite attacks."
    "name": "Multiattack"
  - "desc": "*Melee Weapon Attack:* +7 to hit, reach 5 ft., one target. *Hit:* 11\
      \ (2d6 + 4) piercing damage plus 3 (1d6) fire damage."
    "name": "Bite"
  - "desc": "The cerberus exhales a 30-foot cone of molten rock. Each creature in\
      \ the cone must make a DC 15 Dexterity saving throw, taking 21 (6d6) fire\
      \ damage on a failed save, or half as much damage on a successful one. On a\
      \ failed save, a creature is also [restrained](Compendium/rules/conditions.md#Restrained)\
      \ by the hardening rock. A creature can make a DC 15 Strength ([Athletics](Compendium/rules/skills.md#Athletics))\
      \ check as an action, freeing itself or a creature within reach from the rock\
      \ on a success. The rock has AC 17 and 20 hit points, and it is immune to fire,\
      \ poison, and psychic damage."
    "name": "Breath Weapon (Recharge 5-6)"
"source":
  - "MOT"
"image": "Compendium/bestiary/monstrosity/token/underworld-cerberus-mot.webp"
```
^statblock
---
title: Archetype of Imagination
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxvi
- ttrpg-cli/monster/cr/7
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/miscellaneous
statblock: inline
aliases: ["Archetype of Imagination"]
---
# Archetype of Imagination
*Source: Theros Bestiary TBVXVI*  

The archetype of imagination is a human wizard blessed by Ephara. His blessing extends to his allies.

![Archetype of Imagination](Compendium/bestiary/miscellaneous/img/archetype-of-imagination.webp#right)  

```statblock
"name": "Archetype of Imagination (TBVXVI)"
"size": "Medium"
"type": "human"
"alignment": "Any alignment"
"ac": !!int "12"
"hp": !!int "36"
"hit_dice": "9d8 + 0"
"modifier": !!int "2"
"stats":
  - !!int "9"
  - !!int "14"
  - !!int "11"
  - !!int "17"
  - !!int "12"
  - !!int "11"
"speed": "30 ft."
"saves":
  - "intelligence": !!int "6"
  - "wisdom": !!int "4"
"skillsaves":
  - "name": "[Arcana](Compendium/rules/skills.md#Arcana)"
    "desc": "+6"
  - "name": "[History](Compendium/rules/skills.md#History)"
    "desc": "+6"
"senses": "passive Perception 10"
"languages": "Common"
"cr": "7"
"traits":
  - "desc": "Allies of the archetype that it can see within 120 ft. have a flying speed equal to their walking speed or their current flying speed, whichever is greater. As long as the archetype can see any non-allies within 120 ft., their flying speed (if any) is reduced to 0 and cannot increase."
    "name": "Blessing of Ephara"
  - "desc": "The mage is a 9th-level spellcaster. Its spellcasting ability is Intelligence (spell save DC 14, +6 to hit with spell attacks). The mage has the following wizard spells prepared: • Cantrips (at will): fire bolt, light, mage hand, prestidigitation • 1st level (4 slots): detect magic, mage armor, magic missile, shield • 2nd level (3 slots): misty step, suggestion • 3rd level (3 slots): counterspell, fireball, fly • 4th level (3 slots): greater invisibility, ice storm • 5th level (1 slot): cone of cold"
    "name": "Spellcasting"
  - "desc": "The archetype's weapon attacks are magical."
    "name": "Magic Weapons"
  - "desc": "The archetype glows with the soft light of the night sky, shedding dim light in a 15-foot radius."
    "name": "Starlight Form"
"actions":
  - "desc": "Melee or Ranged Weapon Attack: +5 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 4 (1d4 + 2) piercing damage."
    "name": "Dagger"
"source":
  - "TBVXVI"
"image": "Compendium/bestiary/miscellaneous/token/archetype-of-imagination-tbvxvi.webp"
```
^statblock
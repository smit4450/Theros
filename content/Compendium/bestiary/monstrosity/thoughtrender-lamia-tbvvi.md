---
title: Thoughtrender Lamia
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvvi
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Thoughtrender Lamia"]
---
# Thoughtrender Lamia
*Source: Theros Bestiary TBVVI*  

<small><blockquote>Some predators can sense fear in their prey, but the lamia is drawn to madness.</blockquote></small>

![Thoughtrender Lamia](Compendium/bestiary/monstrosity/img/thoughtrender-lamia.webp#right|850)  

```statblock
"name": "Thoughtrender Lamia (TBVVI)"
"size": "Medium"
"type": "monstrosity"
"subtype": "shapechanger"
"alignment": "Chaotic Evil"
"ac": !!int "12"
"ac_class": "natural armor"
"hp": !!int "35"
"hit_dice": "5d8 + 15"
"modifier": !!int "0"
"stats":
  - !!int "15"
  - !!int "10"
  - !!int "16"
  - !!int "11"
  - !!int "11"
  - !!int "20"
"speed": "125 ft."
"skillsaves":
  - "name": "[Persuasion](Compendium/rules/skills.md#Persuasion)"
    "desc": "+7"
  - "name": "[Intimidation](Compendium/rules/skills.md#Intimidation)"
    "desc": "+7"
"condition_immunities": "[blinded](Compendium/rules/conditions.md#Blinded)"
"senses": "[Blindsight](Compendium/rules/senses.md#Blindsight) 30 ft. (can't see beyond this radius), passive Perception 10"
"languages": "Common"
"cr": "4"
"traits":
  - "desc": "The lamia can't use its blindsight while [deafened](Compendium/rules/conditions.md#Deafened) and unable to smell."
    "name": "Blind Senses"
  - "desc": "The lamia has [Advantage](Compendium/rules/variant-rules/advantage-xphb.md) on melee attack rolls against any creature that doesn't have all its [Hit Points](Compendium/rules/variant-rules/hit-points-xphb.md)."
    "name": "Blood Frenzy"
  - "desc": "The lamia has [Advantage](Compendium/rules/variant-rules/advantage-xphb.md) on saving throws against spells and other magical effects."
    "name": "Magic Resistance"
  - "desc": "The lamia's weapon attacks are magical."
    "name": "Magic Weapons"
  - "desc": "On the lamia's turn, if the lamia is within 5 feet of at least one other lamia, each of those lamias may each take a bonus action to expend one spell slot of a creature that lamia can reach."
    "name": "Rend Thoughts"
  - "desc": "The lamia can use its action to change the appearance of its body, arms, legs, or tail to resemble that of a beast it has seen. Its head, neck, chest, and breasts always remain their original form-- a beautiful female human. Its statistics are the same in each form. Any equipment it is wearing or carrying isn't transformed."
    "name": "Shapechanger"
  - "desc": "The lamia glows with the soft light of the night sky, shedding dim light in a 15-foot radius."
    "name": "Starlight Form"
"actions":
  - "desc": "_Melee Weapon Attack:_ +4 to hit, reach 5 ft., one target. _Hit:_ 7 (2d4 + 2) slashing damage and 15 (4d4 + 5) psychic damage."
    "name": "Claws"
"source":
  - "TBVVI"
"image": "Compendium/bestiary/monstrosity/token/thoughtrender-lamia-tbvvi.webp"
```
^statblock
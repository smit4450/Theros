---
title: Marshmist Titan
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvix
- ttrpg-cli/monster/cr/19
- ttrpg-cli/monster/size/g
- ttrpg-cli/monster/type/giant
statblock: inline
aliases: ["Marshmist Titan"]
---
# Marshmist Titan
*Source: Theros Bestiary TBVIX*  

<small><blockquote>A favorite of Erebos, for it has sent many to the Underworld.</blockquote></small>

![Marshmist Titan](Compendium/bestiary/giant/img/marshmist-titan.webp#right|850)  

```statblock
"name": "Marshmist Titan (TBVIX)"
"size": "Gargantuan"
"type": "giant"
"subtype": "titan"
"alignment": "Lawful Evil"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "750"
"hit_dice": "50d20 + 250"
"modifier": !!int "1"
"stats":
  - !!int "18"
  - !!int "12"
  - !!int "21"
  - !!int "12"
  - !!int "14"
  - !!int "16"
"speed": "120 ft."
"saves":
  - "constitution": !!int "11"
  - "wisdom": !!int "8"
"skillsaves":
  - "name": "[Intimidation](Compendium/rules/skills.md#Intimidation)"
    "desc": "+9"
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+8"
"damage_immunities": "necrotic, poison, acid"
"condition_immunities": "frightened, poisoned"
"senses": "darkvision 120 ft., passive Perception 10"
"languages": "Titan"
"cr": "19"
"traits":
  - "desc": "Any creature that starts its turn within 10 feet of the titan must succeed on a DC 18 Constitution saving throw, or it takes 10 (3d6) necrotic damage and can’t regain hit points until the start of its next turn. On a successful saving throw, the creature is immune to the titan's Aura of Erebos for 24 hours."
    "name": "Aura of Erebos"
  - "desc": "The titan has advantage on saving throws against spells and other magical effects."
    "name": "Magic Resistance"
  - "desc": "The titan deals double damage to objects and structures."
    "name": "Siege Monster"
  - "desc": "Unless provoked, the titan ignores all nonflying things that are Huge or smaller and all flying things that are Large or smaller."
    "name": "Titanic Nature"
"actions":
  - "desc": "Melee Weapon Attack: +9 to hit, reach 10 ft., one target. Hit: 40 (8d8 + 4) bludgeoning damage plus 10 (3d6) necrotic damage."
    "name": "Unarmed Strike"
  - "desc": "The titan exhales a mighty gust that creates a blast of deadly mist in a 60-foot line that is 10 feet wide. Each creature in that line must make a DC 18 Constitution saving throw. On a failed save, the creature takes 36 (8d8) necrotic damage and is knocked prone. On a successful save, a creature takes half as much damage and isn’t knocked prone."
    "name": "Noxious Gust (Recharge 5–6)"
"source":
  - "TBVIX"
"image": "Compendium/bestiary/giant/token/marshmist-titan-tbvix.webp"
```
^statblock
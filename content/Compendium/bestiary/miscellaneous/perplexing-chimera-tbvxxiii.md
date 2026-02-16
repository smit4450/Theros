---
title: Perplexing Chimera
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxxiii
- ttrpg-cli/monster/cr/4
- ttrpg-cli/monster/size/h
- ttrpg-cli/monster/type/miscellaneous
statblock: inline
aliases: ["Perplexing Chimera"]
---
# Perplexing Chimera
*Source: Theros Bestiary TBVXXIII*  

The perplexing chimera is a nyxborn creature with no back end, only two front ends. Each end of it has the head of a mastiff, the talons of an eagle, and the mane of a lion. Its heads are in a constant power struggle against one another.

![Perplexing Chimera](Compendium/bestiary/miscellaneous/img/perplexing-chimera.webp#right|850)  

```statblock
"name": "Perplexing Chimera (TBVXXIII)"
"size": "Huge"
"type": "5th-level transmutation aberration"
"alignment": "Unaligned"
"ac": !!int "12"
"hp": !!int "117"
"hit_dice": "13d12 + 39"
"modifier": !!int "1"
"stats":
  - !!int "17"
  - !!int "12"
  - !!int "16"
  - !!int "3"
  - !!int "6"
  - !!int "7"
"speed": "30 ft."
"skillsaves":
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+1"
"senses": "passive Perception 10"
"languages": ""
"cr": "4"
"traits":
  - "desc": "The chimera can't attack the same target two turns in a row or move the same direction two turns in a row."
    "name": "Internal Power Struggle"
  - "desc": "The chimera has [Advantage](Compendium/rules/variant-rules/advantage-xphb.md) on Wisdom (Perception) checks that rely on hearing or smell."
    "name": "Keen Hearing and Smell"
  - "desc": "The chimera's weapon attacks are magical."
    "name": "Magic Weapons"
  - "desc": "In addition to being a creature, the chimera is a 5th-level divine transmutation spell with no target."
    "name": "Spell Nature"
  - "desc": "The chimera glows with the soft light of the night sky, shedding dim light in a 15-foot radius."
    "name": "Starlight Form"
  - "desc": "The chimera has [Advantage](Compendium/rules/variant-rules/advantage-xphb.md) on saving throws against being [blinded](Compendium/rules/conditions.md#Blinded), [charmed](Compendium/rules/conditions.md#Charmed), [deafened](Compendium/rules/conditions.md#Deafened), [frightened](Compendium/rules/conditions.md#Frightened), [stunned](Compendium/rules/conditions.md#Stunned), and knocked [unconscious](Compendium/rules/conditions.md#Unconscious)."
    "name": "Two Heads"
"actions":
  - "desc": "The chimera makes two attacks against a single target: one with its bite and one with its talons."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 12 (2d8 + 3) piercing damage. If the target is a creature, it must succeed on a DC 15 Strength saving throw or be knocked [prone](Compendium/rules/conditions.md#Prone)."
    "name": "Bite"
  - "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 10 (2d6 + 3) slashing damage."
    "name": "Talons"
"source":
  - "TBVXXIII"
"image": "Compendium/bestiary/miscellaneous/token/perplexing-chimera-tbvxxiii.webp"
```
^statblock
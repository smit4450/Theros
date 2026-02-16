---
title: Nessian Asp
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbviv
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Nessian Asp"]
---
# Nessian Asp
*Source: Theros Bestiary TBVIV*  

<small><blockquote>It’s not the two heads you should fear. It’s the four fangs.</blockquote></small>

![Nessian Asp](Compendium/bestiary/beast/img/nessian-asp.webp#right|850)  

```statblock
"name": "Nessian Asp (TBVIV)"
"size": "Medium"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "14"
"hp": !!int "25"
"hit_dice": "5d8 + 5"
"modifier": !!int "4"
"stats":
  - !!int "10"
  - !!int "18"
  - !!int "13"
  - !!int "2"
  - !!int "10"
  - !!int "3"
"speed": "30 ft., climb 30 ft., swim 30 ft."
"skillsaves":
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+2"
"senses": "[Blindsight](Compendium/rules/senses.md#Blindsight) 10 ft., passive Perception 10"
"languages": ""
"cr": "2"
"traits":
  - "desc": "The asp has [Advantage](Compendium/rules/variant-rules/advantage-xphb.md) on Wisdom (Perception) checks and on saving throws against being [blinded](Compendium/rules/conditions.md#Blinded), [charmed](Compendium/rules/conditions.md#Charmed), [deafened](Compendium/rules/conditions.md#Deafened), [frightened](Compendium/rules/conditions.md#Frightened), [stunned](Compendium/rules/conditions.md#Stunned), or knocked [unconscious](Compendium/rules/conditions.md#Unconscious)."
    "name": "Two Heads"
  - "desc": "If the asp is reduced to 0 [Hit Points](Compendium/rules/variant-rules/hit-points-xphb.md), it doesn’t die or fall [unconscious](Compendium/rules/conditions.md#Unconscious). Instead, it sheds its skin, regains 19 (4d8+1) [Hit Points](Compendium/rules/variant-rules/hit-points-xphb.md), and moves up to its speed without provoking opportunity attacks."
    "name": "Shed Skin (Mythic Trait; Recharges after a Short or Long Rest)."
"actions":
  - "desc": "The asp makes two bite attacks on either one or two targets that are within 5 feet of each other."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +2 to hit, reach 10 ft., one target. Hit: 6 (1d4 + 4) piercing damage, and the target must make a DC 11 Constitution saving throw, taking 10 (3d6) poison damage on a failed save, or half as much damage on a successful one."
    "name": "Bite"
"source":
  - "TBVIV"
"image": "Compendium/bestiary/beast/token/nessian-asp-tbviv.webp"
```
^statblock
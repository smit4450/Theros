---
title: Ravenous Leucrocota
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbviv
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/size/l
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Ravenous Leucrocota"]
---
# Ravenous Leucrocota
*Source: Theros Bestiary TBVIV*  

<blockquote><small>Hunger makes a leucrocota dangerous. A full belly makes it angry and dangerous.</small></blockquote>

![Ravenous Leucrocota](Compendium/bestiary/monstrosity/img/ravenous-leucrocota.webp#right)  

```statblock
"name": "Ravenous Leucrocota (TBVIV)"
"size": "Large"
"type": "monstrosity"
"alignment": "Chaotic Evil"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "36"
"hit_dice": "4d10 + 16"
"modifier": !!int "2"
"stats":
  - !!int "15"
  - !!int "14"
  - !!int "18"
  - !!int "9"
  - !!int "12"
  - !!int "6"
"speed": "50 ft."
"skillsaves":
  - "name": "[Deception](Compendium/rules/skills.md#Deception)"
    "desc": "+0"
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+3"
"senses": "darkvision 60 ft., passive Perception 10"
"languages": ""
"cr": "3"
"traits":
  - "desc": "The leucrocota has advantage on Wisdom (perception) checks that rely on smell."
    "name": "Keen Smell"
  - "desc": "If the leucrocota attacks with its hooves, it can take the Disengage action as a bonus action."
    "name": "Kicking Retreat"
  - "desc": "The leucrocota can mimic animal sounds and humanoid voices. A creature that hears the sounds can tell they are imitations with a successful DC 14 Wisdom (Insight) check."
    "name": "Mimicry"
  - "desc": "When the leucrocota reduces a creature to 0 hit points with a melee attack on its turn, it can take a bonus action to move up to half its speed and make an attack with its hooves."
    "name": "Rampage"
  - "desc": "The leucrocota can't be surprised."
    "name": "Vigilant"
"actions":
  - "desc": "The leucrocota makes two attacks: one with its bite and one with its hooves."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) piercing damage. If the leucrocota scores a critical hit, it rolls the damage dice three times, instead of twice."
    "name": "Bite"
  - "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 9 (2d6 + 2) bludgeoning damage."
    "name": "Hooves"
  - "desc": "The leucrocota devours a corpse it can reach. It gets a +3 bonus to Strength and Dexterity checks and damage rolls, and gains 16 (3d10) temporary hit points. This effect ends when the leucrocota completes a Short or Long Rest."
    "name": "Eat Corpse (Mythic Trait; Recharges After a Short or Long Rest)"
"source":
  - "TBVIV"
"image": "Compendium/bestiary/monstrosity/token/ravenous-leucrocota-tbviv.webp"
```
^statblock
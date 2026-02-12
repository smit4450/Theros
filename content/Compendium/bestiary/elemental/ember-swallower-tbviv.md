---
title: Ember Swallower
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbviv
- ttrpg-cli/monster/cr/6
- ttrpg-cli/monster/size/l
- ttrpg-cli/monster/type/elemental
statblock: inline
aliases: ["Ember Swallower"]
---
# Ember Swallower
*Source: Theros Bestiary TBVIV*  

A molten rock elemental in the shape of a manticore poses a serious threat.

![Ember Swallower](Compendium/bestiary/elemental/img/ember-swallower.webp#right|850)  

```statblock
"name": "Ember Swallower (TBVIV)"
"size": "Large"
"type": "elemental"
"alignment": "Lawful Evil"
"ac": !!int "14"
"hp": !!int "64"
"hit_dice": "8d10 + 24"
"modifier": !!int "3"
"stats":
  - !!int "17"
  - !!int "16"
  - !!int "17"
  - !!int "7"
  - !!int "12"
  - !!int "10"
"speed": "30 ft."
"damage_resistances": "bludgeoning, piercing, and slashing from nonmagical attacks"
"damage_immunities": "fire"
"senses": "darkvision 60 ft., passive Perception 10"
"languages": ""
"cr": "6"
"traits":
  - "desc": "At the start of each of the ember swallower's turns, each creature within 5 feet of it takes 10 (3d6) fire damage, and flammable objects in the aura that aren't being worn or carried ignite. A creature that touches the ember swallower or hits it with a melee attack while within 5 feet of it takes 10 (3d6) fire damage."
    "name": "Fire Aura"
  - "desc": "For every 5 feet the ember swallower moves in water, or for every gallon of water splashed on it, it takes 1 cold damage."
    "name": "Water Susceptibility"
  - "desc": "When the ember swallower is reduced to 0 hit points, it doesn’t die or fall unconscious. Instead, the damage creates cracks in its carapace, revealing its hearts. The ember swallower has three hearts in its chest. A heart has an AC of 14 and 20 hit points. It is immune to bludgeoning, piercing, and slashing damage from nonmagical attacks and to fire, and it is immune to all conditions. If it is forced to make a saving throw, treat its ability scores as 10 (+0). If it finishes a short or long rest, the carapace heals, any destroyed hearts regenerate, and the hearts are covered again. The ember swallower dies when all the hearts are destroyed."
    "name": "Hearts of the Beast (Mythic Trait; Recharges after a Short or Long Rest)"
"actions":
  - "desc": "The ember swallower makes four attacks: one with its bite, one with its sting, and two with its claws."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) piercing damage and 10 (2d6 +3) fire damage."
    "name": "Bite"
  - "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) slashing damage and 10 (2d6 +3) fire damage."
    "name": "Claw"
  - "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one creature. Hit: 8 (1d10 + 3) piercing damage, and the target must make a DC 12 Constitution saving throw, taking 22 (4d10) fire damage on a failed save, or half as much damage on a successful one."
    "name": "Sting"
"legendary_actions":
  - "desc": "**Mythic Actions**If Tromokratis’s mythic trait is active, it can use the options below as legendary actions for 1 hour after using Hearts of the Beast. **_Erupt._** The ember swallower dies erupts fire and magma. Each creature within 10 feet of it must make a DC 11 Dexterity saving throw, taking 7 (2d6) fire damage on a failed save, or half as much damage on a successful one. Flammable objects that aren't being worn or carried in that area are ignited."
    "name": ""
"source":
  - "TBVIV"
"image": "Compendium/bestiary/elemental/token/ember-swallower-tbviv.webp"
```
^statblock
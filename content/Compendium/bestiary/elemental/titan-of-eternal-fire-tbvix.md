---
title: Titan of Eternal Fire
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvix
- ttrpg-cli/monster/cr/27
- ttrpg-cli/monster/size/g
- ttrpg-cli/monster/type/elemental
statblock: inline
aliases: ["Titan of Eternal Fire"]
---
# Titan of Eternal Fire
*Source: Theros Bestiary TBVIX*  

<blockquote><small>There is no gift more precious or more perilous than fire.</small></blockquote>
<b><big>Usage Notes</big></b>
A DM using this creature should keep in mind that this creature is capable of a total party kill with a single attack. This boss should only be given to a experienced players with high-level characters, and only in carefully planed environments that allow the players to gain some sort of upper hand. Perhaps the players have siege weapons at their discretion, or have befriended a titan that aids them. Or perhaps the titan is trapped in a chasm that it can't scale.

![Titan of Eternal Fire](Compendium/bestiary/elemental/img/titan-of-eternal-fire.webp#right)  

```statblock
"name": "Titan of Eternal Fire (TBVIX)"
"size": "Gargantuan"
"type": "elemental"
"subtype": "titan"
"alignment": "Lawful Evil"
"ac": !!int "14"
"hp": !!int "960"
"hit_dice": "60d20 + 360"
"modifier": !!int "2"
"stats":
  - !!int "20"
  - !!int "15"
  - !!int "22"
  - !!int "7"
  - !!int "12"
  - !!int "20"
"speed": "120 ft."
"damage_resistances": "bludgeoning, piercing, and slashing from nonmagical attacks"
"damage_immunities": "fire"
"senses": "darkvision 60 ft., passive Perception 10"
"languages": "Titan"
"cr": "27"
"traits":
  - "desc": "When the titan dies, it explodes in a burst of fire and rock. Each creature within 10 feet of it must make a DC 21 Dexterity saving throw, taking 7 (2d6) fire damage on a failed save, or half as much damage on a successful one. Flammable objects that aren't being worn or carried in that area are ignited."
    "name": "Death Burst"
  - "desc": "At the start of each of the titan's turns, each creature within 5 feet of it takes 10 (3d6) fire damage, and flammable objects in the aura that aren't being worn or carried ignite. A creature that touches the titan or hits it with a melee attack while within 5 feet of it takes 10 (3d6) fire damage."
    "name": "Fire Aura"
  - "desc": "The titan deals double damage to objects and structures."
    "name": "Siege Monster"
  - "desc": "The titan has advantage on Dexterity (Stealth) checks made to hide in rocky terrain."
    "name": "Stone Camouflage"
  - "desc": "Unless provoked, the giant ignores all nonflying things that are Huge or smaller and all flying things that are Large or smaller."
    "name": "Titanic Nature"
  - "desc": "For every 5 feet the titan moves in water, or for every gallon of water splashed on it, it takes 1 cold damage."
    "name": "Water Susceptibility"
"actions":
  - "desc": "_Ranged Spell Attack:_ spell save DC 21, +13 to hit with spell attacks, range 100 ft. The titan pulls a fireball from its chest and throws it at a point within range. Each creature in a 20-foot-radius sphere centered on that point must make a DC 21 Dexterity saving throw. A target takes 49 (14d6) fire damage on a failed save, or half as much damage on a successful one. The fire spreads around corners. It ignites flammable objects in the area that aren’t being worn or carried."
    "name": "Fireball"
"source":
  - "TBVIX"
"image": "Compendium/bestiary/elemental/token/titan-of-eternal-fire-tbvix.webp"
```
^statblock
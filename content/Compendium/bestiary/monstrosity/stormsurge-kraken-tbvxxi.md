---
title: Stormsurge Kraken
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxxi
- ttrpg-cli/monster/cr/28
- ttrpg-cli/monster/size/g
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Stormsurge Kraken"]
---
# Stormsurge Kraken
*Source: Theros Bestiary TBVXXI*  

<small><blockquote>Most see krakens as wantonly violent, failing to notice their meticulous attention to detail when dismantling a vessel.</blockquote></small>
A well-disciplined summoner of sea monsters can summon a stormsurge kraken as a powerful ally in naval combat if they possess the proper telepathic skills.

![Stormsurge Kraken](https://img.scryfall.com/cards/art_crop/front/e/d/ed1c1121-593d-4780-a1d0-5fbd2c09a9f2.jpg?1561963771#right)  

```statblock
"name": "Stormsurge Kraken (TBVXXI)"
"size": "Gargantuan"
"type": "monstrosity"
"alignment": "Lawful Evil"
"ac": !!int "18"
"ac_class": "natural armor"
"hp": !!int "750"
"hit_dice": "50d20 + 250"
"modifier": !!int "0"
"stats":
  - !!int "21"
  - !!int "11"
  - !!int "21"
  - !!int "22"
  - !!int "18"
  - !!int "20"
"speed": "20 ft., swim 60 ft."
"saves":
  - "strength": !!int "13"
  - "dexterity": !!int "8"
  - "constitution": !!int "13"
  - "intelligence": !!int "14"
  - "wisdom": !!int "12"
"damage_immunities": "lightning, bludgeoning, piercing, and slashing from nonmagical attacks"
"condition_immunities": "[frightened](Compendium/rules/conditions.md#Frightened), [paralyzed](Compendium/rules/conditions.md#Paralyzed)"
"senses": "[Truesight](Compendium/rules/senses.md#Truesight) 120 ft., passive Perception 10"
"languages": "understands Abyssal, Celestial, Infernal, and Primordial but can't speak, telepathy 120 ft."
"cr": "28"
"traits":
  - "desc": "The kraken can breathe air and water."
    "name": "Amphibious"
  - "desc": "The kraken ignores difficult terrain, and magical effects can't reduce its speed or cause it to be [restrained](Compendium/rules/conditions.md#Restrained). It can spend 5 feet of movement to escape from nonmagical restraints or being [grappled](Compendium/rules/conditions.md#Grappled)."
    "name": "Freedom of Movement"
  - "desc": "The kraken can't be affected or detected by spells of 6th level or lower unless it wishes to be. It has [Advantage](Compendium/rules/variant-rules/advantage-xphb.md) on saving throws against all other spells and magical effects."
    "name": "Limited Magic Immunity"
  - "desc": "The kraken deals double damage to objects and structures."
    "name": "Siege Monster"
  - "desc": "As long as the kraken maintains a telepathic bond with a master, the kraken gets a +2 bonus on Strength and Dexterity checks, and its [Hit Points](Compendium/rules/variant-rules/hit-points-xphb.md) and maximum [Hit Points](Compendium/rules/variant-rules/hit-points-xphb.md) increase by 210 (20d20) until that bond is broken."
    "name": "Willing Servant"
"actions":
  - "desc": "The kraken makes three tentacle attacks, each of which it can replace with one use of Fling."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +21 to hit or +23 to hit if following a command, reach 5 ft., one target. Hit: 50 (10d8 + 5) piercing damage or 70 (14d8 + 7) piercing damage if following a command. If the target is a Large or smaller creature [grappled](Compendium/rules/conditions.md#Grappled) by the kraken, that creature is swallowed, and the grapple ends. While swallowed, the creature is [blinded](Compendium/rules/conditions.md#Blinded) and [restrained](Compendium/rules/conditions.md#Restrained), it has total cover against attacks and other effects outside the kraken, and it takes 42 (12d6) acid damage at the start of each of the kraken's turns. If the kraken takes 50 damage or more on a single turn from a creature inside it, the kraken must succeed on a DC 15 Constitution saving throw at the end of that turn, or regurgitate all swallowed creatures, which fall [prone](Compendium/rules/conditions.md#Prone) in a space within 10 feet of the kraken. If the kraken dies, a swallowed creature is no longer [restrained](Compendium/rules/conditions.md#Restrained) by it and can escape from the corpse using 15 feet of movement, exiting [prone](Compendium/rules/conditions.md#Prone)."
    "name": "Bite"
  - "desc": "Melee Weapon Attack: +21 to hit or +23 to hit if following a command, reach 30 ft., one target. Hit: 40 (10d6 + 5) bludgeoning damage or 56 (14d6 + 7) bludgeoning damage if following a command, and the target is [grappled](Compendium/rules/conditions.md#Grappled) (escape DC 15). Until this grapple ends, the target is [restrained](Compendium/rules/conditions.md#Restrained). The kraken has ten tentacles, each of which can grapple one target."
    "name": "Tentacle"
  - "desc": "One Large or smaller object held or creature [grappled](Compendium/rules/conditions.md#Grappled) by the kraken is thrown up to 60 feet in a random direction and knocked [prone](Compendium/rules/conditions.md#Prone). If a thrown target strikes a solid surface, the target takes 3 (1d6) bludgeoning damage for every 10 feet it was thrown. If the target is thrown at another creature, that creature must succeed on a DC 16 Dexterity saving throw or take the same damage and be knocked [prone](Compendium/rules/conditions.md#Prone)."
    "name": "Fling"
  - "desc": "The kraken magically creates three bolts of lightning, each of which can strike a target the kraken can see within 120 feet of it. A target must make a DC 23 Dexterity saving throw, taking 22 (4d10) lightning damage on a failed save, or half as much damage on a successful one."
    "name": "Lightning Storm"
"source":
  - "TBVXXI"
"image": "Compendium/bestiary/monstrosity/token/stormsurge-kraken-tbvxxi.webp"
```
^statblock
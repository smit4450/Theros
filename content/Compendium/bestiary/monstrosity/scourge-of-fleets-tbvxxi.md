---
title: Scourge of Fleets
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxxi
- ttrpg-cli/monster/cr/21
- ttrpg-cli/monster/size/g
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Scourge of Fleets"]
---
# Scourge of Fleets
*Source: Theros Bestiary TBVXXI*  



![Scourge of Fleets](Compendium/bestiary/monstrosity/img/scourge-of-fleets.webp#right|850)  

```statblock
"name": "Scourge of Fleets (TBVXXI)"
"size": "Gargantuan"
"type": "monstrosity"
"subtype": "kraken"
"alignment": "Chaotic Evil"
"ac": !!int "20"
"ac_class": "natural armor"
"hp": !!int "960"
"hit_dice": "60d20 + 360"
"modifier": !!int "1"
"stats":
  - !!int "22"
  - !!int "12"
  - !!int "22"
  - !!int "1"
  - !!int "9"
  - !!int "17"
"speed": "40 ft., swim 120 ft."
"damage_immunities": "bludgeoning, piercing, and slashing from nonmagical attacks"
"condition_immunities": "[[conditions#Frightened|frightened]], [[conditions#Paralyzed|paralyzed]]"
"senses": "passive Perception 10"
"languages": ""
"cr": "21"
"traits":
  - "desc": "The kraken can breathe air and water."
    "name": "Amphibious"
  - "desc": "If the kraken breaches the surface, it creates a massive wave that pushes all Huge and smaller floating objects, structures, and creatures within a 500-foot radius 100 feet away from the kraken. If the kraken makes a bite attack as it breaches, targets it bites aren't affected by the forceful breach."
    "name": "Forceful Breach"
  - "desc": "The kraken deals double damage to objects and structures."
    "name": "Siege Monster"
"actions":
  - "desc": "The kraken makes two arm attacks, each of which it can replace with one use of Fling."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +13 to hit, reach 5 ft., one target. Hit: 60 (12d8 + 6) piercing damage. If the target is a Large or smaller creature [[conditions#Grappled|grappled]] by the kraken, that creature is swallowed, and the grapple ends. While swallowed, the creature is [[conditions#Blinded|blinded]] and [[conditions#Restrained|restrained]], it has total cover against attacks and other effects outside the kraken, and it takes 42 (12d6) acid damage at the start of each of the kraken's turns. If the kraken takes 50 damage or more on a single turn from a creature inside it, the kraken must succeed on a DC 21 Constitution saving throw at the end of that turn or regurgitate all swallowed creatures, which fall [[conditions#Prone|prone]] in a space within 10 feet of the kraken. If the kraken dies, a swallowed creature is no longer [[conditions#Restrained|restrained]] by it and can escape from the corpse using 15 feet of movement, exiting [[conditions#Prone|prone]]."
    "name": "Bite"
  - "desc": "Melee Weapon Attack: +13 to hit, reach 10 ft., one target. Hit: 27 (6d6 + 6) bludgeoning damage, and the target is [[conditions#Grappled|grappled]] (escape DC 15). The kraken has two arms. Until this grapple ends, the target is [[conditions#Restrained|restrained]] and the kraken cannot make attacks with that arm."
    "name": "Arm"
  - "desc": "One Large or smaller object held or creature [[conditions#Grappled|grappled]] by the kraken's arm is thrown up to 60 feet in a random direction and knocked [[conditions#Prone|prone]]. If a thrown target strikes a solid surface, the target takes 3 (1d6) bludgeoning damage for every 10 feet it was thrown. If the target is thrown at another creature, that creature must succeed on a DC 16 Dexterity saving throw or take the same damage and be knocked [[conditions#Prone|prone]]."
    "name": "Fling"
"source":
  - "TBVXXI"
"image": "Compendium/bestiary/monstrosity/token/scourge-of-fleets-tbvxxi.webp"
```
^statblock
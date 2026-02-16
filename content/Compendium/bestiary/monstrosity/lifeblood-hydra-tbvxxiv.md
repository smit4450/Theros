---
title: Lifeblood Hydra
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxxiv
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/size/h
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Lifeblood Hydra"]
---
# Lifeblood Hydra
*Source: Theros Bestiary TBVXXIV*  

<small><blockquote>Pharika has written her secrets on its bones so that only the worthy may discover them.</blockquote></small>

![Lifeblood Hydra](https://img.scryfall.com/cards/art_crop/front/5/5/5514bc19-5b1b-420b-ab43-fde15a4ee446.jpg?1561942723#right)  

```statblock
"name": "Lifeblood Hydra (TBVXXIV)"
"size": "Huge"
"type": "monstrosity"
"alignment": "Unaligned"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "55"
"hit_dice": "5d12 + 25"
"modifier": !!int "1"
"stats":
  - !!int "21"
  - !!int "12"
  - !!int "21"
  - !!int "2"
  - !!int "10"
  - !!int "7"
"speed": "30 ft., swim 30 ft."
"skillsaves":
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+6"
"senses": "[Darkvision](Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception 10"
"languages": ""
"cr": "5"
"traits":
  - "desc": "When the hydra takes piercing or slashing damage, each creature within 5 feet of it regains 9 (2d8) [Hit Points](Compendium/rules/variant-rules/hit-points-xphb.md)."
    "name": "Healing Blood"
  - "desc": "The hydra can hold its breath for 1 hour."
    "name": "Hold Breath"
  - "desc": "The hydra has five heads. While it has more than one head, the hydra has [Advantage](Compendium/rules/variant-rules/advantage-xphb.md) on saving throws against being [blinded](Compendium/rules/conditions.md#Blinded), [charmed](Compendium/rules/conditions.md#Charmed), [deafened](Compendium/rules/conditions.md#Deafened), [frightened](Compendium/rules/conditions.md#Frightened), [stunned](Compendium/rules/conditions.md#Stunned), and knocked [unconscious](Compendium/rules/conditions.md#Unconscious). Whenever the hydra takes 11 or more damage in a single turn, one of its heads dies. If all its heads die, the hydra dies. At the end of its turn, it grows two heads for each of its heads that died since its last turn, unless it has taken fire damage since its last turn. The hydra regains 11 [Hit Points](Compendium/rules/variant-rules/hit-points-xphb.md) for each head regrown in this way."
    "name": "Multiple Heads"
  - "desc": "For each head the hydra has beyond one, it gets an extra reaction that can be used only for opportunity attacks."
    "name": "Reactive Heads"
  - "desc": "The hydra can move in and out of a Medium or smaller creature's space. If it would, it uses a bonus action to attack that creature with its stomp attack. That creature must succeed on a DC 16 Strength saving throw or be knocked [prone](Compendium/rules/conditions.md#Prone). If the creature succeeds, the hydra can't enter that space and must end its turn immediately. If the hydra stops on top of that creature, that creature becomes [restrained](Compendium/rules/conditions.md#Restrained) until the hydra moves off it (escape DC 16)."
    "name": "Trample"
  - "desc": "While the hydra sleeps, at least one of its heads is awake."
    "name": "Wakeful"
"actions":
  - "desc": "The hydra makes as many bite attacks as it has heads."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 10 (1d10 + 5) piercing damage."
    "name": "Bite"
  - "desc": "_Melee Weapon Attack:_ +8 to hit, reach 5 ft., one target. _Hit:_ 7 (1d4 + 5) bludgeoning damage."
    "name": "Stomp"
"source":
  - "TBVXXIV"
"image": "Compendium/bestiary/monstrosity/token/lifeblood-hydra-tbvxxiv.webp"
```
^statblock
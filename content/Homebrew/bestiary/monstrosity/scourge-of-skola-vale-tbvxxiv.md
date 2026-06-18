---
title: Scourge of Skola Vale
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvxxiv
- monster/cr/3
- monster/size/h
- monster/type/monstrosity
statblock: inline
aliases: ["Scourge of Skola Vale"]
---
# Scourge of Skola Vale
*Source: Theros Bestiary TBVXXIV*  



![Scourge of Skola Vale](Homebrew/bestiary/monstrosity/img/scourge-of-skola-vale.webp#right)  

```statblock
"name": "Scourge of Skola Vale (TBVXXIV)"
"size": "Huge"
"type": "monstrosity"
"alignment": "Unaligned"
"ac": !!int "15"
"hp": !!int "55"
"hit_dice": "5d12 + 25"
"modifier": !!int "1"
"stats":
  - !!int "20"
  - !!int "12"
  - !!int "20"
  - !!int "2"
  - !!int "10"
  - !!int "7"
"speed": "30 ft., swim 30 ft."
"skillsaves":
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+6"
"senses": "[[senses#Darkvision|Darkvision]] 60 ft., passive Perception 10"
"languages": ""
"cr": "3"
"traits":
  - "desc": "The hydra can hold its breath for 1 hour."
    "name": "Hold Breath"
  - "desc": "The hydra has two heads. While it has more than one head, the hydra has [[advantage-xphb|Advantage]] on saving throws against being [[conditions#Blinded|blinded]], [[conditions#Charmed|charmed]], [[conditions#Deafened|deafened]], [[conditions#Frightened|frightened]], [[conditions#Stunned|stunned]], and knocked [[conditions#Unconscious|unconscious]]. Whenever the hydra takes 25 or more damage in a single turn, one of its heads dies. If all its heads die, the hydra dies. At the end of its turn, it grows two heads for each of its heads that died since its last turn, unless it has taken fire damage since its last turn. The hydra regains 10 [[hit-points-xphb|Hit Points]] for each head regrown in this way."
    "name": "Multiple Heads"
  - "desc": "For each head the hydra has beyond one, it gets an extra reaction that can be used only for opportunity attacks."
    "name": "Reactive Heads"
  - "desc": "While the hydra sleeps, at least one of its heads is awake."
    "name": "Wakeful"
  - "desc": "The hydra can move in and out of a Medium or smaller creature's space. If it would, it uses a bonus action to attack that creature with its stomp attack. That creature must succeed on a DC 15 Strength saving throw or be knocked [[conditions#Prone|prone]]. If the creature succeeds, the hydra can't enter that space and must end its turn immediately. If the hydra stops on top of that creature, that creature becomes [[conditions#Restrained|restrained]] until the hydra moves off it (escape DC 15)."
    "name": "Trample"
"actions":
  - "desc": "The hydra makes as many bite attacks as it has heads."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 10 (1d10 + 5) piercing damage."
    "name": "Bite"
  - "desc": "The hydra eats a corpse and deals 25 piercing damage to itself."
    "name": "Eat"
  - "desc": "_Melee Weapon Attack:_ +7 to hit, reach 5 ft., one target. _Hit:_ 7 (1d4 + 5) bludgeoning damage."
    "name": "Stomp"
"source":
  - "TBVXXIV"
"image": "Homebrew/bestiary/monstrosity/token/scourge-of-skola-vale-tbvxxiv.webp"
```
^statblock
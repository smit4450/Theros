---
title: Sedge Scorpion
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvxvii
- monster/cr/0
- monster/size/t
- monster/type/beast
statblock: inline
aliases: ["Sedge Scorpion"]
---
# Sedge Scorpion
*Source: Theros Bestiary TBVXVII*  

<blockquote><small>Thakolides the Mighty
Slayer of minotaurs
Vanquisher of giants
Killed by a scorpion

—Inscription on an Akroan grave</small></blockquote>

![Sedge Scorpion](Homebrew/bestiary/beast/img/sedge-scorpion.webp#right)  

```statblock
"name": "Sedge Scorpion (TBVXVII)"
"size": "Tiny"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "11"
"hp": !!int "1"
"hit_dice": "1d4 + -1"
"modifier": !!int "0"
"stats":
  - !!int "2"
  - !!int "11"
  - !!int "8"
  - !!int "1"
  - !!int "8"
  - !!int "2"
"speed": "10 ft."
"senses": "[[senses#Blindsight|Blindsight]] 10 ft., passive Perception 10"
"languages": ""
"cr": "0"
"traits":
  - "desc": "A creature [[conditions#Poisoned|poisoned]] by the scorpion takes 2 (1d4) poison damage each hour until cured of poison."
    "name": "Scorpion Venom"
  - "desc": "If a creature below its race's maturity age or having a Constitution modifier of +1 or less becomes [[conditions#Poisoned|poisoned]] by the scorpion, roll a d10. On a 9 or less, the creature becomes diseased with acute pancreatitis for 5 (1d10) days or until cured of the disease. A creature with this disease must make a DC 11 Constitution saving throw every 24 hours; on a failed save, the it takes 1 acid damage."
    "name": "Dangerous to the Weak"
"actions":
  - "desc": "Melee Weapon Attack: +2 to hit, reach 5 ft., one creature. Hit: 1 piercing damage, and the target must succeed on a DC 20 Constitution saving throw or take 4 (1d8) poison damage and becomes [[conditions#Poisoned|poisoned]]. If a target [[conditions#Poisoned|poisoned]] this way is not diseased, that target remains [[conditions#Poisoned|poisoned]] for no more than 8 hours; otherwise it remains [[conditions#Poisoned|poisoned]] until cured of poison."
    "name": "Sting"
"source":
  - "TBVXVII"
"image": "Homebrew/bestiary/beast/token/sedge-scorpion-tbvxvii.webp"
```
^statblock
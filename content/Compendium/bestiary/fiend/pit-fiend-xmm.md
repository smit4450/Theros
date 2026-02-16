---
title: Pit Fiend
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/20
- ttrpg-cli/monster/environment/nine-hells
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/fiend/devil
statblock: inline
aliases: ["Pit Fiend"]
---
# Pit Fiend
*Source: Monster Manual (2024) p. 243. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/fiend/img/pit-fiend.webp#right|850)  
## Pit Fiend

*Devil of Domination*

- **Habitat.** Planar (Nine Hells)  
- **Treasure.** [[random-magic-items-relics|Relics]]  

Masterminds of the Nine Hells and generals of infernal legions, pit fiends seek conquests across the planes of existence. More than warmongers, these diabolical tyrants concoct intricate plots that play out among fiendish battlefields, infernal politics, and mortal conspiracies.

Pit fiends are the nobility of the Nine Hells, and many rule Lower Planar fiefdoms, doomed mortal worlds, and other infernal redoubts. Most serve archdevils of the Nine Hells as they pursue their own ambitions. Ranks of lesser devils obey pit fiends, but these cunning tyrants remain on guard against betrayal from their servants.

Smoldering with the evil of the Nine Hells, pit fiends strike fear in creatures with their mere presence. Despite their size and incredible physical and magical might, pit fiends are as likely to try to corrupt foes as they are to destroy them outright. Pit fiends' arrogance can lead them to underestimate mortal foes—a failing that can lead to their downfall.
```statblock
"name": "Pit Fiend (XMM)"
"size": "Large"
"type": "fiend"
"subtype": "devil"
"alignment": "Lawful Evil"
"ac": !!int "21"
"hp": !!int "337"
"hit_dice": "27d10 + 189"
"modifier": !!int "14"
"stats":
  - !!int "26"
  - !!int "14"
  - !!int "24"
  - !!int "22"
  - !!int "18"
  - !!int "24"
"speed": "30 ft., fly 60 ft."
"saves":
  - "dexterity": !!int "8"
  - "wisdom": !!int "10"
"skillsaves":
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+10"
  - "name": "[[skills#Persuasion|Persuasion]]"
    "desc": "+19"
"damage_resistances": "cold"
"damage_immunities": "fire, poison"
"condition_immunities": "[[conditions#Poisoned|poisoned]]"
"senses": "[[senses#Truesight|Truesight]] 120 ft., passive Perception\
  \ 20"
"languages": "Infernal; telepathy 120 ft."
"cr": "20"
"traits":
  - "desc": "If the pit fiend dies outside the Nine Hells, its body disappears in\
      \ sulfurous smoke, and it gains a new body instantly, reviving with all its\
      \ [[hit-points-xphb|Hit Points]] somewhere\
      \ in the Nine Hells."
    "name": "Diabolical Restoration"
  - "desc": "The pit fiend emanates an aura in a 20-foot [[emanation-area-of-effect-xphb|Emanation]]\
      \ while it doesn't have the [[conditions#Incapacitated|Incapacitated]]\
      \ condition. *Wisdom Saving Throw:* DC 21, any enemy that starts its turn in\
      \ the aura. *Failure:* The target has the [[conditions#Frightened|Frightened]]\
      \ condition until the start of its next turn. *Success:* The target is immune\
      \ to this pit fiend's aura for 24 hours."
    "name": "Fear Aura"
  - "desc": "If the pit fiend fails a saving throw, it can choose to succeed instead."
    "name": "Legendary Resistance (4/Day)"
  - "desc": "The pit fiend has [[advantage-xphb|Advantage]]\
      \ on saving throws against spells and other magical effects."
    "name": "Magic Resistance"
"actions":
  - "desc": "The pit fiend makes one Bite attack, two Devilish Claw attacks, and one\
      \ Fiery Mace attack."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +14, reach 10 ft. *Hit:* 18 (3d6 + 8) Piercing\
      \ damage. If the target is a creature, it must make the following saving throw.\
      \ *Constitution Saving Throw:* DC 21. *Failure:* The target has the [[conditions#Poisoned|Poisoned]]\
      \ condition. While [[conditions#Poisoned|Poisoned]], the\
      \ target can't regain [[hit-points-xphb|Hit Points]]\
      \ and takes 21 (6d6) Poison damage at the start of each of its turns, and\
      \ it repeats the save at the end of each of its turns, ending the effect on\
      \ itself on a success. After 1 minute, it succeeds automatically."
    "name": "Bite"
  - "desc": "*Melee Attack Roll:* +14, reach 10 ft. *Hit:* 26 (4d8 + 8) Necrotic\
      \ damage."
    "name": "Devilish Claw"
  - "desc": "*Melee Attack Roll:* +14, reach 10 ft. *Hit:* 22 (4d6 + 8) Force\
      \ damage plus 21 (6d6) Fire damage."
    "name": "Fiery Mace"
  - "desc": "The pit fiend casts [[fireball-xphb|Fireball]] (level\
      \ 5 version) twice, requiring no Material components and using Charisma as the\
      \ spellcasting ability (spell save DC 21). It can replace one [[fireball-xphb|Fireball]]\
      \ with [[hold-monster-xphb|Hold Monster]] (level 7 version)\
      \ or [[wall-of-fire-xphb|Wall of Fire]].\n"
    "name": "Hellfire Spellcasting (Recharge 4-6)"
"source":
  - "XMM"
"image": "Compendium/bestiary/fiend/token/pit-fiend-xmm.webp"
```
^statblock
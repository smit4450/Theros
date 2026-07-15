---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/tbvxi
- monster/cr/5
- monster/size/medium
- monster/type/humanoid/minotaur
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Felhide Petrifier"
---
# Felhide Petrifier
*Source: Theros Bestiary, Vol. XI*
![](/Compendium/bestiary/humanoid/img/felhide-petrifier.webp#right)

It’s common practice among minotaurs to collect the heads of their victims as trophies. Sometimes the trophies prove more than ornamental.

```statblock
"name": "Felhide Petrifier"
"size": "Medium"
"type": "humanoid"
"subtype": "minotaur"
"alignment": "Chaotic Evil"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "21"
"hit_dice": "3d8 + 9"
"modifier": !!int "2"
"stats":
  - !!int "15"
  - !!int "14"
  - !!int "16"
  - !!int "10"
  - !!int "12"
  - !!int "10"
"speed": "30 ft."
"saves":
  - "constitution": !!int "6"
"skillsaves":
  - "name": "[Athletics](/Compendium/rules/skills.md#Athletics)"
    "desc": "+5"
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+4"
  - "name": "[Survival](/Compendium/rules/skills.md#Survival)"
    "desc": "+4"
  - "name": "[Persuasion](/Compendium/rules/skills.md#Persuasion)"
    "desc": "+3"
"senses": "passive Perception 10"
"languages": "Common, Minotaur, any one language"
"cr": "5"
"traits":
  - "desc": "The minotaur has Advantage on initiative rolls."
    "name": "Battle Readiness"
  - "desc": "As soon as a creature within 30 feet of the head (including anyone wielding\
      \ it) sees the head, it may make a DC 14 Constitution saving throw. On a success,\
      \ that creature may use a reaction to shield its eyes or avert them. If the\
      \ saving throw fails by 5 or more, or if the creature is unable to react, the\
      \ creature is instantly petrified. Otherwise, a creature that fails the save\
      \ begins to turn to stone and is restrained. The restrained creature must repeat\
      \ the saving throw at the end of its next turn, becoming petrified on a failure\
      \ or ending the effect on a success. The petrification lasts until the creature\
      \ is unpetrified by a god.This trait has no effect if the head's face is not\
      \ its normal flesh state."
    "name": "Gorgon's Head (Weapon)"
  - "desc": "Immediately after the minotaur uses the Dash action on its turn and moves\
      \ at least 20 feet, it can make one melee attack with its horns as a bonus action."
    "name": "Goring Rush"
  - "desc": "The minotaur's attack rolls score a critical hit on a roll of 19 or 20\
      \ on the d20."
    "name": "Improved Critical"
  - "desc": "As long as it is holding the head of a gorgon, allies of the minotaur\
      \ that it can see within 120 ft. can use a bonus action on their turn to do\
      \ the following:**_Diversion._** The allied creature points, cocks its head,\
      \ or some other gesture to try to get other creatures to look away and look\
      \ instead at the gorgon's head. Each creature that can see the ally must succeed\
      \ on a DC 15 Wisdom saving throw or try to look in the direction of the head."
    "name": "Provide Diversion"
"actions":
  - "desc": "The minotaur makes two attacks."
    "name": "Multiattack"
  - "desc": "_Melee Weapon Attack:_ +7 to hit, reach 5 ft., one target. _Hit:_ 5 (1d6\
      \ + 2) piercing damage, and the minotaur can use a bonus action to attempt to\
      \ shove that target with its horns. The target must be within 5 feet of the\
      \ minotaur and no more than one size larger than it. Unless the target succeeds\
      \ on a DC 13 Strength saving throw, the minotaur pushes it up to 10 feet away\
      \ from the minotaur."
    "name": "Horns"
  - "desc": "_Melee or Ranged Weapon Attack:_ +7 to hit, reach 5 ft. or range 20/60\
      \ ft., one target. _Hit:_ 5 (1d6 + 2) piercing damage, plus 9 (2d8) poison damage."
    "name": "Spear"
"reactions":
  - "desc": "When another Felhide minotaur falls in combat, if the minotaur is the\
      \ only Felhide in a 120-foot radius, the minotaur spends its turns running from\
      \ combat. After one hour, it returns to its fallen comrades and eats them."
    "name": "Felhide Burial Rites"
"source":
  - "TBVXI"
```
^statblock
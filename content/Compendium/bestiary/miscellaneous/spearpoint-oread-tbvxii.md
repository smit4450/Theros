---
title: Spearpoint Oread
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxii
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/miscellaneous
statblock: inline
aliases: ["Spearpoint Oread"]
---
# Spearpoint Oread
*Source: Theros Bestiary TBVXII*  

Every mountain in Theros has a spirit, and these spirits are the oreads. Most of them are friendly, guiding travelers through the labyrinthine mountain passes.

They are close friends with satyrs and are frequent revelers with them.

The spearpoint oread lives on a wooded mountain. Hunters seek out the spearpoint oreads before hunting boars or other game. They also know where to find precious rocks and minerals.

![Spearpoint Oread](Compendium/bestiary/miscellaneous/img/spearpoint-oread.webp#right|850)  

```statblock
"name": "Spearpoint Oread (TBVXII)"
"size": "Medium"
"type": "3rd-level transmutation fey"
"alignment": "Chaotic Good"
"ac": !!int "16"
"ac_class": "natural armor"
"hp": !!int "55"
"hit_dice": "11d8 + 11"
"modifier": !!int "2"
"stats":
  - !!int "14"
  - !!int "14"
  - !!int "12"
  - !!int "11"
  - !!int "13"
  - !!int "18"
"speed": "30 ft."
"skillsaves":
  - "name": "[Acrobatics](Compendium/rules/skills.md#Acrobatics)"
    "desc": "+4"
  - "name": "[Athletics](Compendium/rules/skills.md#Athletics)"
    "desc": "+4"
  - "name": "[Performance](Compendium/rules/skills.md#Performance)"
    "desc": "+6"
  - "name": "[Nature](Compendium/rules/skills.md#Nature)"
    "desc": "+2"
"damage_immunities": "poison"
"condition_immunities": "charmed, frightened, poisoned"
"senses": "passive Perception 10"
"languages": "Common, Sylvan"
"cr": "2"
"traits":
  - "desc": "The oread can move across difficult terrain made of earth or stone without expending extra movement."
    "name": "Earth Walk"
  - "desc": "The oread's innate spellcasting ability is Charisma (spell save DC 14, +6 to hit with spell attacks). It can innately cast the following spells, requiring no material components: At will: _passwall_, _find the path_ 3/day: _stone shape_ 1/day: _hallucinatory terrain_, _wall of stone_, _creation_"
    "name": "Innate Spellcasting"
  - "desc": "The creature can attempt to hide even when it is only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena."
    "name": "Mask of the Wild"
  - "desc": "In addition to being a creature, the oread is a level 3 divine transmutation spell with no target. Its weapon attacks are magical, and it glows with the soft light of the night sky, shedding dim light in a 15-foot radius."
    "name": "Spell Nature"
"actions":
  - "desc": "_Melee or Ranged Weapon Attack:_ +4 to hit, reach 5 ft. or range 80/320 ft., one target. _Hit:_ 5 (1d6 + 2) bludgeoning damage in melee, or 5 (1d6 + 2) bludgeoning damage at range."
    "name": "Rock"
  - "desc": "_Melee or Ranged Weapon Attack:_ +4 to hit, reach 5 ft. or range 20/60 ft., one target. _Hit:_ 4 (1d4 + 2) piercing damage."
    "name": "Stone Dagger"
"source":
  - "TBVXII"
"image": "Compendium/bestiary/miscellaneous/token/spearpoint-oread-tbvxii.webp"
```
^statblock
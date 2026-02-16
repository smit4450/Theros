---
title: Young Gold Dragon
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/10
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/dragon/metallic
statblock: inline
aliases: ["Young Gold Dragon"]
---
# Young Gold Dragon
*Source: Monster Manual (2024) p. 144. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/dragon/img/gold-dragon.webp#right|850)  
Young gold dragons have seen glimpses of the world's true evils and crusade to oppose them. They often seek bold and direct solutions to problems.

## Gold Dragons

*Dragons of Hope and Majesty*

- **Habitat.** Forest, Grassland  
- **Treasure.** [[random-magic-items-arcana|Arcana]]  

Gold dragons work to make the world a better place. The most powerful of the metallic dragons, these awe-inspiring dragons strive to protect that which is good and bend fate toward a brighter future. Their kind dispositions don't prevent gold dragons from engaging in combat when necessary, though, and they exhale brilliant flames and weakening magic to rout their foes.

Gold dragons favor grasslands and pristine forests, frequently dwelling near awe-inspiring natural wonders or guarding monuments from ancient civilizations. In their lairs, gold dragons hoard coins and gems, but they frequently put their treasure to use in pursuit of greater goals. They often use their riches to buy rare lore books, pay informants, or patronize idealistic adventurers.

### Gold Dragon Lairs

Gold dragons make their homes in places of natural and magical wonder.
## Statblock

```statblock
"name": "Young Gold Dragon (XMM)"
"size": "Large"
"type": "dragon"
"subtype": "metallic"
"alignment": "Lawful Good"
"ac": !!int "18"
"hp": !!int "178"
"hit_dice": "17d10 + 85"
"modifier": !!int "6"
"stats":
  - !!int "23"
  - !!int "14"
  - !!int "21"
  - !!int "16"
  - !!int "13"
  - !!int "20"
"speed": "40 ft., fly 80 ft., swim 40 ft."
"saves":
  - "dexterity": !!int "6"
  - "wisdom": !!int "5"
"skillsaves":
  - "name": "[[skills#Insight|Insight]]"
    "desc": "+5"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+9"
  - "name": "[[skills#Persuasion|Persuasion]]"
    "desc": "+9"
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+6"
"damage_immunities": "fire"
"senses": "[[senses#Blindsight|Blindsight]] 30 ft., [[senses#Darkvision|Darkvision]]\
  \ 120 ft., passive Perception 19"
"languages": "Common, Draconic"
"cr": "10"
"traits":
  - "desc": "The dragon can breathe air and water."
    "name": "Amphibious"
"actions":
  - "desc": "The dragon makes three Rend attacks. It can replace one attack with a\
      \ use of Weakening Breath."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +10, reach 10 ft. *Hit:* 17 (2d10 + 6) Slashing\
      \ damage."
    "name": "Rend"
  - "desc": "*Dexterity Saving Throw:* DC 17, each creature in a 30-foot [[cone-area-of-effect-xphb|Cone]].\
      \ *Failure:* 55 (10d10) Fire damage. *Success:* Half damage."
    "name": "Fire Breath (Recharge 5-6)"
  - "desc": "*Strength Saving Throw:* DC 17, each creature that isn't currently affected\
      \ by this breath in a 30-foot [[cone-area-of-effect-xphb|Cone]].\
      \ *Failure:* The target has [[disadvantage-xphb|Disadvantage]]\
      \ on Strength-based [[d20-test-xphb|D20 Tests]]\
      \ and subtracts 3 (1d6) from its damage rolls. It repeats the save at the\
      \ end of each of its turns, ending the effect on itself on a success. After\
      \ 1 minute, it succeeds automatically."
    "name": "Weakening Breath"
"source":
  - "XMM"
"image": "Compendium/bestiary/dragon/token/young-gold-dragon-xmm.webp"
```
^statblock
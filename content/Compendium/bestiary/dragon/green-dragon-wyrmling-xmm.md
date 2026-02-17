---
title: Green Dragon Wyrmling
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/2
- monster/environment/forest
- monster/size/medium
- monster/type/dragon/chromatic
statblock: inline
aliases: ["Green Dragon Wyrmling"]
---
# Green Dragon Wyrmling
*Source: Monster Manual (2024) p. 152. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/dragon/img/green-dragon-wyrmling.webp#right|850)  
Green dragon wyrmlings often serve as pawns in older dragons' schemes. By spying on those dragons' agents, wyrmlings learn the art of manipulation. Once they've accumulated influence and lackeys, these wyrmlings depart to claim their own territories and pursue their sinister ambitions.

## Green Dragons

*Dragons of Deceit and Derision*

- **Habitat.** Forest  
- **Treasure.** [[random-magic-items-arcana|Arcana]]  

From forbidden forest depths, green dragons whisper evils into the world and manipulate the lives of those who listen. Elusive, conniving, and egotistical, these chromatic dragons patiently prey on the fears of shorter-lived beings, corrupting and isolating them. Green dragons might lurk amid labyrinthine wildernesses for centuries without revealing themselves; even their most devoted followers might know them only as the voice of the woodlands or a whisper in their dreams.

Despite their might, most green dragons disdain physical violence, viewing combat as servants' work and preferring to trick foes into dangerous or exploitative scenarios. These dragons collect "baubles" that embody their webs of manipulation and serve as tools of extortion, such as compromising documents, family heirlooms, and sentimental treasures.

### Green Dragon Lairs

Green dragons lair in ancient forests, often shaping stands of massive trees into compounds of interwoven branches, hollow trunks, and caverns amid mighty roots. They might also dwell amid forested ruins, particularly the former homes of those they've conquered.
## Statblock

```statblock
"name": "Green Dragon Wyrmling (XMM)"
"size": "Medium"
"type": "dragon"
"subtype": "chromatic"
"alignment": "Lawful Evil"
"ac": !!int "17"
"hp": !!int "38"
"hit_dice": "7d8 + 7"
"modifier": !!int "3"
"stats":
  - !!int "15"
  - !!int "12"
  - !!int "13"
  - !!int "14"
  - !!int "11"
  - !!int "13"
"speed": "30 ft., fly 60 ft., swim 30 ft."
"saves":
  - "dexterity": !!int "3"
  - "wisdom": !!int "2"
"skillsaves":
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+4"
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+3"
"damage_immunities": "poison"
"condition_immunities": "[[conditions#Poisoned|poisoned]]"
"senses": "[[senses#Blindsight|Blindsight]] 10 ft., [[senses#Darkvision|Darkvision]]\
  \ 60 ft., passive Perception 14"
"languages": "Draconic"
"cr": "2"
"traits":
  - "desc": "The dragon can breathe air and water."
    "name": "Amphibious"
"actions":
  - "desc": "The dragon makes two Rend attacks."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +4, reach 5 ft. *Hit:* 7 (1d10 + 2) Slashing\
      \ damage plus 3 (1d6) Poison damage."
    "name": "Rend"
  - "desc": "*Constitution Saving Throw:* DC 11, each creature in a 15-foot [[cone-area-of-effect-xphb|Cone]].\
      \ *Failure:* 21 (6d6) Poison damage. *Success:* Half damage."
    "name": "Poison Breath (Recharge 5-6)"
"source":
  - "XMM"
"image": "Compendium/bestiary/dragon/token/green-dragon-wyrmling-xmm.webp"
```
^statblock
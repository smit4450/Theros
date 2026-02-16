---
title: Flumph
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/1-8
- ttrpg-cli/monster/environment/underdark
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/aberration
statblock: inline
aliases: ["Flumph"]
---
# Flumph
*Source: Monster Manual (2024) p. 122*  

![](Compendium/books/monster-manual-2025/img/flumph.webp#right)  
## Flumph

*Strange Ally from a Strange Place*

- **Habitat.** Underdark  
- **Treasure.** [[random-magic-items-arcana|Arcana]]  

Bizarre creatures with aberrant agendas inhabit the Underdark. Flumphs number among the few that are helpful to strangers.

These tentacled, telepathic creatures jet through the air in short bursts, venting gases with a sound that gives them their name. Rather than speaking, flumphs communicate telepathically and by changing color to reflect their moods.

Flumphs dwell in psychically charged regions or near creatures with psionic magic. They harmlessly feed off psychic energies, but in doing so, they often encounter dangerous beings such as aboleths and mind flayers. While flumphs generally avoid combat, they often help adventurers in peril. Such help might be of doubtful use, but flumphs mean well. Roll on or choose a result from the Flumph Assistance table to inspire what support flumphs provide.

**Flumph Assistance**

| dice: 1d6 | The Flumph Helps By... |
|-----------|------------------------|
| 1 | Cooking a meal of Underdark delicacies. |
| 2 | Performing a psychic song or "smell poem." |
| 3 | Recovering and nursing fallen adventurers. |
| 4 | Revealing the location of helpful magic items. |
| 5 | Serving as a guide to a foe's hidden lair. |
| 6 | Sharing excessive encouragement and praise. |
^flumph-assistance

### Flumph Colors

A flumph's extremities change color to reflect its mood. The Flumph Colors and Emotions table summarizes common flumph colors and the human emotions to which they most closely correspond.

**Flumph Colors and Emotions**

| Color | Emotion |
|-------|---------|
| Blue, Dark | Sadness |
| Blue, Light | Happiness |
| Green | Curiosity |
| Magenta | Unknown* |
| Orange | Confusion |
| Pink | Amusement |
| Purple | Fear |
| Red | Anger |
| Teal | Serenity |
| Yellow | Excitement |
^flumph-colors-and-emotions

*Rarely seen; potentially no human equivalent
```statblock
"name": "Flumph (XMM)"
"size": "Small"
"type": "aberration"
"alignment": "Lawful Good"
"ac": !!int "12"
"hp": !!int "7"
"hit_dice": "2d6"
"modifier": !!int "2"
"stats":
  - !!int "6"
  - !!int "15"
  - !!int "10"
  - !!int "14"
  - !!int "14"
  - !!int "11"
"speed": "5 ft., fly 30 ft. (hover)"
"skillsaves":
  - "name": "[[skills#Arcana|Arcana]]"
    "desc": "+4"
  - "name": "[[skills#History|History]]"
    "desc": "+4"
  - "name": "[[skills#Religion|Religion]]"
    "desc": "+4"
"damage_vulnerabilities": "psychic"
"senses": "[[senses#Darkvision|Darkvision]] 60 ft., passive Perception\
  \ 12"
"languages": "understands Undercommon but can't speak; telepathy 60 ft."
"cr": "1/8"
"traits":
  - "desc": "The flumph perceives the content of any telepathic communication within\
      \ 60 feet of it."
    "name": "Advanced Telepathy"
  - "desc": "If the flumph receives the [[conditions#Prone|Prone]]\
      \ condition, roll a die. On an odd number, it has the [[conditions#Incapacitated|Incapacitated]]\
      \ condition. At the end of each of its turns, the flumph makes a DC 10 Dexterity\
      \ saving throw, ending the [[conditions#Incapacitated|Incapacitated]]\
      \ condition on a success."
    "name": "Prone Deficiency"
  - "desc": "The flumph's thoughts can't be read by any means, and magic can't detect\
      \ its location or observe it remotely."
    "name": "Telepathic Shroud"
"actions":
  - "desc": "*Melee Attack Roll:* +4, reach 5 feet. *Hit:* 4 (1d4 + 2) Acid damage."
    "name": "Tentacle"
  - "desc": "*Dexterity Saving Throw:* DC 10, one creature the flumph can see within\
      \ 15 feet. *Failure:* The target is coated in a foul-smelling liquid, exudes\
      \ a stench for 1d4 hours, and has the [[conditions#Poisoned|Poisoned]]\
      \ condition while the stench lasts. Other creatures have the [[conditions#Poisoned|Poisoned]]\
      \ condition while in a 5-foot [[emanation-area-of-effect-xphb|Emanation]]\
      \ originating from the coated target. The target can remove the stench on itself\
      \ if it bathes during a [[short-rest-xphb|Short]]\
      \ or [[long-rest-xphb|Long Rest]]."
    "name": "Stench Spray (1/Day)"
"source":
  - "XMM"
"image": "Compendium/bestiary/aberration/token/flumph-xmm.webp"
```
^statblock
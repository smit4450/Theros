---
title: Doppelganger
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/3
- monster/environment/underdark
- monster/environment/urban
- monster/size/medium
- monster/type/monstrosity
statblock: inline
aliases: ["Doppelganger"]
---
# Doppelganger
*Source: Monster Manual (2024) p. 100, FRHoF. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/monstrosity/img/doppelganger.webp#right|850)  
## Doppelganger

*Shape-Shifting Infiltrator*

- **Habitat.** Underdark, Urban  
- **Treasure.** Individual  

Doppelgangers are supernatural beings with the ability to shape-shift into any humanlike form. Their mind-reading abilities aid them in creating near-perfect disguises and plucking secrets from unguarded minds. Occasionally, doppelgangers use their shape-shifting ability in more overt ways, transforming into unsettling forms to frighten foes.

A doppelganger's agenda might relate to its mysterious magical origins or to more mercenary goals. Roll on or choose a result from the Doppelganger Deceptions table to inspire a doppelganger's plot.

**Doppelganger Deceptions**

| dice: 1d6 | The Doppelganger Schemes To... |
|-----------|--------------------------------|
| 1 | Cause chaos within the temple of a deity that cursed it to live without a true form. |
| 2 | Conceal evidence of a vast conspiracy. |
| 3 | Control a community through fear by posing as a legendary bogeyman. |
| 4 | Replace a noble to enjoy a decadent lifestyle. |
| 5 | Spy on wizards to learn how to complete its own botched magical creation. |
| 6 | Take an influential position, acting as a sleeper agent for a doppelganger invasion. |
^doppelganger-deceptions

> [!quote] A quote from Someone claiming to be Lorhirin of Fearchor Keep  
> 
> Meeting yourself is the surest way to realize you're not as charming as you think you are.

```statblock
"name": "Doppelganger (XMM)"
"size": "Medium"
"type": "monstrosity"
"alignment": "Neutral"
"ac": !!int "14"
"hp": !!int "52"
"hit_dice": "8d8 + 16"
"modifier": !!int "4"
"stats":
  - !!int "11"
  - !!int "18"
  - !!int "14"
  - !!int "11"
  - !!int "12"
  - !!int "14"
"speed": "30 ft."
"skillsaves":
  - "name": "[[skills#Deception|Deception]]"
    "desc": "+6"
  - "name": "[[skills#Insight|Insight]]"
    "desc": "+3"
"condition_immunities": "[[conditions#Charmed|charmed]]"
"senses": "[[senses#Darkvision|Darkvision]] 60 ft., passive Perception\
  \ 11"
"languages": "Common plus three other languages"
"cr": "3"
"actions":
  - "desc": "The doppelganger makes two Slam attacks and uses Unsettling Visage if\
      \ available."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +6 (with [[advantage-xphb|Advantage]]\
      \ during the first round of each combat), reach 5 ft. *Hit:* 11 (2d6 + 4)\
      \ Bludgeoning damage."
    "name": "Slam"
  - "desc": "*Wisdom Saving Throw:* DC 12, each creature in a 15-foot [[emanation-area-of-effect-xphb|Emanation]]\
      \ originating from the doppelganger that can see the doppelganger. *Failure:*\
      \ The target has the [[conditions#Frightened|Frightened]]\
      \ condition and repeats the save at the end of each of its turns, ending the\
      \ effect on itself on a success. After 1 minute, it succeeds automatically."
    "name": "Unsettling Visage (Recharge 6)"
  - "desc": "The doppelganger casts [[detect-thoughts-xphb|Detect Thoughts]],\
      \ requiring no spell components and using Charisma as the spellcasting ability\
      \ (spell save DC 12).\n"
    "name": "Read Thoughts"
"bonus_actions":
  - "desc": "The doppelganger shape-shifts into a Medium or Small Humanoid, or it\
      \ returns to its true form. Its game statistics, other than its size, are the\
      \ same in each form. Any equipment it is wearing or carrying isn't transformed."
    "name": "Shape-Shift"
"source":
  - "XMM"
  - "FRHoF"
"image": "Compendium/bestiary/monstrosity/token/doppelganger-xmm.webp"
```
^statblock
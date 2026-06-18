---
title: Serpent Dancer
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvxiv
- monster/cr/0
- monster/size/m
- monster/type/humanoid
statblock: inline
aliases: ["Serpent Dancer"]
---
# Serpent Dancer
*Source: Theros Bestiary TBVXIV*  



![Serpent Dancer](Homebrew/bestiary/humanoid/img/serpent-dancer.webp#right)  

```statblock
"name": "Serpent Dancer (TBVXIV)"
"size": "Medium"
"type": "humanoid"
"subtype": "human"
"alignment": "Chaotic Neutral"
"ac": !!int "11"
"hp": !!int "4"
"hit_dice": "1d8 + 0"
"modifier": !!int "3"
"stats":
  - !!int "11"
  - !!int "16"
  - !!int "11"
  - !!int "13"
  - !!int "13"
  - !!int "15"
"speed": "10 ft."
"skillsaves":
  - "name": "[[skills#Acrobatics|Acrobatics]]"
    "desc": "+5"
  - "name": "[[skills#Animal Handling|Animal Handling]]"
    "desc": "+3"
  - "name": "[[skills#Performance|Performance]]"
    "desc": "+4"
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+5"
  - "name": "[[skills#Intimidation|Intimidation]]"
    "desc": "+4"
"senses": "passive Perception 10"
"languages": "Common, any language"
"cr": "0"
"traits":
  - "desc": "The dancer and up to two serpents it holds are friendly to one another as long as the dancer controls its own actions."
    "name": "Control Serpent"
  - "desc": "If the reveler performs for at least 1 minute, it chooses up to four humanoids within 60 feet of it who watched or listened to the entire performance. Each target must succeed on a DC 13 Wisdom saving throw or be [[conditions#Charmed|charmed]]. While [[conditions#Charmed|charmed]] in this way, the target idolizes the reveler and will take part in the reveler’s revels. The [[conditions#Charmed|charmed]] condition ends for the creature after 1 hour, if it takes any damage, if the reveler attacks the target, or if the target witnesses the reveler attacking or damaging any of the target’s allies."
    "name": "Enthralling Performance"
  - "desc": "While the serpent dancer is handling a serpent, any humanoid that starts its turn within 30 feet of the dancer and can see the dancer must make a DC 11 Wisdom saving throw. On a failed save, the creature is [[conditions#Frightened|frightened]] for 1 minute. A creature can repeat the saving throw at the end of each of its turns, with [[disadvantage-xphb|Disadvantage]] if the dancer is within line of sight, ending the effect on itself on a success. If a creature's saving throw is successful or the effect ends for it, the creature is immune to the dancer's Horrific Appearance for the next 24 hours. Unless the target is surprised or the revelation that it holds a serpent is sudden, the target can avert its eyes and avoid making the initial saving throw. Until the start of its next turn, a creature that averts its eyes has [[disadvantage-xphb|Disadvantage]] on attack rolls against the dancer."
    "name": "Horrific Appearance"
  - "desc": "Magic can’t put the reveler to sleep."
    "name": "Sleepless Reveler"
"source":
  - "TBVXIV"
"image": "Homebrew/bestiary/humanoid/token/serpent-dancer-tbvxiv.webp"
```
^statblock
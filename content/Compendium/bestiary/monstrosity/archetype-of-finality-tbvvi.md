---
title: Archetype of Finality
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvvi
- monster/cr/7
- monster/size/m
- monster/type/monstrosity
statblock: inline
aliases: ["Archetype of Finality"]
---
# Archetype of Finality
*Source: Theros Bestiary TBVVI*  

<blockquote><small>She sees mortals not as they wish to be, but as what they will become.</small></blockquote>
The archetype of finality is a gorgon blessed by Pharika. Her blessing extends to her allies.

![Archetype of Finality](Compendium/bestiary/monstrosity/img/archetype-of-finality.webp#right|850)  

```statblock
"name": "Archetype of Finality (TBVVI)"
"size": "Medium"
"type": "monstrosity"
"subtype": "medusa, gorgon"
"alignment": "Lawful Evil"
"ac": !!int "15"
"hp": !!int "119"
"hit_dice": "17d8 + 51"
"modifier": !!int "2"
"stats":
  - !!int "10"
  - !!int "15"
  - !!int "16"
  - !!int "12"
  - !!int "13"
  - !!int "15"
"speed": "30 ft."
"skillsaves":
  - "name": "[[skills#Deception|Deception]]"
    "desc": "+5"
  - "name": "[[skills#Insight|Insight]]"
    "desc": "+4"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+4"
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+5"
  - "name": "[[skills#Medicine|Medicine]]"
    "desc": "+4"
"senses": "[[senses#Darkvision|Darkvision]] 60 ft., passive Perception 10"
"languages": "Common"
"cr": "7"
"traits":
  - "desc": "The gorgon is an expert in extending its own life to immortality, and it enjoys a high-stake deal. If a creature successfully restrains the gorgon, it will share one of its medicinal secrets in exchange for its freedom."
    "name": "Gorgon's Trial"
  - "desc": "The gorgon doesn't require food, drink, or sleep."
    "name": "Immortal Nature"
  - "desc": "The gorgon has [[advantage-xphb|Advantage]] on saving throws against spells and other magical effects."
    "name": "Magic Resistance"
  - "desc": "The gorgon's weapon attacks are magical."
    "name": "Magic Weapons"
  - "desc": "As soon as a creature within 30 feet of the gorgon sees the gorgon's face, it may make a DC 14 Constitution saving throw. On a success, that creature may use a reaction to shield its eyes or avert them. If the saving throw fails by 5 or more, or if the creature is unable to react, the creature is instantly [[conditions#Petrified|petrified]]. Otherwise, a creature that fails the save begins to turn to stone and is [[conditions#Restrained|restrained]]. The [[conditions#Restrained|restrained]] creature must repeat the saving throw at the end of its next turn, becoming [[conditions#Petrified|petrified]] on a failure or ending the effect on a success. The petrification lasts until the creature is unpetrified by a god. If the gorgon sees its own face reflected on a polished surface within 30 ft. of it and in an area of bright light, the gorgon is, due to its curse, affected by its own visage. This trait has no effect if the gorgon's face is not its normal flesh state. The trait remains active even if the gorgon is [[conditions#Incapacitated|incapacitated]], killed, and even beheaded."
    "name": "Petrifying Visage"
  - "desc": "Allies of the gorgon that it can see within 120 ft. can use a bonus action on their turn to do the following: **_Diversion._** The allied creature points, cocks its head, or some other gesture to try to get other creatures to look away and look instead at the gorgon. Each creature that can see the ally must succeed on a DC 15 Wisdom saving throw or look at the gorgon.As long as the gorgon can see any non-allies within 120 ft., they do not have the Diversion ability and cannot gain it."
    "name": "Provide Diversion"
  - "desc": "The gorgon glows with the soft light of the night sky, shedding dim light in a 15-foot radius."
    "name": "Starlight Form"
"actions":
  - "desc": "The gorgon makes either three melee attacks—one with its snake hair, one to constrict, and one with its shortsword—or two ranged attacks with its longbow."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +3 to hit, reach 10 ft., one target. Hit: 7 (2d6) bludgeoning damage, and the target is [[conditions#Grappled|grappled]] (escape DC 11) if it is a Large or smaller creature. Until this grapple ends, the target is [[conditions#Restrained|restrained]], and the gorgon can’t constrict another target."
    "name": "Constrict"
  - "desc": "Ranged Weapon Attack: +5 to hit, range 150/600 ft., one target. Hit: 6 (1d8 + 2) piercing damage plus 7 (2d6) poison damage."
    "name": "Longbow"
  - "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) piercing damage."
    "name": "Shortsword"
  - "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one creature. Hit: 4 (1d4 + 2) piercing damage plus 14 (4d6) poison damage."
    "name": "Snake Hair"
"source":
  - "TBVVI"
"image": "Compendium/bestiary/monstrosity/token/archetype-of-finality-tbvvi.webp"
```
^statblock
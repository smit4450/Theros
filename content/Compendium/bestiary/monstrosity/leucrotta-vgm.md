---
title: Leucrotta
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/vgm
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/environment/grassland
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/monstrosity
statblock: inline
aliases: ["Leucrotta"]
---
# Leucrotta
*Source: Volo's Guide to Monsters p. 169, Mythic Odysseys of Theros*  

![](Compendium/bestiary/monstrosity/img/leucrotta.webp#right|850)  
A leucrotta is what you would get if you took the head of a giant badger, the brain of a person who likes to torture and eat people, the legs of a deer, and the body of a large hyena, put them together, and reanimated them with demon ichor without bothering to cover up the stink of death.

## Spawn of Yeenoghu

The first leucrottas came into being alongside the gnolls during Yeenoghu's rampages on the Material Plane. Some of the hyenas that ate Yeenoghu's kills went through different transformations rather than turning into gnolls. Among these bizarre results, leucrottas were the most numerous.

As clever as it is cruel, a leucrotta loves to deceive, torture, and kill. Because leucrottas are smarter and tougher than most gnolls, one could occupy an elevated position within a gnoll tribe. Although a leucrotta is unlikely to lead a group of gnolls, it can influence the leader, and it might even agree to carry a leader into battle and offer advice during the fight.

Gnolls see leucrottas as a form of entertainment, partly because a leucrotta can mimic the squeals of a suffering victim-a sound that always gives gnolls pleasure-even when no victims are to be had. Further, a gnoll is bloodthirsty and sadistic, but unable by its nature to prolong the fun of killing. Most leucrottas are consciously cruel, to the point of being meticulous about their savagery to draw out a kill into better and longer sport. Gnolls enjoy watching a leucrotta work almost as much as they like doing their own killing.

## Foulness Embodied

The leucrotta is so loathsome that only gnolls and others of its kind can stand to be around one for long. Its horrific, hodgepodge body oozes a foul stench that pollutes anywhere the creature lairs. This reek is outdone only by the creature's breath, which issues from a maw that drips fluid corrupted with rot and digestive juices. In place of fangs, a leucrotta has bony ridges as hard as steel that can crush bones and lacerate flesh. These plates are so tough that a leucrotta can use them to peel plate armor away from the body of a slain knight.

A leucrotta's stench would normally warn away prey long before the creature could attack. It has two natural capabilities, however, that give it an advantage. First, a leucrotta's tracks are nearly impossible to distinguish from those of common deer. Second, it can duplicate the call or the vocal expressions of just about any creature it has heard. The monster uses its mimicry to lure in potential victims, then attacks when they are confused or unaware of the actual threat.
## Statblock

```statblock
"name": "Leucrotta (VGM)"
"size": "Large"
"type": "monstrosity"
"alignment": "Chaotic Evil"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "67"
"hit_dice": "9d10 + 18"
"modifier": !!int "2"
"stats":
  - !!int "18"
  - !!int "14"
  - !!int "15"
  - !!int "9"
  - !!int "12"
  - !!int "6"
"speed": "50 ft."
"skillsaves":
  - "name": "[Deception](Compendium/rules/skills.md#Deception)"
    "desc": "+2"
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+3"
"senses": "[darkvision](Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception\
  \ 13"
"languages": "Abyssal, Gnoll"
"cr": "3"
"traits":
  - "desc": "The leucrotta has advantage on Wisdom ([Perception](Compendium/rules/skills.md#Perception))\
      \ checks that rely on smell."
    "name": "Keen Smell"
  - "desc": "If the leucrotta attacks with its hooves, it can take the Disengage action\
      \ as a bonus action."
    "name": "Kicking Retreat"
  - "desc": "The leucrotta can mimic animal sounds and humanoid voices. A creature\
      \ that hears the sounds can tell they are imitations with a successful DC 14\
      \ Wisdom ([Insight](Compendium/rules/skills.md#Insight)) check."
    "name": "Mimicry"
  - "desc": "When the leucrotta reduces a creature to 0 hit points with a melee attack\
      \ on its turn, it can take a bonus action to move up to half its speed and make\
      \ an attack with its hooves."
    "name": "Rampage"
"actions":
  - "desc": "The leucrotta makes two attacks: one with its bite and one with its hooves."
    "name": "Multiattack"
  - "desc": "*Melee Weapon Attack:* +6 to hit, reach 5 ft., one target. *Hit:* 8\
      \ (1d8 + 4) piercing damage. If the leucrotta scores a critical hit, it rolls\
      \ the damage dice three times, instead of twice."
    "name": "Bite"
  - "desc": "*Melee Weapon Attack:* +6 to hit, reach 5 ft., one target. *Hit:* 11\
      \ (2d6 + 4) bludgeoning damage."
    "name": "Hooves"
"source":
  - "VGM"
  - "MOT"
"image": "Compendium/bestiary/monstrosity/token/leucrotta-vgm.webp"
```
^statblock
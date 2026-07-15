---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/tbvxviii
- monster/cr/5
- monster/size/medium
- monster/type/humanoid/human
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Fabled Hero"
---
# Fabled Hero
*Source: Theros Bestiary, Vol. XVIII*
![](/Compendium/bestiary/humanoid/img/fabled-hero.webp#center)

```statblock
"name": "Fabled Hero"
"size": "Medium"
"type": "humanoid"
"subtype": "human"
"alignment": "Any alignment"
"ac": !!int "17"
"ac_class": "half plate"
"hp": !!int "24"
"hit_dice": "4d8 + 8"
"modifier": !!int "2"
"stats":
  - !!int "17"
  - !!int "14"
  - !!int "15"
  - !!int "11"
  - !!int "12"
  - !!int "12"
"speed": "30 ft."
"skillsaves":
  - "name": "[Survival](/Compendium/rules/skills.md#Survival)"
    "desc": "+3"
  - "name": "[Acrobatics](/Compendium/rules/skills.md#Acrobatics)"
    "desc": "+4"
  - "name": "[Athletics](/Compendium/rules/skills.md#Athletics)"
    "desc": "+5"
"senses": "passive Perception 10"
"languages": "Common"
"cr": "5"
"traits":
  - "desc": "When the hero is reduced to 0 Hit Points but not killed outright, it\
      \ can drop to 1 hit point instead."
    "name": "Hard to Kill (Recharges After a Long Rest)"
"actions":
  - "desc": "The hero has two chains. It makes one chain attack for each of its chains\
      \ that aren't already grappling a target."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 9 (2d6\
      \ + 2) slashing damage. The target is grappled (escape DC 14) if the hero isn't\
      \ already grappling a creature. Until this grapple ends, the target is restrained\
      \ and takes 7 (2d6) piercing damage at the start of each of its turns."
    "name": "Chain"
"reactions":
  - "desc": "Whenever the hero is the target of a spell, that spell's caster chooses\
      \ whether following happens: - Until the end of combat, the hero gains a +1\
      \ bonus to damage rolls and Dexterity checks, and it gains 4 (1d8) temporary\
      \ Hit Points."
    "name": "Heroic"
"source":
  - "TBVXVIII"
```
^statblock
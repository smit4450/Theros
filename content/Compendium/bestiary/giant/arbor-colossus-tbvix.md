---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/tbvix
- monster/cr/20
- monster/size/gargantuan
- monster/type/giant
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Arbor Colossus"
---
# Arbor Colossus
*Source: Theros Bestiary, Vol. IX*
![](/Compendium/bestiary/giant/img/arbor-colossus.webp#center)

```statblock
"name": "Arbor Colossus"
"size": "Gargantuan"
"type": "giant"
"alignment": "Any alignment"
"ac": !!int "16"
"ac_class": "studded leather armor"
"hp": !!int "960"
"hit_dice": "60d20 + 360"
"modifier": !!int "6"
"stats":
  - !!int "22"
  - !!int "22"
  - !!int "22"
  - !!int "12"
  - !!int "14"
  - !!int "11"
"speed": "50 ft."
"skillsaves":
  - "name": "[Acrobatics](/Compendium/rules/skills.md#Acrobatics)"
    "desc": "+12"
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+24"
"senses": "passive Perception 10"
"languages": "Giant"
"cr": "20"
"traits":
  - "desc": "As a bonus action, the archer can add 1d10 to its next attack or damage\
      \ roll with a longbow or shortbow."
    "name": "Archer's Eye (3/Day)"
  - "desc": "When the colossus is reduced to 0 Hit Points, it doesn’t die or fall\
      \ unconscious. Instead, the damage creates tears in its skin, revealing its\
      \ hearts. The colossus has three hearts in its chest. A heart has an AC of 16\
      \ and 165 Hit Points. It is immune to all conditions. If it is forced to make\
      \ a saving throw, treat its ability scores as 10 (+0). The colossus dies when\
      \ all the hearts are destroyed."
    "name": "Hearts of the Colossus (Mythic Trait; Recharges after a Short or Long\
      \ Rest)"
  - "desc": "Unless provoked, the giant ignores all nonflying things that are Huge\
      \ or smaller and all flying things that are Large or smaller."
    "name": "Titanic Nature"
"actions":
  - "desc": "The colossus makes two attacks with its longbow."
    "name": "Multiattack"
  - "desc": "_Ranged Weapon Attack:_ +14 to hit, range 300/1200 ft., one target. _Hit:_\
      \ 60 (12d8 + 6) piercing damage."
    "name": "Longbow"
"legendary_description": "Legendary Action Uses: 3. Immediately after another creature's\
  \ turn, the arbor colossus can expend a use to take one of the following actions.\
  \ The arbor colossus regains all expended uses at the start of each of its turns."
"legendary_actions":
  - "desc": "**Mythic Actions**If the colossus's mythic trait is active, it can use\
      \ the options below as legendary actions for 1 hour after using Hearts of the\
      \ Colossus. **_Desperate Shot._** The colossus makes a longbow attack against\
      \ creature that is flying."
    "name": ""
"source":
  - "TBVIX"
```
^statblock
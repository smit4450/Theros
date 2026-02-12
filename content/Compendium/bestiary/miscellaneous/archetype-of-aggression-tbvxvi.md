---
title: Archetype of Aggression
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxvi
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/miscellaneous
statblock: inline
aliases: ["Archetype of Aggression"]
---
# Archetype of Aggression
*Source: Theros Bestiary TBVXVI*  

<blockquote><small>“Did Purphoros bless Maikal because of his rage? Or did Maikal’s rage blossom after he’d been blessed? Only the gods know.” —Eocles, oracle of Purphoros</small></blockquote>
The archetype of aggression is a human warrior blessed by Purphoros. His blessing extends to his allies.

![Archetype of Aggression](Compendium/bestiary/miscellaneous/img/archetype-of-aggression.webp#right|850)  

```statblock
"name": "Archetype of Aggression (TBVXVI)"
"size": "Medium"
"type": "human"
"alignment": "Chaotic Neutral"
"ac": !!int "13"
"hp": !!int "63"
"hit_dice": "9d8 + 27"
"modifier": !!int "1"
"stats":
  - !!int "16"
  - !!int "12"
  - !!int "17"
  - !!int "9"
  - !!int "11"
  - !!int "9"
"speed": "30 ft."
"senses": "passive Perception 10"
"languages": "Common"
"cr": "3"
"traits":
  - "desc": "Allies of the archetype that it can see within 120 ft. have the archetype's Trample ability. As long as the archetype can see any non-allies within 120 ft., they do not have the Trample ability and cannot gain it."
    "name": "Blessing of Purphoros"
  - "desc": "The archetype of aggression's weapon attacks are magical."
    "name": "Magic Weapons"
  - "desc": "The archetype glows with the soft light of the night sky, shedding dim light in a 15-foot radius."
    "name": "Starlight Form"
  - "desc": "The archetype can move in and out of a Medium or smaller creature's space. If it would, it uses a bonus action to attack that creature with its unarmed strike. That creature must succeed on a DC 13 Strength saving throw or be knocked prone. If the creature succeeds, the archetype can't enter that space and must end its turn immediately. If the archetype stops on top of that creature, that creature becomes restrained until the archetype moves off it (escape DC 13)."
    "name": "Trample"
"actions":
  - "desc": "The archetype makes two unarmed strikes."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 17 bludgeoning damage."
    "name": "Unarmed Strike"
"source":
  - "TBVXVI"
"image": "Compendium/bestiary/miscellaneous/token/archetype-of-aggression-tbvxvi.webp"
```
^statblock
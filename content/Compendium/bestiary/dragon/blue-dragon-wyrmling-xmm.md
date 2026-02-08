---
title: Blue Dragon Wyrmling
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/environment/coastal
- ttrpg-cli/monster/environment/desert
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/dragon/chromatic
statblock: inline
aliases: ["Blue Dragon Wyrmling"]
---
# Blue Dragon Wyrmling
*Source: Monster Manual (2024) p. 48. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*  

![](Compendium/bestiary/dragon/img/blue-dragon-wyrmling.webp#right)  
Blue dragon wyrmlings often serve other powerful creatures, learning the ways of control and establishing fearful reputations among weaker creatures. Many wyrmlings initially serve loyally, but as their powers grow to match their ambitions, they eventually betray or abandon their associates. These wyrmlings tempt small groups of creatures into their service, rewarding them with modest treasures and promises of future power.

## Blue Dragons

*Dragons of Tyranny and Tempests*

- **Habitat.** Desert  
- **Treasure.** [Relics](Compendium/tables/random-magic-items-relics.md)  

Arrogant and imperious, blue dragons are chromatic dragons that crave control and collect followers like other dragons hoard treasure. They seek to transform their territories into empires, domains to be feared by nations.

Blue dragons have sharp features with piercing horns and scales that range from sapphire to the shades of stormy skies. They dwell in deserts and badlands, particularly regions with dramatic spires from whose tops they might see for miles. They seek lairs near sites of symbolic power, such as the abandoned fortresses of giants, the colossi of fallen empires, or monuments raised by their followers.

Regalia of rulership and artistic masterpieces fill blue dragons' hoards. These dragons have no interest in treasures that are common or flawed, preferring one-of-a-kind gemstones, the crowns of fallen royals, and magic items capable of spreading the dragons' influence.

### Blue Dragon Lairs

Blue dragons dwell in arid lands. Their lairs might be death traps meant to entomb invaders or ostentatious fortresses where they plot domination.
## Statblock

```statblock
"name": "Blue Dragon Wyrmling (XMM)"
"size": "Medium"
"type": "dragon"
"subtype": "chromatic"
"alignment": "Lawful Evil"
"ac": !!int "17"
"hp": !!int "65"
"hit_dice": "10d8 + 20"
"modifier": !!int "2"
"stats":
  - !!int "17"
  - !!int "10"
  - !!int "15"
  - !!int "12"
  - !!int "11"
  - !!int "15"
"speed": "30 ft., burrow 15 ft., fly 60 ft."
"saves":
  - "dexterity": !!int "2"
  - "wisdom": !!int "2"
"skillsaves":
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+4"
  - "name": "[Stealth](Compendium/rules/skills.md#Stealth)"
    "desc": "+2"
"damage_immunities": "lightning"
"senses": "[Blindsight](Compendium/rules/senses.md#Blindsight) 10 ft., [Darkvision](Compendium/rules/senses.md#Darkvision)\
  \ 60 ft., passive Perception 14"
"languages": "Draconic"
"cr": "3"
"actions":
  - "desc": "The dragon makes two Rend attacks."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +5, reach 5 ft. *Hit:* 8 (1d10 + 3) Slashing\
      \ damage plus 3 (1d6) Lightning damage."
    "name": "Rend"
  - "desc": "*Dexterity Saving Throw:* DC 12, each creature in a 30-foot-long, 5-foot-wide\
      \ [Line](Compendium/rules/variant-rules/line-area-of-effect-xphb.md). *Failure:*\
      \ 21 (6d6) Lightning damage. *Success:* Half damage."
    "name": "Lightning Breath (Recharge 5-6)"
"source":
  - "XMM"
"image": "Compendium/bestiary/dragon/token/blue-dragon-wyrmling-xmm.webp"
```
^statblock
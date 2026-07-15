---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/mot
- monster/cr/3
- monster/size/large
- monster/type/monstrosity
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Fleecemane Lion"
---
# Fleecemane Lion
*Source: Mythic Odysseys of Theros p. 223*
![](/Compendium/bestiary/monstrosity/img/fleecemane-lion.webp#right)

Twice the size of normal lions and with resplendent manes of silvery or golden hair, fleecemane lions prowl and protect sites imbued with the power of Nyx. While the specifics of these massive lions' connection to Nyx is unclear, many myths tell of the deadly predators stalking mortals and spreading fear until they're ultimately defeated by a brave hunter. As a result, overcoming a fleecemane lion is widely considered an early step on the road to becoming a true hero.

```statblock
"name": "Fleecemane Lion"
"size": "Large"
"type": "monstrosity"
"alignment": "Unaligned"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "45"
"hit_dice": "6d10 + 12"
"modifier": !!int "3"
"stats":
  - !!int "19"
  - !!int "16"
  - !!int "14"
  - !!int "6"
  - !!int "14"
  - !!int "10"
"speed": "50 ft."
"saves":
  - "strength": !!int "6"
  - "constitution": !!int "4"
"skillsaves":
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+4"
  - "name": "[Stealth](/Compendium/rules/skills.md#Stealth)"
    "desc": "+5"
"senses": "passive Perception 14"
"languages": ""
"cr": "3"
"traits":
  - "desc": "The lion has advantage on Wisdom ([Perception](/Compendium/rules/skills.md#Perception))\
      \ checks that rely on smell."
    "name": "Keen Smell"
  - "desc": "If the lion moves at least 20 feet straight toward a creature and then\
      \ hits it with a claw attack on the same turn, that target must succeed on a\
      \ DC 14 Strength saving throw or be knocked [prone](/Compendium/rules/conditions.md#Prone).\
      \ If the target is [prone](/Compendium/rules/conditions.md#Prone), the lion\
      \ can make one bite attack against it as a bonus action."
    "name": "Pounce"
  - "desc": "With a 10-foot running start, the lion can long jump up to 25 feet."
    "name": "Running Leap"
  - "desc": "The lion has advantage on saving throws against any spell that targets\
      \ only the lion (not an area). If the lion's saving throw succeeds and the spell\
      \ is of 4th level or lower, the spell has no effect on the lion and instead\
      \ targets the caster."
    "name": "Spell Turning"
"actions":
  - "desc": "The lion makes two attacks: one with its bite and one with its claw."
    "name": "Multiattack"
  - "desc": "*Melee Weapon Attack:* +6 to hit, reach 5 ft., one target. *Hit:* 8 (1d8\
      \ + 4) piercing damage."
    "name": "Bite"
  - "desc": "*Melee Weapon Attack:* +6 to hit, reach 5 ft., one target. *Hit:* 7 (1d6\
      \ + 4) slashing damage."
    "name": "Claw"
"legendary_description": "Legendary Action Uses: 2. Immediately after another creature's\
  \ turn, the fleecemane lion can expend a use to take one of the following actions.\
  \ The fleecemane lion regains all expended uses at the start of each of its turns."
"legendary_actions":
  - "desc": "The lion makes one claw attack."
    "name": "Claw"
  - "desc": "The lion emits a magical roar. Each creature within 60 feet of the lion\
      \ that can hear the roar must succeed on a DC 12 Wisdom saving throw or be [frightened](/Compendium/rules/conditions.md#Frightened)\
      \ of the lion until the end of the lion's next turn."
    "name": "Roar (Costs 2 Actions)"
"source":
  - "MOT"
"image": "/Compendium/bestiary/monstrosity/token/fleecemane-lion-mot.webp"
```
^statblock
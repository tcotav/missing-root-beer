# Map Design Templates
## "The Case of the Missing Root Beer"

Detailed layouts and design specifications for each game map.

## Map 001: Blue's House Interior

### Layout (17x13 tiles)
```
###################
#                 #
#  [TV]    [Owl]  #
#  [🛋️]           #
#                 #
#     [Table]     #
#                 #
#  [Fridge] [Stove]#
#                 #
#     [Bed]       #
#                 #
#        [🚪]       #
###################
```

### Interactive Objects
- **Refrigerator** (8,7): Main quest trigger - "The root beer was here!"
- **TV** (3,2): "The news is talking about Miskko Corp again..."
- **Bed** (7,9): "I'm too worried about my root beer to sleep."
- **Couch** (3,3): "Pudding usually sits here with me."
- **Table** (7,5): "Crumbs... Pudding was eating here recently."
- **Door** (8,11): Transfer to Overworld Map

### Events
1. **Game Start** (Autorun, center of room)
2. **Tutorial Trigger** (Action on refrigerator)
3. **Clue Hints** (Various furniture interactions)
4. **Map Transfer** (Door to overworld)

### Atmosphere
- **BGM**: Peaceful home theme (slightly melancholy)
- **Lighting**: Warm interior lighting
- **Color Scheme**: Blue/teal accents to match Blue's character

## Map 002: Neighborhood Overworld

### Layout (30x20 tiles)
```
################################
#                              #
# [Tree] [Tree]    [MISKKO HQ] #
#                    [🏢🏢🏢]   #
#     [Park]                   #
#      [🌳]         [Path]     #
#                              #
#  [Blue's]         [Path]     #
#  [House]                     #
#   [🏠]           [Flowers]    #
#                              #
#         [Path Path Path]     #
#                              #
# [Tree]              [Tree]   #
#                              #
################################
```

### Key Locations
- **Blue's House** (6,8): Entry point, player's home base
- **Miskko HQ** (25,3): Locked initially, main dungeon entrance
- **Park Area** (8,5): Optional exploration, hidden items
- **Connecting Paths**: Guide player movement between areas

### Interactive Elements
- **House Entrance**: Transfer to Blue's House
- **Miskko HQ Doors**: "Locked. Employees only." (until quest progresses)
- **Park Bench**: Rest spot, save point
- **Trees/Flowers**: Flavor text, possible hidden items
- **Random NPCs**: Neighborhood residents with hints

### Hidden Elements
- **Secret Path** behind trees leading to bonus area
- **Clue Item** hidden near Miskko HQ (footprints)
- **Easter Egg** references in background details

## Map 003: Miskko HQ Lobby

### Layout (20x15 tiles)
```
####################
#                  #
# [Plant] [Plant]  #
#                  #
# [Receptionist]   #
# [Desk]     [🪑]  #
#                  #
#     [Elevator]   #
#        [⬆️]      #
#                  #
#  [🪑][🪑] [🪑][🪑] #
#                  #
#       [🚪🚪]       #
####################
```

### Interactive Elements
- **Receptionist Desk**: Main NPC interaction point
- **Elevator**: Locked until player gains access
- **Waiting Chairs**: Flavor interactions
- **Corporate Art**: Environmental storytelling
- **Entry Doors**: Transfer back to overworld

### NPCs
- **Receptionist**: Key character for accessing upper floors
  - Initial: "Do you have an appointment?"
  - After quest progress: "Oh! You're here about the missing items?"

### Corporate Atmosphere
- **BGM**: Mysterious/corporate music
- **Lighting**: Fluorescent, sterile lighting
- **Color Scheme**: Grays and blues, impersonal corporate feel

## Map Design Principles

### Navigation Flow
1. **Blue's House** → **Overworld** → **Miskko HQ**
2. Clear paths guide player between important locations
3. Optional areas reward exploration without blocking progress

### Interactive Density
- **High**: Blue's House (tutorial area, many interactions)
- **Medium**: Overworld (some NPCs and secrets)
- **Focused**: Miskko HQ Lobby (key story interactions)

### Visual Consistency
- **Indoor Maps**: Use Interior tilesets with warm/cool lighting
- **Outdoor Maps**: Use Exterior tilesets with natural elements
- **Corporate Areas**: Modern, sterile appearance

## Implementation Notes

### Tileset Requirements
- **Interior A**: Blue's house furniture and fixtures
- **Exterior A**: Neighborhood buildings, trees, paths
- **Interior B**: Modern office furniture and corporate decor

### Transfer Events
All map connections should include:
- Fade out/in transitions
- Position player appropriately on destination map
- Update BGM if changing areas
- Trigger any area-specific events

### Save Points
- **Blue's House**: Bed interaction
- **Overworld**: Park bench
- **Miskko HQ**: Lobby seating area

This map structure provides a focused but expandable game world that supports the mystery storyline while teaching fundamental RPG Maker concepts.
# The Case of the Missing Root Beer - RPG Technical Guide

A 2D RPG mystery/adventure game created with RPG Maker, featuring Blue Planet Six exploring the world to find his missing root beer and raccoon friend.

## Overview

"The Case of the Missing Root Beer" is an exploration-based RPG where players guide Blue Planet Six through various locations, interact with NPCs, solve puzzles, and uncover the mystery behind his missing root beer and friend Pudding. The game combines classic RPG mechanics with comedy and mystery storytelling.

The game features:
- Exploration-based gameplay with multiple connected areas
- Quest system with main storyline and optional side content
- Character companion system (Owl as permanent party member)
- Interactive investigation mechanics with item collection
- Multiple story endings based on player choices and exploration
- Character relationship tracking affecting dialogue and outcomes

## Characters

- **Blue Planet Six**: The protagonist - a one-foot-tall blue alien explorer
- **Owl**: Blue's companion and best friend, follows the player throughout the game
- **Pudding**: A missing raccoon friend who becomes central to the mystery
- **Miskers**: The antagonist raccoon CEO running the Miskko corporation
- **Scrappy Blue**: Blue's annoying nephew and the actual culprit

## Game Structure

### Maps & Areas
- **Overworld**: Blue's neighborhood connecting all major locations
- **Blue's House**: Starting area with tutorial elements and story setup
- **Miskko HQ**: Multi-floor dungeon with investigation events and puzzles
- **Additional Locations**: Expandable areas for side quests and character development

### Core Mechanics
- **Movement**: Standard RPG movement with Owl companion following
- **Interaction System**: Examine events for clues, talk events for NPCs
- **Quest System**: Main quest "Find the Missing Root Beer" with branching objectives
- **Inventory**: Item collection system for clues, keys, and story items
- **Relationship Tracking**: Variables track player choices affecting NPC reactions

## Installation & Setup

1. Install [RPG Maker MZ](https://www.rpgmakerweb.com/products/rpg-maker-mz) (recommended) or [RPG Maker MV](https://www.rpgmakerweb.com/products/rpg-maker-mv)
2. Clone or download this repository
3. Open the project folder in RPG Maker
4. Use "Test Play" to run the game during development
5. Follow the [Learning Plan](LearningPlan.md) for structured development

## Development Structure

### Required Assets
- **Character Sprites**: 4-direction walking animations for Blue, Owl, and NPCs
- **Tilesets**: Custom tilesets for house interior, office buildings, and outdoor areas  
- **Item Icons**: Root beer bottle, clues, keys, and other inventory items
- **Audio**: Background music for different areas and sound effects for interactions

### Event System
- **Story Events**: Trigger main plot progression and dialogue
- **Investigation Events**: Allow players to examine clues and gather information
- **NPC Events**: Handle character interactions and relationship tracking
- **Transfer Events**: Connect different maps and areas

### Variables & Switches
- **Story Progress**: Track main quest completion and available areas
- **Relationship Values**: Monitor player relationships with different characters
- **Item Flags**: Control availability of clues and story items
- **Ending Flags**: Determine which ending the player will see

## Expanding the Game

The RPG structure allows for easy expansion:
- **New Areas**: Create additional maps and connect them to the overworld
- **Side Quests**: Add optional NPCs with their own storylines
- **Character Development**: Expand companion interactions and party members
- **Puzzle Mechanics**: Implement more complex investigation and logic puzzles

## Technical Considerations

### Performance
- Keep map sizes reasonable (50x50 tiles maximum recommended)
- Optimize event placement to avoid unnecessary processing
- Use appropriate image formats and sizes for assets

### Compatibility
- Test on multiple screen sizes and resolutions
- Ensure keyboard and gamepad controls work properly
- Verify save/load functionality across different areas

## Credits

- Story & Game Design: [Your Name]
- RPG Development: [Your Name]
- Asset Creation: [Your Name]
- [Add other credits as needed]

## License

This project is intended for educational use. Feel free to use it as a learning resource or starting point for your own RPG Maker games.
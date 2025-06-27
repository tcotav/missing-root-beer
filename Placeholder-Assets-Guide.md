# Placeholder Assets Creation Guide
## Quick Start Graphics for Development

This guide helps create simple placeholder graphics so students can start developing immediately while learning to create better assets later.

## Overview

**Purpose**: Get the game running quickly with basic graphics that can be replaced later  
**Time Required**: 30-60 minutes to create all placeholders  
**Tools Needed**: Any simple drawing program (even MS Paint works!)

## Blue Planet Six - Main Character Placeholder

### Quick Method (5 minutes)
**Use RPG Maker's built-in character editor:**
1. **Open RPG Maker MZ Character Generator** (Tools menu)
2. **Create a simple character**:
   - Body: Human, Male
   - Skin: Change to bright blue color
   - Hair: Simple style, darker blue
   - Clothes: Basic shirt/pants
3. **Export as**: `blue_placeholder.png`
4. **Use this temporarily** until custom sprite is ready

### DIY Method (15 minutes)
**Create a simple blue character:**
1. **Open any drawing program**
2. **Create 144x192 pixel canvas**
3. **Draw a simple blue stick figure** in each of the 12 positions:
   - 3 frames × 4 directions = 12 total frames
   - Each frame: 48x48 pixels
4. **Use bright blue (#4A90E2) for the body**
5. **Add simple black dots for eyes**
6. **Save as PNG with transparency**

### Super Simple Method (2 minutes)
**Recolor existing sprite:**
1. **Copy a default RPG Maker character file**
2. **Open in any image editor**
3. **Use "Replace Color" or "Colorize" to make it blue**
4. **Save as `blue_simple.png`**

## Owl Companion Placeholder

### Quick Options
1. **Use a default animal sprite** from RPG Maker resources
2. **Recolor a bird sprite** to brown/white
3. **Draw a simple brown oval with wings** (very basic but functional)

### Simple Drawing Method
- **Body**: Brown oval shape
- **Wings**: Two brown triangles on sides
- **Eyes**: Large yellow circles with black dots
- **Beak**: Small orange triangle
- **Size**: Same as Blue (48x48 per frame)

## Environment Placeholders

### Tileset Modifications
**Instead of creating new tilesets:**
1. **Use default Interior/Exterior tilesets**
2. **Focus on layout rather than custom graphics**
3. **Add variety through creative tile combinations**

### Key Objects
**For special story items, create simple icons:**
- **Root Beer Bottle**: Brown rectangle with label
- **Clue Items**: Simple geometric shapes with colors
- **Corporate Logo**: Basic "M" for Miskko

## UI Element Placeholders

### Annoyance Meter
**Simple bar graphic:**
```
[████████__] - High annoyance (red)
[█████_____] - Medium annoyance (yellow)  
[██________] - Low annoyance (green)
```

### Menu Customization
**Quick color changes:**
1. **Open System settings in Database**
2. **Change window colors** to blue theme
3. **Modify text colors** to match Blue's character

## Asset Organization

### File Structure
```
img/
├── characters/
│   ├── blue_placeholder.png
│   ├── owl_simple.png
│   └── npcs_basic.png
├── system/
│   ├── annoyance_meter.png
│   └── ui_elements.png
└── pictures/
    ├── miskko_logo.png
    └── story_images.png
```

## Quality Standards for Placeholders

### "Good Enough" Criteria
- **Recognizable**: Player can tell what it's supposed to be
- **Consistent**: All placeholders match in style/quality
- **Functional**: Works properly in the game engine
- **Temporary**: Clearly marked as placeholders to be replaced

### Don't Worry About
- **Perfect art**: These are temporary
- **Complex animations**: Simple is fine
- **Professional polish**: Focus on functionality
- **Detailed features**: Basic shapes work great

## Implementation Tips

### RPG Maker Setup
1. **Place placeholder files** in correct img/ folders
2. **Test each graphic** by using it in-game
3. **Take screenshots** to track what needs replacement
4. **Keep a list** of placeholders to upgrade later

### Version Control
**Create a "placeholder log":**
- List what each placeholder represents
- Note which ones work well vs. need priority replacement
- Track student feedback on what's confusing

## Student Instructions

### Day 1 Approach
**Tell students:**
1. **"These graphics are temporary"** - sets expectations
2. **"Focus on making the game work first"** - priorities
3. **"We'll make it beautiful later"** - reassurance
4. **"Your game logic is more important than art right now"**

### Placeholder Replacement Schedule
- **Week 1-2**: Use all placeholders, focus on functionality
- **Week 3**: Start replacing main character graphics
- **Week 4-5**: Replace environment and UI elements  
- **Week 6**: Final art polish and custom graphics

## Benefits of This Approach

### For Learning
- **Immediate gratification**: Game works right away
- **Reduced overwhelm**: Don't need art skills immediately
- **Clear progression**: Can see improvement over time
- **Focus on code**: Learn game logic without art distractions

### For Development
- **Rapid prototyping**: Test ideas quickly
- **Modular replacement**: Swap graphics as needed
- **Iterative improvement**: Build quality gradually
- **Risk reduction**: Game works even if art isn't perfect

## Common Placeholder Mistakes to Avoid

### Don't
- **Spend too much time** making placeholders perfect
- **Use copyrighted images** from other games
- **Make placeholders too complex** (defeats the purpose)
- **Forget to label them** as temporary

### Do
- **Keep them simple and functional**
- **Use consistent sizing/style**
- **Test them in actual gameplay**
- **Plan for easy replacement later**

This placeholder approach gets students building and playing their game immediately while they learn to create better assets throughout the learning plan.
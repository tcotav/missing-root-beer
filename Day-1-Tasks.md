# Day 1 Tasks - Project Setup
## "The Case of the Missing Root Beer"

**Welcome to Day 1!** Today you'll set up your RPG Maker project and get familiar with the basics.

## Today's Goals ✨
By the end of today, you'll have:
- ✅ A working RPG Maker project
- ✅ Your main character (Blue) set up  
- ✅ The basic house map created
- ✅ Your first interactive event working

**Estimated Time**: 2-3 hours (take breaks!)

## Task 1: RPG Maker Setup (30 minutes)

### Get RPG Maker Running
1. **Launch RPG Maker MZ** (or MV if that's what you have)
2. **Click "Create New Project"**
3. **Fill in the details**:
   - Project Title: `The Case of the Missing Root Beer`
   - Folder: Choose somewhere easy to find
   - Resources: Use Default Resources
4. **Click OK** and wait for project creation

### Test Your Setup
1. **Click the green "Test Play" button**
2. **You should see**: A game window with a character you can move around
3. **Try moving**: Use arrow keys to walk around
4. **Close the test**: Alt+F4 or close window
5. **Success!** You have a working RPG Maker project

## Task 2: Character Setup (45 minutes)

### Open the Database
1. **Press F9** or click the "Database" button
2. **Go to the "Actors" tab** (should be selected by default)
3. **Click on "Actor001"** (Harold by default)

### Create Blue Planet Six
1. **Change the name**: 
   - Name: `Blue Planet Six`
   - Nickname: `Blue`
2. **Character settings**:
   - Class: `Hero` (we'll change this later)
   - Initial Level: `1`
   - EXP: `0`
3. **For now, leave the graphics as default** (we'll change this on Day 3)
4. **Click "OK"** to save changes

### Test Your Character
1. **Test Play** your game again
2. **The character should now be named "Blue Planet Six"**
3. **Check the menu**: Press X or Escape to see your character's stats

## Task 3: Create Blue's House Map (60 minutes)

### Map Properties Setup
1. **In the main editor, right-click "MAP001"**
2. **Choose "Map Properties"**
3. **Change settings**:
   - Display Name: `Blue's House`
   - Width: `17`
   - Height: `13`
   - Tileset: `Interior_A`
4. **Click OK**

### Build the Basic House Layout
**Use the Map-Design-Templates.md file as your guide!**

#### Step-by-Step Building
1. **Select the floor tile** from the tileset (usually top-left)
2. **Hold right-click and drag** to fill the entire map with floor
3. **Select wall tiles** and create the room borders
4. **Add furniture**:
   - Refrigerator (important for the story!)
   - Bed
   - Table/Couch
   - TV
5. **Don't worry about making it perfect** - you can always improve it later!

### Quick Building Tips
- **Right-click drag**: Fills areas quickly
- **Left-click**: Places single tiles
- **Shift+click**: Rectangle selection
- **Use different layers**: Ground → Decorations → Events

## Task 4: Your First Event (45 minutes)

### Create the Refrigerator Event
This is where the main story begins!

1. **Right-click on your refrigerator tile**
2. **Choose "New Event"**
3. **Set up the event**:
   - Name: `Refrigerator`
   - Trigger: `Action Button`
   - Priority: `Same as Characters`

### Add the Dialogue
**Copy this exactly into your event**:

```
◆Show Text: Blue Planet Six
: This is where I kept my special root beer...
: It was RIGHT HERE this morning!
◆Show Text: Blue Planet Six  
: I can't believe someone would steal it!
◆Show Text: System
: This is where your adventure begins!
: Try examining other objects in the house.
```

### How to Add Show Text Commands
1. **Double-click the event to edit**
2. **In the "Contents" area, double-click the empty space**
3. **Choose "Show Text" from the list**
4. **Type your dialogue**
5. **Change the name/face if needed**
6. **Click OK to add the command**

### Test Your Event
1. **Save your project** (Ctrl+S)
2. **Test Play**
3. **Walk up to the refrigerator and press Enter/Space**
4. **You should see the dialogue appear!**

## Task 5: Exploration and Learning (30 minutes)

### Try These Things
1. **Add another simple event** (maybe the TV or bed)
2. **Experiment with different tiles** for decorating
3. **Move your character's starting position** (Player Properties)
4. **Try the different tabs in the Database** (just look around)

### Create a Simple TV Event
1. **Right-click on your TV**
2. **New Event**: Name it "TV"  
3. **Add this text**:
```
◆Show Text: Blue Planet Six
: The news is on... nothing interesting today.
: Wait, is that a Miskko Corporation commercial?
```

## Success Checklist ✅

Before you finish Day 1, make sure you have:
- [ ] RPG Maker project created and named correctly
- [ ] Main character renamed to "Blue Planet Six"
- [ ] House map created with basic furniture
- [ ] Refrigerator event working with dialogue
- [ ] At least one other interactive object (TV, bed, etc.)
- [ ] Saved your project (very important!)

## If You Get Stuck 🆘

### Common Issues
- **Can't find the Database**: Press F9 or look for "Database" button
- **Events don't work**: Make sure Trigger is set to "Action Button"
- **Text doesn't show**: Check that you're using "Show Text" command
- **Map looks weird**: Try switching between different layer tabs

### Getting Help
- **Read the LLM-Assistant-Guide.md** for how to ask AI for help
- **Press F1** in RPG Maker for built-in help
- **Take screenshots** of problems to show others

### Sample Questions for AI
- "My event isn't working when I press Enter, what might be wrong?"
- "How do I change the name of my map in RPG Maker MZ?"
- "I can't find the Show Text command, where is it?"

## What's Next? 🚀

### Tomorrow (Day 2)
- Learn more about the map editor
- Add more rooms or areas to your house
- Start understanding events and switches

### This Week
- Create your character sprite (Day 3)
- Build the overworld map (Day 4)
- Set up the quest system (Day 5)

## Celebration Time! 🎉

**Congratulations!** You've taken your first major step into game development. You now have:
- A working RPG project
- A character with a story
- An interactive world you created
- The foundation for an amazing game

**Take a break, show someone what you've built, and get excited for tomorrow!**

---

**Day 1 Complete!** 
Save your project and get ready for Day 2 where we'll expand your world and add more interactive elements.
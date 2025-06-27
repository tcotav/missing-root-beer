# Character Sprite Specifications
## "The Case of the Missing Root Beer"

Detailed specifications for creating character sprites in RPG Maker format.

## Blue Planet Six - Main Character

### Basic Specifications
- **File Format**: PNG with transparent background
- **Sprite Sheet Size**: 144x192 pixels (RPG Maker MZ standard)
- **Individual Sprite Size**: 48x48 pixels per frame
- **Animation Frames**: 3 frames per direction (idle, step1, step2)
- **Directions**: 4 (Down, Left, Right, Up)

### Character Design
- **Height**: Small (about 1 foot tall as described in story)
- **Color**: Bright blue humanoid
- **Body**: Simple, cartoon-like design
- **Eyes**: Large, expressive (main feature for emotion)
- **Clothing**: Simple outfit, possibly space-themed

### Sprite Sheet Layout
```
[Down1][Down2][Down3]
[Left1][Left2][Left3]
[Right1][Right2][Right3]
[Up1][Up2][Up3]
```

### Expression Variations
Create additional sprite sheets for different moods:
- **Normal** (blue_normal.png): Standard expression
- **Annoyed** (blue_annoyed.png): Slightly irritated look
- **Angry** (blue_angry.png): Very upset, for high annoyance moments

### Color Palette
- **Primary Blue**: #4A90E2 (bright, friendly blue)
- **Highlight Blue**: #7BB3F0 (lighter accent)
- **Shadow Blue**: #2E5B8F (darker shading)
- **Eyes**: #FFFFFF (white) with #000000 (black pupils)
- **Mouth**: #333333 (dark gray for simple line)

## Owl - Companion Character

### Basic Specifications
- **File Format**: PNG with transparent background
- **Sprite Sheet Size**: 144x192 pixels
- **Individual Sprite Size**: 48x48 pixels per frame
- **Animation**: 3 frames per direction
- **Special**: Should appear to "follow" rather than walk

### Character Design
- **Species**: Wise-looking owl
- **Colors**: Brown and white natural owl colors
- **Size**: Medium (larger than Blue but not huge)
- **Features**: Large eyes, scholarly appearance
- **Posture**: Upright, dignified

### Animation Style
- **Down**: Facing forward, slight head bobbing
- **Left/Right**: Side profile, wing movement
- **Up**: Back view, tail feathers visible
- **Special**: Consider "hopping" animation instead of walking

### Color Palette
- **Primary Brown**: #8B4513 (saddle brown)
- **Light Brown**: #CD853F (peru brown for highlights)
- **White**: #F5F5DC (beige-white for chest/face)
- **Eyes**: #FFD700 (golden yellow, typical for owls)
- **Beak**: #FF8C00 (dark orange)

## Supporting NPCs

### Receptionist (Miskko HQ)
- **Style**: Professional business attire
- **Colors**: Corporate grays and blues
- **Animation**: Minimal (desk worker, mostly stationary)
- **Size**: Standard RPG Maker character size

### Pudding (Raccoon Friend)
- **Style**: Friendly cartoon raccoon
- **Colors**: Gray with black mask markings
- **Size**: Similar to Blue (small, cute)
- **Note**: Will appear in later story sections

### Miskers (Corporate Raccoon CEO)
- **Style**: Business suit, villainous appearance
- **Colors**: Dark grays with red accents (tie, eyes)
- **Size**: Larger than other characters (intimidating)
- **Features**: Sharp, corporate look

### Scrappy Blue (Annoying Nephew)
- **Style**: Smaller version of Blue
- **Colors**: Similar blue but more muted/pale
- **Size**: Even smaller than Blue
- **Features**: Mischievous expression, less mature design

## Sprite Creation Tips

### For Beginners
1. **Start Simple**: Use basic shapes and minimal details
2. **Consistent Style**: Keep all characters in the same art style
3. **Clear Silhouettes**: Characters should be recognizable by outline alone
4. **Readable at Small Size**: Details should be visible when displayed small

### Technical Requirements
- **Transparency**: Use PNG format with transparent backgrounds
- **Grid Alignment**: Each frame should align to the 48x48 pixel grid
- **Center Registration**: Character should be centered in each frame
- **Consistent Sizing**: All characters should use similar proportions

### Animation Guidelines
- **Frame 1**: Idle pose (both feet on ground)
- **Frame 2**: Mid-step (one foot forward)
- **Frame 3**: Idle pose again (maintains walk cycle)
- **Timing**: Each frame displays for about 15-20 game frames

## Asset Organization

### File Structure
```
img/characters/
├── blue_normal.png      (Main character sprite)
├── blue_annoyed.png     (Annoyed expression variant)
├── blue_angry.png       (Angry expression variant)
├── owl_companion.png    (Owl companion sprite)
├── receptionist.png     (Miskko HQ receptionist)
├── pudding.png          (Raccoon friend - for later)
├── miskers.png          (Corporate villain - for later)
└── scrappy_blue.png     (Annoying nephew - for later)
```

### Face Graphics
Create matching face portraits (144x144 pixels):
```
img/faces/
├── blue_faces.png       (Multiple expressions on one sheet)
├── owl_faces.png        (Owl portrait variations)
├── receptionist_face.png
└── [others as needed]
```

## Placeholder Solutions

### For Initial Development
If custom sprites aren't ready immediately:
1. **Use RPG Maker defaults** temporarily
2. **Modify existing sprites** by changing colors
3. **Start with simple geometric shapes** 
4. **Focus on getting gameplay working** first

### Quick Sprite Creation
- **Blue**: Recolor a default character to bright blue
- **Owl**: Use animal sprite from RPG Maker resources
- **Others**: Modify existing characters with different clothes/colors

This approach allows development to continue while custom art is being created, following the learning plan's progression from basic functionality to polished assets.
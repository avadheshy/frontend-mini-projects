# CSS Notes 🎨

---

## Selectors & Specificity

```css
*           { }  /* Universal — lowest priority */
div         { }  /* Element */
.classname  { }  /* Class */
#idname     { }  /* ID — higher priority */
div p       { }  /* Descendant */
div > p     { }  /* Direct child */
div + p     { }  /* Adjacent sibling (immediately after) */
div ~ p     { }  /* General sibling (any after) */
[type="text"] { } /* Attribute selector */
```

**Specificity order (low → high):**
`* → element → class → ID → inline style → !important`

---

## Display Property

Controls how an element is rendered in the layout:

```css
display: block;        /* full width, starts new line (default for div, p, h1) */
display: inline;       /* only as wide as content, no width/height (default for span, a) */
display: inline-block; /* inline position BUT respects width/height/padding */
display: none;         /* removes element from layout (invisible + no space) */
display: flex;         /* flex container */
display: grid;         /* grid container */
```

**`display: none` vs `visibility: hidden`:**
- `display: none` → element is gone, no space taken
- `visibility: hidden` → element is invisible but **still occupies space**

```css
/* Useful: center a block element horizontally */
.box {
  display: block;
  width: 300px;
  margin: 0 auto;
}
```

---

## Box Model

Every element is a box:

```
┌─────────────────────────┐
│         Margin          │
│  ┌───────────────────┐  │
│  │      Border       │  │
│  │  ┌─────────────┐  │  │
│  │  │   Padding   │  │  │
│  │  │  ┌───────┐  │  │  │
│  │  │  │Content│  │  │  │
│  │  │  └───────┘  │  │  │
│  │  └─────────────┘  │  │
│  └───────────────────┘  │
└─────────────────────────┘
```

```css
box-sizing: border-box; /* padding+border included in width — use this always */
```

---

## Colors

```css
color: red;                   /* named */
color: #ff5733;               /* hex */
color: rgb(255, 87, 51);      /* rgb */
color: rgba(255, 87, 51, 0.5); /* rgba — 4th param = opacity */
color: hsl(14, 100%, 60%);    /* hsl */
```

---

## Units

| Unit | What it is |
|------|-----------|
| `px` | Fixed pixels |
| `%` | Relative to **parent** element |
| `em` | Relative to **current** element's font-size |
| `rem` | Relative to **root** (`html`) font-size |
| `vw` | 1% of **viewport width** |
| `vh` | 1% of **viewport height** |

**`1%` vs `1vw`:**
- `1%` → 1% of the *parent container's* width
- `1vw` → 1% of the *browser window's* width (always)

---

## Gradients

```css
/* Linear */
background: linear-gradient(to right, red, blue);
background: linear-gradient(45deg, red, yellow, blue);

/* Radial (circular) */
background: radial-gradient(circle, red, blue);

/* Conic (pie chart style) */
background: conic-gradient(red 0deg, blue 180deg, green 360deg);
```

---

## Shadows

```css
/* Text shadow: x y blur color */
text-shadow: 2px 2px 4px rgba(0,0,0,0.5);

/* Box shadow: x y blur spread color */
box-shadow: 4px 4px 10px 2px rgba(0,0,0,0.3);
box-shadow: inset 0 0 10px gray; /* inset = inside */
```

---

## Pseudo-classes

Style elements based on their **state** or **position**:

```css
/* State */
a:hover   { color: red; }         /* mouse over */
a:active  { color: blue; }        /* being clicked */
input:focus { outline: 2px solid blue; } /* focused */
input:disabled { opacity: 0.5; }
input:checked  { accent-color: green; }

/* Position */
li:first-child  { font-weight: bold; }
li:last-child   { border: none; }
li:nth-child(2) { background: lightgray; }
li:nth-child(odd)  { background: #f5f5f5; }
li:nth-child(even) { background: white; }

/* Negation */
p:not(.special) { color: gray; }

/* Combined with elements */
.card:hover { box-shadow: 0 4px 20px rgba(0,0,0,0.2); }
```

---

## Typography

```css
/* Font */
font-family: "Inter", Arial, sans-serif; /* fallback chain */
font-size: 16px;
font-weight: 400;   /* 100–900, or normal/bold */
font-style: italic;
font-variant: small-caps;

/* Spacing */
line-height: 1.6;       /* 1.5–1.8 is readable for body text */
letter-spacing: 0.05em;
word-spacing: 4px;

/* Text */
text-align: left | center | right | justify;
text-decoration: none | underline | line-through | overline;
text-transform: uppercase | lowercase | capitalize;
text-indent: 2em;      /* indent first line */

/* Overflow */
white-space: nowrap;
overflow: hidden;
text-overflow: ellipsis; /* "Hello Wor..." truncation */

/* Multi-line clamp */
display: -webkit-box;
-webkit-line-clamp: 3;
-webkit-box-orient: vertical;
overflow: hidden;
```

---

## z-index & Stacking Context

`z-index` controls which element appears **on top** when elements overlap.

```css
/* Only works on positioned elements (not static) */
.modal   { position: fixed;    z-index: 1000; }
.overlay { position: absolute; z-index: 999; }
.card    { position: relative; z-index: 1; }

/* Higher z-index = on top */
/* Elements with same z-index: later in HTML = on top */
```

> A new stacking context is created when `position` + `z-index`, `opacity < 1`, `transform`, or `filter` are applied. Children can't escape their parent's stacking context.

---

## Border & Border-radius

```css
border: 1px solid #ccc;             /* shorthand: width style color */
border-top: 2px dashed red;
border-radius: 8px;                 /* all corners */
border-radius: 50%;                 /* circle (on square element) */
border-radius: 10px 20px 10px 20px; /* top-left top-right bottom-right bottom-left */

outline: 2px solid blue;            /* like border but outside, doesn't affect layout */
outline-offset: 4px;
```

---

## object-fit & object-position

Controls how `<img>` or `<video>` fits inside its container (like `background-size` but for content elements):

```css
img {
  width: 300px;
  height: 200px;
  object-fit: cover;    /* fill container, crop overflow (most common) */
  object-fit: contain;  /* fit inside, letterbox */
  object-fit: fill;     /* stretch to fit (distorts) */

  object-position: center;   /* where to anchor the image */
  object-position: top left;
}
```

---

## Media Queries (Responsive Design)

Apply CSS only when the screen matches a condition:

```css
/* Mobile-first approach (recommended) */
/* Base styles = mobile */
.container { width: 100%; }

/* Tablet and up */
@media (min-width: 768px) {
  .container { width: 720px; }
}

/* Desktop and up */
@media (min-width: 1024px) {
  .container { width: 960px; }
}

/* Large screens */
@media (min-width: 1280px) {
  .container { width: 1200px; }
}

/* Common breakpoints (Tailwind-style) */
/* sm: 640px  md: 768px  lg: 1024px  xl: 1280px */

/* Other conditions */
@media (max-width: 600px) { }       /* only small screens */
@media (orientation: landscape) { } /* landscape mode */
@media print { }                    /* print styles */

/* Example: stack columns on mobile */
.grid { display: grid; grid-template-columns: 1fr 1fr; }

@media (max-width: 768px) {
  .grid { grid-template-columns: 1fr; }
}
```

---

## Dimensions & Overflow

```css
width: 300px;
height: 200px;
min-width: 100px;  max-width: 600px;
min-height: 50px;  max-height: 400px;

overflow: visible; /* default, content spills out */
overflow: hidden;  /* clips overflow */
overflow: scroll;  /* always shows scrollbar */
overflow: auto;    /* scrollbar only when needed */
```

---

## Position

```css
position: static;    /* default, normal flow */
position: relative;  /* offset from its normal position */
position: absolute;  /* removed from flow, positioned to nearest relative parent */
position: fixed;     /* stays fixed to viewport (doesn't scroll) */
position: sticky;    /* relative until scroll threshold, then fixed */
```

**`background-attachment: fixed` vs `position: fixed`:**
- `background-attachment: fixed` → background image doesn't scroll (parallax effect)
- `position: fixed` → the *entire element* is fixed to the screen

---

## 2D Transforms

```css
transform: translateX(50px);        /* move */
transform: translateY(-20px);
transform: translate(50px, -20px);  /* move x & y */
transform: scale(1.5);              /* scale up 150% */
transform: rotate(45deg);           /* rotate */
transform: skewX(20deg);            /* skew */
/* Multiple transforms */
transform: translate(50px) rotate(45deg) scale(1.2);
```

## 3D Transforms

```css
perspective: 500px; /* set on parent */
transform: rotateX(45deg);
transform: rotateY(45deg);
transform: translateZ(100px);
transform: rotate3d(1, 1, 0, 45deg);
```

---

## Flexbox

### Container Properties
```css
display: flex;

flex-direction: row | row-reverse | column | column-reverse;
flex-wrap: nowrap | wrap | wrap-reverse;
flex-flow: row wrap; /* shorthand for direction + wrap */

justify-content: flex-start | flex-end | center | space-between | space-around | space-evenly;
align-items: stretch | flex-start | flex-end | center | baseline;
align-content: flex-start | center | space-between; /* multi-line alignment */
gap: 10px;
```

### Item Properties
```css
order: 2;           /* change visual order */
flex-grow: 1;       /* how much to grow */
flex-shrink: 1;     /* how much to shrink */
flex-basis: 200px;  /* initial size before grow/shrink */
flex: 1 1 200px;    /* shorthand: grow shrink basis */
align-self: center; /* override align-items for this item */
```

**`flex-basis` vs `width`:**
- `flex-basis` sets size *along the main axis* (respects flex context)
- `width` is absolute; `flex-basis` works with `flex-grow`/`flex-shrink`

**`<img>` vs `background-image`:**
- `<img>` → content image (semantic, accessible, in HTML)
- `background-image` → decorative image (in CSS, can't add alt text)

---

## Grid

### Container Basics
```css
display: grid;
grid-template-columns: 200px 200px 200px;    /* 3 cols */
grid-template-columns: repeat(3, 1fr);       /* 3 equal cols */
grid-template-rows: 100px auto;
gap: 10px;          /* shorthand for row-gap + column-gap */
```

### Advanced Grid
```css
grid-template-columns: repeat(3, minmax(100px, 1fr)); /* min/max size */
grid-auto-rows: 150px;   /* auto-generated row height */

/* fr unit = fraction of available space */
grid-template-columns: 1fr 2fr 1fr; /* 25% 50% 25% */
```

### Placing Items
```css
/* By line numbers */
grid-column: 1 / 3;  /* start line 1, end line 3 */
grid-row: 1 / 2;

/* Named areas */
grid-template-areas:
  "header header"
  "sidebar main"
  "footer footer";

.header  { grid-area: header; }
.sidebar { grid-area: sidebar; }
```

### Alignment
```css
/* Container */
justify-content: center;   /* horizontal alignment of grid */
align-content: center;     /* vertical alignment of grid */
justify-items: center;     /* horizontal align all cells */
align-items: center;       /* vertical align all cells */
place-items: center;       /* shorthand align-items + justify-items */

/* Item */
justify-self: end;
align-self: start;
place-self: center;
```

**`grid` vs `inline-grid`:**
- `grid` → block-level grid (takes full width)
- `inline-grid` → inline-level grid (only as wide as content)

---

## Useful Functions

```css
width: calc(100% - 40px);       /* math */
width: min(500px, 100%);        /* smaller of the two */
width: max(200px, 50%);         /* larger of the two */
width: clamp(200px, 50%, 800px); /* min, preferred, max */
```

---

## `::before` and `::after`

```css
/* Pseudo-elements — inject content without HTML */
.button::before {
  content: "→ ";   /* required, can be empty "" */
  color: red;
}
.card::after {
  content: "";
  display: block;
  height: 2px;
  background: blue;
}
```

---

## CSS Variables

```css
/* Global (on :root) */
:root {
  --primary-color: #3498db;
  --font-size: 16px;
}

/* Local (on element) */
.card {
  --card-padding: 20px;
  padding: var(--card-padding);
}

/* Usage */
color: var(--primary-color);
font-size: var(--font-size);
```

**`:root` vs `*` (universal selector):**
- `:root` targets the `<html>` element → highest specificity for variables
- `*` targets every element → lower specificity, used for resets

---

## Transitions & Animations

### Transition (simple A→B)
```css
transition: property duration timing-function delay;
transition: background-color 0.3s ease 0s;
transition: all 0.3s ease;

/* Timing functions */
ease | linear | ease-in | ease-out | ease-in-out | cubic-bezier(...)
```

### Animation (keyframe-based)
```css
@keyframes slideIn {
  from { transform: translateX(-100px); opacity: 0; }
  to   { transform: translateX(0);      opacity: 1; }
}

/* Or with percentages */
@keyframes pulse {
  0%   { transform: scale(1); }
  50%  { transform: scale(1.1); }
  100% { transform: scale(1); }
}

.box {
  animation-name: slideIn;
  animation-duration: 0.5s;
  animation-delay: 0.2s;
  animation-timing-function: ease;
  animation-iteration-count: infinite; /* or a number */
  animation-direction: alternate;       /* normal | reverse | alternate */
  animation-fill-mode: forwards;        /* keeps end state */

  /* Shorthand */
  animation: slideIn 0.5s ease 0.2s infinite alternate forwards;
}
```
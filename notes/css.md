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
```

**Specificity order (low → high):**
`* → element → class → ID → inline style → !important`

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

# CSS Position Property

## 1. static
- Default position
- Follows normal document flow
- `top`, `left`, `right`, `bottom`, `z-index` do NOT work

---

## 2. relative
- Stays in normal flow
- Can be moved using `top`, `left`, etc.
- Original space is preserved
- Creates a reference for `absolute` children

---

## 3. absolute
- Removed from normal document flow
- Positioned relative to nearest **positioned ancestor**
  - (`relative`, `absolute`, `fixed`, `sticky`)
- If no positioned parent → relative to viewport
- Can overlap other elements

---

## 4. fixed
- Removed from normal document flow
- Positioned relative to **viewport**
- Does NOT move on scroll
- Always stays in the same place on screen

---

## 5. sticky
- Acts like `relative` initially
- Becomes `fixed` when scroll reaches a threshold
- Requires `top`, `bottom`, `left`, or `right`
- Works only within its parent container

---

# Important Notes

## Positioned Ancestor
- `absolute` looks for nearest parent with:
  - `position: relative | absolute | fixed | sticky`

---

## z-index
- Works only on positioned elements
- Does NOT work with `position: static`

---

## Sticky Limitations
- Needs a value like `top: 0`
- Does NOT work if parent has:
  - `overflow: hidden` or `overflow: auto`

---

## Flow Behavior
- `static` and `relative` → stay in normal flow
- `absolute` and `fixed` → removed from flow
- Removed elements do NOT reserve space

---

# Quick Summary

- static → normal flow  
- relative → move within flow  
- absolute → removed, parent-based  
- fixed → removed, viewport-based  
- sticky → scroll + stick  

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
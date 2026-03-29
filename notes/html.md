# HTML Notes 🌐

---

## What is HTML?
**HyperText Markup Language** — the skeleton of every webpage.
- **HyperText** → links that connect pages
- **Markup** → annotating content with tags
- **Language** → a set of rules/syntax

---

## Tags, Elements & Attributes

### Tag vs Element
```html
<p>Hello</p>
<!-- <p> = opening tag, </p> = closing tag, the whole thing = element -->
```

### Attribute (Property + Value)
```html
<a href="https://google.com" target="_blank">Click</a>
<!-- href = property, "https://google.com" = value -->
```

---

## Block vs Inline Elements

| Block | Inline |
|-------|--------|
| Takes full width, starts on new line | Only takes content width, stays inline |
| `<div>`, `<p>`, `<h1>`, `<ul>`, `<table>` | `<span>`, `<a>`, `<img>`, `<strong>`, `<em>` |

---

## Headings (h1–h6)
Only **6 levels** because they represent a document outline — like chapters → sub-sections → sub-sub-sections. Going deeper loses semantic meaning.

```html
<h1>Main Title</h1>   <!-- Only one per page ideally -->
<h2>Section</h2>
<h3>Sub-section</h3>
<!-- ... up to h6 -->
```

---

## Tables

```html
<table>
  <colgroup>
    <col style="background-color: lightblue"> <!-- style whole column -->
  </colgroup>
  <thead>
    <tr>
      <th>Name</th>   <!-- th = table header -->
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Alice</td>  <!-- td = table data -->
      <td>25</td>
    </tr>
  </tbody>
</table>
```

**Spanning:**
```html
<td colspan="2">Spans 2 columns</td>
<td rowspan="2">Spans 2 rows</td>
```

---

## Quotations & Figures

```html
<!-- Block-level long quote -->
<blockquote cite="https://source.com">
  Long quoted text here...
</blockquote>

<!-- Inline short quote -->
<p>He said <q>Hello world</q></p>

<!-- cite = title of a work -->
<p>From <cite>The Great Gatsby</cite></p>

<!-- Figure with caption -->
<figure>
  <img src="photo.jpg" alt="A photo">
  <figcaption>Photo description</figcaption>
</figure>
```

---

## Anchor Tag Use Cases

```html
<!-- 1. URL -->
<a href="https://google.com" target="_blank">Open Google</a>

<!-- 2. Email -->
<a href="mailto:hello@example.com">Send Email</a>

<!-- 3. Call -->
<a href="tel:+911234567890">Call Us</a>

<!-- 4. Bookmark (same page) -->
<a href="#section1">Go to Section</a>
<div id="section1">Target Section</div>
```

---

## Semantic Tags

Semantic tags tell the browser (and screen readers) **what the content means**.

```html
<header>   <!-- Site/section header, logo, nav -->
<nav>      <!-- Navigation links -->
<main>     <!-- Primary content of the page (only ONE per page) -->
<section>  <!-- A themed grouping of content -->
<article>  <!-- Standalone content (blog post, news) -->
<footer>   <!-- Footer info, links, copyright -->
<aside>    <!-- Sidebar, tangentially related content -->
```

### Common Questions

**`<h1>` vs `<header>`**
- `<h1>` = a text heading (level 1)
- `<header>` = a container for intro content (can contain `<h1>`, logo, nav)

**Can `<article>` go inside `<section>` and vice versa?**
- ✅ Yes, both ways are valid. `<section>` groups related content; `<article>` is self-contained.

**Can `<header>` go inside `<footer>`?**
- Technically valid HTML, but bad practice semantically. Avoid it.

**Can there be multiple `<header>` tags?**
- ✅ Yes! Each `<section>` or `<article>` can have its own `<header>`.

**`<body>` vs `<main>`**
- `<body>` = everything visible on the page
- `<main>` = the **primary** content only (excludes nav, header, footer)

---

## Quick Reference: Common Tags

```html
<!-- Text -->
<p>, <span>, <strong>, <em>, <br>, <hr>

<!-- Lists -->
<ul> <li>Unordered</li> </ul>
<ol> <li>Ordered</li> </ol>

<!-- Media -->
<img src="img.jpg" alt="description">
<video src="vid.mp4" controls></video>

<!-- Form -->
<form action="/submit" method="POST">
  <input type="text" name="username" placeholder="Enter name">
  <input type="submit" value="Submit">
</form>

<!-- Div & Span (non-semantic containers) -->
<div>block container</div>
<span>inline container</span>
```

---

## `<head>` & Meta Tags

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">                              <!-- character encoding -->
  <meta name="viewport" content="width=device-width, initial-scale=1.0"> <!-- responsive! -->
  <meta name="description" content="Page description for SEO">
  <title>Page Title</title>

  <link rel="stylesheet" href="style.css">           <!-- CSS file -->
  <link rel="icon" href="favicon.ico">               <!-- browser tab icon -->

  <!-- Scripts: defer = load after HTML parsed, async = load in parallel -->
  <script src="app.js" defer></script>
</head>
```

> **Always include the viewport meta tag** — without it, your responsive CSS won't work on mobile.

---

## Forms — Input Types & Validation

```html
<form action="/submit" method="POST">

  <!-- label ties to input via for/id -->
  <label for="email">Email:</label>
  <input type="email"    id="email"    name="email"    required>

  <input type="text"     name="user"   placeholder="Username" minlength="3" maxlength="20">
  <input type="password" name="pass">
  <input type="number"   name="age"    min="1" max="120">
  <input type="date"     name="dob">
  <input type="file"     name="photo"  accept="image/*">
  <input type="range"    name="vol"    min="0" max="100" step="5">
  <input type="color"    name="color">
  <input type="checkbox" name="agree"  value="yes">
  <input type="radio"    name="gender" value="male">

  <!-- Pattern validation (regex) -->
  <input type="text" pattern="[A-Za-z]{3,}" title="At least 3 letters">

  <!-- Textarea -->
  <textarea name="message" rows="4" cols="40"></textarea>

  <!-- Fieldset + Legend (group related inputs) -->
  <fieldset>
    <legend>Address</legend>
    <input type="text" name="city">
  </fieldset>

  <!-- Datalist (autocomplete suggestions) -->
  <input list="fruits" name="fruit">
  <datalist id="fruits">
    <option value="Apple">
    <option value="Mango">
  </datalist>

  <button type="submit">Submit</button>
  <button type="reset">Reset</button>
</form>
```

**Common validation attributes:** `required`, `min`, `max`, `minlength`, `maxlength`, `pattern`, `disabled`, `readonly`

---

## HTML Entities

Use when you need to display reserved/special characters:

| Character | Entity |
|-----------|--------|
| `<`       | `&lt;` |
| `>`       | `&gt;` |
| `&`       | `&amp;` |
| `"`       | `&quot;` |
| non-breaking space | `&nbsp;` |
| `©`      | `&copy;` |
| `→`      | `&rarr;` |

```html
<p>5 &lt; 10 and 10 &gt; 5</p>
<p>Copyright &copy; 2024</p>
<p>First&nbsp;&nbsp;&nbsp;Second</p> <!-- multiple spaces -->
```

---

## `data-*` Custom Attributes

Store extra data on elements without using hidden inputs or JS variables.

```html
<button data-user-id="42" data-role="admin" onclick="handleClick(this)">
  Delete User
</button>

<script>
  function handleClick(el) {
    console.log(el.dataset.userId); // "42"
    console.log(el.dataset.role);   // "admin"
  }
</script>
```

---

## `<details>` & `<summary>` (Native Accordion)

```html
<details>
  <summary>Click to expand</summary>
  <p>Hidden content shown when expanded.</p>
</details>

<details open>  <!-- open = expanded by default -->
  <summary>FAQ: What is HTML?</summary>
  <p>HyperText Markup Language...</p>
</details>
```

---

## `<iframe>` — Embed External Content

```html
<!-- Embed another page or map -->
<iframe
  src="https://www.google.com/maps/embed?..."
  width="600"
  height="450"
  style="border:0"
  allowfullscreen
  loading="lazy">
</iframe>

<!-- Embed YouTube -->
<iframe
  width="560" height="315"
  src="https://www.youtube.com/embed/VIDEO_ID"
  allow="autoplay; encrypted-media"
  allowfullscreen>
</iframe>
```

---

## Responsive Images

```html
<!-- srcset: browser picks best size based on screen -->
<img
  src="photo-800.jpg"
  srcset="photo-400.jpg 400w, photo-800.jpg 800w, photo-1200.jpg 1200w"
  sizes="(max-width: 600px) 400px, 800px"
  alt="A responsive photo">

<!-- picture: different images for different breakpoints -->
<picture>
  <source media="(max-width: 600px)" srcset="small.jpg">
  <source media="(max-width: 1200px)" srcset="medium.jpg">
  <img src="large.jpg" alt="Responsive image">
</picture>
```
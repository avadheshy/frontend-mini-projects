# JavaScript Notes ⚡

---

## JS Engine & Console
- JS runs inside a **JS Engine** (V8 in Chrome/Node, SpiderMonkey in Firefox)
- `console.log()` → print to browser console (F12 → Console tab)
- `console.warn()`, `console.error()`, `console.table()` are also useful

---

## Variables

```js
let name = "Alice";     // block-scoped, can reassign
var age = 25;           // function-scoped, avoid using (legacy)
const PI = 3.14;        // block-scoped, cannot reassign
```

**Rule of thumb:** Always use `const`. Use `let` only when you need to reassign. Never use `var`.

---

## Primitive Types

```js
let str    = "hello";       // string
let num    = 42;            // number (int & float both)
let bool   = true;          // boolean
let empty  = null;          // intentionally empty
let undef  = undefined;     // declared but not assigned
let sym    = Symbol("id");  // unique identifier
```

**Dynamic Typing** — JS figures out the type at runtime:
```js
let x = 5;      // number
x = "hello";    // now a string — JS allows this
typeof x;       // "string"
```

---

## Reference Types

```js
// Objects
const person = { name: "Alice", age: 25 };

// Arrays
const fruits = ["apple", "banana", "mango"];

// Functions
function greet() { return "Hello"; }
```

> Primitives are **copied by value**. Reference types are **copied by address** (reference).

```js
let a = 5;
let b = a;    // b is a copy
b = 10;       // a is still 5

let obj1 = { x: 1 };
let obj2 = obj1;   // same reference!
obj2.x = 99;       // obj1.x is now 99 too
```

---

## Operators

```js
// Arithmetic
+ - * / % **   (** = exponent: 2**3 = 8)

// Assignment
= += -= *= /=

// Comparison
>  <  >=  <=
==   // loose equality (type coercion): "5" == 5 → true
===  // strict equality (no coercion): "5" === 5 → false ✅ use this

// Ternary
let result = age >= 18 ? "adult" : "minor";

// Logical
&&  // AND
||  // OR
!   // NOT

// Non-boolean with logical operators:
let name = user.name || "Guest";   // fallback value
let val  = a && b;                 // returns first falsy or last value
```

---

## Conditions

```js
// if / else
if (score > 90) {
  console.log("A");
} else if (score > 75) {
  console.log("B");
} else {
  console.log("C");
}

// switch
switch (day) {
  case "Mon": console.log("Start of week"); break;
  case "Fri": console.log("Friday!"); break;
  default:    console.log("Midweek");
}
```

---

## Loops

```js
// for
for (let i = 0; i < 5; i++) { }

// while
while (i < 5) { i++; }

// do...while (runs at least once)
do { i++; } while (i < 5);

// for...in (object keys)
for (let key in person) { console.log(key, person[key]); }

// for...of (array values)
for (let fruit of fruits) { console.log(fruit); }

// break / continue
for (let i = 0; i < 10; i++) {
  if (i === 5) break;      // stop loop
  if (i === 3) continue;   // skip this iteration
}
```

---

## Objects

```js
// Factory function
function createPerson(name, age) {
  return { name, age };   // shorthand for { name: name, age: age }
}

// Constructor function
function Person(name, age) {
  this.name = name;
  this.age = age;
}
const p = new Person("Alice", 25);

// Dynamic nature
p.email = "alice@example.com";   // add property anytime
delete p.email;                  // remove property
```

**Every object has a `constructor` property pointing to the function used to create it.**

```js
// Clone an object
const clone1 = Object.assign({}, original);  // shallow
const clone2 = { ...original };               // spread (shallow)
```

---

## Functions

```js
// Named
function add(a, b) { return a + b; }

// Anonymous assigned
const add = function(a, b) { return a + b; };

// Arrow function
const add = (a, b) => a + b;

// Hoisting — named functions can be called before declaration
greet(); // works!
function greet() { console.log("Hi"); }

// Arguments object (non-arrow functions only)
function sum() {
  console.log(arguments); // array-like object of all args
}

// Rest operator
function sum(...nums) {
  return nums.reduce((a, b) => a + b, 0);
}

// Default parameters
function greet(name = "Guest") { return `Hello ${name}`; }

// Getter / Setter
const circle = {
  radius: 5,
  get area() { return Math.PI * this.radius ** 2; },
  set diameter(d) { this.radius = d / 2; }
};
```

---

## Built-in Objects

```js
// Math
Math.round(4.7)   // 5
Math.floor(4.9)   // 4
Math.ceil(4.1)    // 5
Math.random()     // 0 to 1
Math.max(1,2,3)   // 3

// String
let s = "Hello World";
s.length          // 11
s.toUpperCase()   // "HELLO WORLD"
s.includes("World")  // true
s.startsWith("He")   // true
s.slice(0, 5)        // "Hello"
s.replace("World","JS") // "Hello JS"
s.split(" ")         // ["Hello","World"]
s.trim()             // removes whitespace

// Template literals
let name = "Alice";
console.log(`Hello, ${name}! You are ${2024 - 1999} years old.`);

// Date
const now = new Date();
now.getFullYear(); now.getMonth(); now.getDate();
```

---

## Arrays

```js
const arr = [1, 2, 3];

// Add
arr.push(4);          // end
arr.unshift(0);       // start

// Remove
arr.pop();            // remove from end
arr.shift();          // remove from start
arr.splice(1, 1);     // remove at index 1, count 1

// Find
arr.indexOf(2);       // index of value
arr.includes(3);      // true/false
arr.find(x => x > 2); // first match
arr.findIndex(x => x > 2);

// Combine / Split
arr.concat([4, 5]);   // join arrays
arr.slice(1, 3);      // portion (non-destructive)
arr.join(", ");       // "1, 2, 3"
```

---

## Array Higher-Order Methods

```js
const nums = [1, 2, 3, 4, 5];

// map → transform each element, returns new array
const doubled = nums.map(n => n * 2);        // [2,4,6,8,10]

// filter → keep elements that pass test
const evens = nums.filter(n => n % 2 === 0); // [2,4]

// reduce → collapse to single value
const sum = nums.reduce((acc, n) => acc + n, 0); // 15

// Chaining
const result = nums
  .filter(n => n > 2)
  .map(n => n * 10);  // [30,40,50]
```

---

## Callback & Arrow Functions

```js
// Callback = function passed as argument
function greet(name, callback) {
  console.log("Hello " + name);
  callback();
}
greet("Alice", () => console.log("Done!"));

// Arrow functions — shorter syntax, no own `this`
const square = x => x * x;
const add = (a, b) => a + b;
const greet = name => {
  const msg = `Hello ${name}`;
  return msg;
};
```

---

## DOM Manipulation

### Selecting Elements
```js
document.getElementById("myId")
document.getElementsByClassName("myClass")  // HTMLCollection
document.getElementsByTagName("div")         // HTMLCollection
document.querySelector(".myClass")          // first match
document.querySelectorAll(".myClass")       // NodeList (all matches)
```

### Reading / Changing Content
```js
el.innerHTML   // HTML string (can include tags)
el.outerHTML   // element + its HTML
el.textContent // all text including hidden
el.innerText   // only visible text

el.textContent = "New text";
el.innerHTML = "<strong>Bold</strong>";
```

### Attributes & Styles
```js
el.getAttribute("href")
el.setAttribute("href", "https://google.com")
el.removeAttribute("disabled")

el.style.color = "red";
el.style.cssText = "color: red; font-size: 18px;";

el.className = "newClass";
el.classList.add("active");
el.classList.remove("active");
el.classList.toggle("active");
```

### Create / Add / Remove Elements
```js
const div = document.createElement("div");
div.textContent = "I'm new!";
parent.appendChild(div);
parent.removeChild(child);

// insertAdjacentHTML positions:
el.insertAdjacentHTML("beforebegin", "<p>Before</p>");
el.insertAdjacentHTML("afterbegin",  "<p>Inside start</p>");
el.insertAdjacentHTML("beforeend",   "<p>Inside end</p>");
el.insertAdjacentHTML("afterend",    "<p>After</p>");
```

---

## Events

```js
// Add event listener
btn.addEventListener("click", handleClick);

// Event handler
function handleClick(event) {
  console.log(event.target);         // element that triggered event
  event.preventDefault();            // stop default behavior (e.g. form submit)
}

// Remove — must pass the SAME function reference
btn.removeEventListener("click", handleClick);
```

### Event Phases
1. **Capture** — event travels from `window` down to target
2. **Target** — event reaches the element
3. **Bubbling** — event bubbles up from target to `window` (default)

### Event Delegation (efficient events)
```js
// Instead of adding listener to each child, add to parent
ul.addEventListener("click", (e) => {
  console.log(e.target.textContent); // know which item was clicked
});
```

---

## Async JavaScript

### The Event Loop
- JS is **single-threaded** — one thing at a time
- **Call Stack** → where functions execute
- **Browser APIs** → handle async tasks (setTimeout, fetch, etc.)
- **Queue** → async callbacks wait here
- **Event Loop** → moves tasks from queue → stack when stack is empty

```js
console.log("1");
setTimeout(() => console.log("2"), 0); // goes to queue
console.log("3");
// Output: 1, 3, 2
```

### setTimeout
```js
setTimeout(() => console.log("After 2s"), 2000);
setTimeout(() => console.log("Next tick"), 0); // queue, runs after sync
clearTimeout(id); // cancel it
```

### Promises
```js
const promise = new Promise((resolve, reject) => {
  // async work
  if (success) resolve("data");
  else reject("error");
});

// 3 states: pending → fulfilled or rejected
promise
  .then(data => console.log(data))
  .catch(err => console.error(err))
  .finally(() => console.log("Done"));

// Parallel execution
Promise.all([p1, p2, p3]).then(results => console.log(results));
```

### Async / Await
```js
async function fetchData() {
  try {
    const response = await fetch("https://api.example.com/data");
    const data = await response.json();
    console.log(data);
  } catch (err) {
    console.error(err);
  }
}
```

### Fetch API
```js
fetch("https://api.example.com/users")
  .then(res => res.json())
  .then(data => console.log(data))
  .catch(err => console.error(err));

// POST request
fetch("/api/users", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ name: "Alice" })
});
```

---

## Closures

A function that **remembers** variables from its outer scope even after the outer function has returned.

```js
function makeCounter() {
  let count = 0;             // outer variable
  return function() {
    count++;                 // inner function references outer var
    return count;
  };
}
const counter = makeCounter();
counter(); // 1
counter(); // 2
// count is preserved in closure — not a copy, a reference
```

---

## Scope

```js
// Global scope — accessible everywhere
let globalVar = "I'm global";

// Function scope
function foo() {
  let funcVar = "only inside foo";
}

// Block scope — let/const are block-scoped
{
  let blockVar = "only in this block";
  const also = "same";
  var leaked = "var ignores blocks!"; // DON'T use var
}

// Hoisting — var declarations moved to top (not value, just declaration)
console.log(x); // undefined (not error) — var is hoisted
var x = 5;

console.log(y); // ReferenceError — let is NOT hoisted
let y = 5;

// Functions are fully hoisted
greet(); // works!
function greet() { console.log("hi"); }
```

---

## Destructuring

```js
// Array destructuring
const [a, b, c] = [1, 2, 3];
const [first, , third] = [1, 2, 3];  // skip index
const [x = 10, y = 20] = [5];        // default values → x=5, y=20

// Object destructuring
const { name, age } = { name: "Alice", age: 25 };
const { name: fullName } = person;   // rename: fullName = person.name
const { city = "Unknown" } = person; // default value

// Nested
const { address: { street } } = person;

// In function parameters
function greet({ name, age = 0 }) {
  return `${name} is ${age}`;
}

// Swap variables
let p = 1, q = 2;
[p, q] = [q, p];
```

---

## Spread & Rest Operators

```js
// Spread (...) — expand iterable into individual elements
const arr1 = [1, 2, 3];
const arr2 = [...arr1, 4, 5];           // [1,2,3,4,5]

const obj1 = { a: 1 };
const obj2 = { ...obj1, b: 2 };         // { a:1, b:2 }
const merged = { ...defaults, ...overrides }; // merge objects

// Copy arrays/objects
const copy = [...original];
const objCopy = { ...original };

// Rest (...) — collect remaining into array
function sum(first, ...rest) {           // rest = array of remaining args
  return first + rest.reduce((a, b) => a + b, 0);
}

const [head, ...tail] = [1, 2, 3, 4];   // head=1, tail=[2,3,4]
const { a, ...remaining } = obj;        // remaining = obj without 'a'
```

---

## Optional Chaining `?.` & Nullish Coalescing `??`

```js
// Optional chaining — safely access nested properties
// Returns undefined instead of throwing error
const user = null;
console.log(user?.name);           // undefined (not TypeError)
console.log(user?.address?.city);  // undefined
console.log(arr?.[0]);             // safe array access
console.log(fn?.());               // safe function call

// Nullish coalescing — fallback only for null/undefined (not 0 or "")
const name = user?.name ?? "Guest";
const count = data?.count ?? 0;

// vs || (OR) — falls back for ALL falsy values (0, "", false too)
const val1 = 0 || "default";    // "default" (might not want this)
const val2 = 0 ?? "default";    // 0 (correct — 0 is a valid value)
```

---

## ES6 Classes

```js
class Animal {
  constructor(name, sound) {
    this.name = name;          // instance property
    this.sound = sound;
  }

  // Method
  speak() {
    return `${this.name} says ${this.sound}`;
  }

  // Static method (called on class, not instance)
  static create(name) {
    return new Animal(name, "...");
  }
}

// Inheritance
class Dog extends Animal {
  constructor(name) {
    super(name, "Woof");       // call parent constructor
    this.tricks = [];
  }

  learn(trick) {
    this.tricks.push(trick);
  }

  // Override parent method
  speak() {
    return super.speak() + "!"; // call parent method
  }
}

const dog = new Dog("Rex");
dog.speak(); // "Rex says Woof!"
dog instanceof Dog;    // true
dog instanceof Animal; // true
```

---

## Error Handling

```js
// try/catch/finally
try {
  const data = JSON.parse(invalidJson); // throws SyntaxError
  riskyOperation();
} catch (error) {
  console.error(error.message);  // error.name, error.message, error.stack
} finally {
  cleanup(); // ALWAYS runs, even if error
}

// Throw custom errors
function divide(a, b) {
  if (b === 0) throw new Error("Cannot divide by zero");
  return a / b;
}

// Custom error types
class ValidationError extends Error {
  constructor(message) {
    super(message);
    this.name = "ValidationError";
  }
}

try {
  throw new ValidationError("Email is required");
} catch (e) {
  if (e instanceof ValidationError) console.log("Validation:", e.message);
  else throw e; // re-throw unknown errors
}
```

---

## ES Modules (import / export)

```js
// Named exports — export multiple things
export const PI = 3.14;
export function add(a, b) { return a + b; }
export class User { ... }

// Default export — one per file, import with any name
export default function greet(name) { return `Hello ${name}`; }

// Import named
import { PI, add } from "./math.js";
import { add as sum } from "./math.js"; // rename

// Import default
import greet from "./greet.js";

// Import everything
import * as Math from "./math.js";
Math.add(1, 2);

// Import both
import greet, { PI, add } from "./module.js";
```

---

## `this` Keyword

`this` refers to the object that is **currently executing the function**:

```js
// In a method — this = the object
const person = {
  name: "Alice",
  greet() { return `Hi I'm ${this.name}`; }
};

// In a regular function — this = window (or undefined in strict mode)
function show() { console.log(this); }

// Arrow functions — no own this, inherit from surrounding scope
const obj = {
  name: "Alice",
  greet: () => console.log(this.name), // this = outer scope (NOT obj)
  hello() {
    const inner = () => console.log(this.name); // this = obj ✅
    inner();
  }
};
```

---

## `bind`, `call`, `apply`

Manually set `this`:

```js
function greet(greeting, punctuation) {
  return `${greeting}, ${this.name}${punctuation}`;
}

const user = { name: "Alice" };

// call — invoke immediately, args as comma-separated
greet.call(user, "Hello", "!");       // "Hello, Alice!"

// apply — invoke immediately, args as array
greet.apply(user, ["Hello", "!"]);    // "Hello, Alice!"

// bind — returns NEW function with this bound (doesn't invoke)
const greetAlice = greet.bind(user);
greetAlice("Hey", ".");               // "Hey, Alice."

// Common use: fix this in event handlers
class Timer {
  start() {
    setTimeout(this.tick.bind(this), 1000); // without bind, this = window
  }
  tick() { console.log("tick"); }
}
```

---

## JSON & localStorage

```js
// JSON — convert between JS objects and strings (for APIs and storage)
const obj = { name: "Alice", age: 25 };

const jsonString = JSON.stringify(obj);       // '{"name":"Alice","age":25}'
const parsed     = JSON.parse(jsonString);    // back to object

// Pretty print
JSON.stringify(obj, null, 2);

// localStorage — persists across browser sessions (string only)
localStorage.setItem("user", JSON.stringify({ name: "Alice" }));
const user = JSON.parse(localStorage.getItem("user"));
localStorage.removeItem("user");
localStorage.clear();

// sessionStorage — cleared when tab closes
sessionStorage.setItem("token", "abc123");
```

---

## Object Utility Methods

```js
const person = { name: "Alice", age: 25, city: "Delhi" };

Object.keys(person)    // ["name", "age", "city"]
Object.values(person)  // ["Alice", 25, "Delhi"]
Object.entries(person) // [["name","Alice"], ["age",25], ["city","Delhi"]]

// Iterate over an object
Object.entries(person).forEach(([key, value]) => {
  console.log(`${key}: ${value}`);
});

// Check if property exists
"name" in person          // true
person.hasOwnProperty("name") // true

// Freeze / Seal
Object.freeze(person); // cannot change any property
Object.seal(person);   // can change values but not add/delete keys

// From entries back to object
const obj = Object.fromEntries([["a", 1], ["b", 2]]); // {a:1, b:2}
```

---

## `typeof` & `instanceof`

```js
typeof "hello"     // "string"
typeof 42          // "number"
typeof true        // "boolean"
typeof undefined   // "undefined"
typeof null        // "object"  ← famous JS bug
typeof {}          // "object"
typeof []          // "object"  ← arrays are objects
typeof function(){} // "function"

// instanceof — checks prototype chain
[] instanceof Array    // true
{} instanceof Object   // true
dog instanceof Dog     // true
dog instanceof Animal  // true (inheritance)

// Better array check
Array.isArray([]);     // true ✅
```

# 🔥 Namaste JavaScript — Final Notes
> Combined from Akshay Saini's Namaste JS series + personal notes

---

## 📌 Table of Contents
1. [How JS Works — Execution Context](#1-how-js-works--execution-context)
2. [Call Stack & Hoisting](#2-call-stack--hoisting)
3. [Variables — var, let, const](#3-variables--var-let-const)
4. [Scope, Scope Chain & Lexical Environment](#4-scope-scope-chain--lexical-environment)
5. [Closures](#5-closures)
6. [First Class Functions](#6-first-class-functions)
7. [Callback Functions & Event Loop](#7-callback-functions--event-loop)
8. [JS Engine Internals](#8-js-engine-internals)
9. [Higher Order Functions — map / filter / reduce](#9-higher-order-functions--map--filter--reduce)
10. [Primitive & Reference Types](#10-primitive--reference-types)
11. [Operators](#11-operators)
12. [Conditions & Loops](#12-conditions--loops)
13. [Objects & Functions (Deep Dive)](#13-objects--functions-deep-dive)
14. [Arrays & Array Methods](#14-arrays--array-methods)
15. [DOM Manipulation](#15-dom-manipulation)
16. [Events](#16-events)
17. [Async JS — Promises & Async/Await](#17-async-js--promises--asyncawait)
18. [Destructuring, Spread & Rest](#18-destructuring-spread--rest)
19. [ES6 Classes & Inheritance](#19-es6-classes--inheritance)
20. [Error Handling](#20-error-handling)
21. [ES Modules](#21-es-modules)
22. [this, bind, call, apply](#22-this-bind-call-apply)
23. [JSON & localStorage](#23-json--localstorage)
24. [Object Utility Methods](#24-object-utility-methods)

---

## 1. How JS Works — Execution Context

> **Everything in JS happens inside an Execution Context.**

An execution context has two components:

| Memory (Variable Environment) | Code (Thread of Execution) |
|-------------------------------|----------------------------|
| key: value pairs              | code runs line by line     |

- **JavaScript is a synchronous, single-threaded language** — it can run one command at a time, in a specific order.
- **Global Execution Context (GEC)** is created when JS starts running.
- When a function is called → a **new execution context** is created for it.
- `return` → returns control back to where it was called from, and that execution context is **gone**.

### Two Phases of Context Creation:
1. **Creation Phase (Memory Phase)** — variables are set to `undefined`, functions store their whole code.
2. **Execution Phase** — values are assigned to variables, code runs line by line.

---

## 2. Call Stack & Hoisting

### Call Stack
- Maintains the **order of execution** of execution contexts.
- Also called: Program Stack / Control Stack / Runtime Stack / Machine Stack / Execution Context Stack.
- The whole execution context is **pushed into** the call stack.
- When function finishes → popped off the stack.

```
GEC → pushed at start
fn() called → new EC pushed
fn() returns → EC popped
GEC ends → popped
```

### Hoisting
- JS moves **declarations** to the top before execution.
- **`var`** → hoisted with value `undefined`
- **Functions** → fully hoisted (whole code stored in memory phase)
- **`let` / `const`** → hoisted but in **Temporal Dead Zone (TDZ)** — cannot access before declaration

```js
console.log(x);   // undefined (var hoisted)
var x = 5;

greet();          // works! (function fully hoisted)
function greet() { console.log("Hi"); }

console.log(y);   // ReferenceError (let in TDZ)
let y = 10;
```

---

## 3. Variables — var, let, const

```js
var   age = 25;    // function-scoped, hoisted as undefined, AVOID
let   name = "JS"; // block-scoped, TDZ, can reassign
const PI = 3.14;   // block-scoped, TDZ, cannot reassign
```

**Rule of thumb:** Always use `const`. Use `let` when you need to reassign. Never use `var`.

### let & const — Block Scope
```js
{
  let a = 10;   // only accessible inside this block
  const b = 20; // same
  var c = 30;   // leaks out! (var ignores blocks)
}
console.log(c); // 30 — var leaked
console.log(a); // ReferenceError
```

### Temporal Dead Zone (TDZ)
- Time between the **start of block** and the **let/const declaration line**.
- Accessing variable in TDZ → `ReferenceError`.
- `let` & `const` are hoisted, but placed in TDZ — **not initialized**.

```js
// TDZ starts here ↓
console.log(a); // ReferenceError: Cannot access 'a' before initialization
let a = 5;      // TDZ ends here ↑
```

### Syntax Errors vs Type Errors
```js
// Syntax Error (caught before execution)
const x = 5;
const x = 10; // SyntaxError: Identifier 'x' has already been declared

// Type Error (at runtime)
const y = 5;
y = 10; // TypeError: Assignment to constant variable
```

### Shadowing
```js
let a = 100;
{
  let a = 20;   // shadows outer 'a' inside this block
  console.log(a); // 20
}
console.log(a); // 100
```
- **`var` shadowing `let`** → illegal (var leaks out to function scope, which conflicts)

---

## 4. Scope, Scope Chain & Lexical Environment

### Scope Chain
- JS looks for a variable in its own scope first, then goes **outward** through parent scopes.
- This chain of scopes is called the **Scope Chain**.
- Scope is determined **lexically** (where code is written), not where it is called.

### Lexical Environment
- Every execution context has a **Lexical Environment** = its local memory + reference to parent's lexical environment.
- **Scope chain = chain of lexical environments**.

```js
function outer() {
  let x = 10;
  function inner() {
    console.log(x); // 10 — found in outer's lexical env
  }
  inner();
}
```

### `undefined` vs `not defined`
- **`undefined`** → variable declared but not assigned (memory allocated, value = undefined)
- **`not defined`** → variable never declared at all → `ReferenceError`

### JS is Loosely Typed
```js
let x = 5;      // number
x = "hello";    // now string — JS allows this
typeof x;       // "string"
```

---

## 5. Closures

> A **closure** is a function that **remembers** variables from its outer (lexical) scope even after the outer function has returned.

```js
function makeCounter() {
  let count = 0;        // outer variable
  return function() {
    count++;            // inner function remembers 'count'
    return count;
  };
}
const counter = makeCounter();
counter(); // 1
counter(); // 2
counter(); // 3
// count is NOT a copy — it's a reference to the same variable
```

### Block Scope also gives Closure
```js
// let gives lexical scope even inside blocks
let a = 20; let x = 30; // gives lexical scope → closure
```

### Closure = function + lexical environment (its outer scope)
```js
// Closure is created when a function is returned/used from its outer scope
function outer() {
  let b = 10;
  return function inner() {
    console.log(b); // closes over 'b'
  };
}
const fn = outer();
fn(); // 10 — still accessible via closure
```

### Shadowing works similar in closures
```js
// Shadowing works in function scope as closures
// works similar to function's lexical scope
```

### setTimeout + Closure Interview Question
```js
// ❌ var — all callbacks share the SAME 'i' (prints 6,6,6,6,6)
function x() {
  for (var i = 1; i <= 5; i++) {
    setTimeout(function() {
      console.log(i); // all print 6
    }, i * 1000);
  }
}

// ✅ let — each iteration gets its OWN 'i' (prints 1,2,3,4,5)
function x() {
  for (let i = 1; i <= 5; i++) {
    setTimeout(function() {
      console.log(i); // 1, 2, 3, 4, 5
    }, i * 1000);
  }
}

// ✅ Fix with var using closure
function x() {
  for (var i = 1; i <= 5; i++) {
    function close(i) {          // new scope per iteration
      setTimeout(function() {
        console.log(i);
      }, i * 1000);
    }
    close(i);
  }
}
```

### Uses of Closures
- Module Design Pattern
- Currying
- Functions like `once` (run only once)
- Memoize / Caching
- Maintaining state in async world
- setTimeouts
- Iterators
- Data privacy / encapsulation

---

## 6. First Class Functions

> **First Class Functions** = Functions are treated like any other value. They can be assigned to variables, passed as arguments, and returned from other functions.

### Types of Functions

```js
// 1. Function Statement (aka Function Declaration) — hoisted ✅
function a() {
  console.log("a called");
}

// 2. Function Expression — NOT hoisted ❌
var b = function(param1) {
  return function xyz() {};
};
console.log(b()); // works after declaration

// 3. Anonymous Function — no name, used as a value
var fn = function() { console.log("anonymous"); };

// 4. Named Function Expression
var c = function myFunc() {
  // myFunc accessible only inside here
};

// 5. Arrow Function — shorter syntax, no own 'this'
const add = (a, b) => a + b;
const square = x => x * x;
const greet = name => {
  return `Hello ${name}`;
};
```

### Parameters vs Arguments
```js
function add(a, b) { }  // a, b → parameters (inside function definition)
add(5, 10);             // 5, 10 → arguments (values passed while calling)
```

### Difference: Function Statement vs Expression
| Feature | Function Statement | Function Expression |
|---------|-------------------|---------------------|
| Hoisted | ✅ Yes | ❌ No |
| Named | Always | Optional |
| Usage | Declaration | Assigned as value |

### Functions as First Class Citizens
```js
// Pass function as argument
function run(fn) { fn(); }
run(() => console.log("called!"));

// Return function from function
function multiplier(x) {
  return function(y) { return x * y; };
}
const double = multiplier(2);
double(5); // 10
```

---

## 7. Callback Functions & Event Loop

### Callback Function
> A **callback** is a function passed as an argument to another function, to be called later.

```js
setTimeout(function() {
  console.log("timer");
}, 5000);

function x(y) {
  console.log("x");
  y();
}
x(function y() {
  console.log("y");
});
```

- JS is **synchronous** and **single-threaded** → but callbacks let us handle async tasks.
- They may take **longer** instead of **5 seconds** sometimes due to microtask/macrotask queue behavior.

### Web APIs (provided by browser, not JS)
- `setTimeout()`
- DOM APIs (`document`)
- `fetch()`
- `localStorage`
- `console`
- `location`

These are **not part of JS** — they are given to JS by the browser through the **global object (`window`)**.

### Event Loop — How Async Works

```
┌─────────────────────────────────────────┐
│           Call Stack                    │
│  (runs one thing at a time)             │
└─────────────────┬───────────────────────┘
                  │ (stack empty?)
                  ▼
┌─────────────────────────────────────────┐
│           Event Loop                    │
│  watches: is stack empty?               │
│  if yes → moves task from queue to stack│
└──────┬─────────────────────┬────────────┘
       │                     │
       ▼                     ▼
┌──────────────┐    ┌─────────────────────┐
│ Microtask    │    │  Callback / Task     │
│ Queue        │    │  Queue (Macrotask)   │
│ (Promises,   │    │  (setTimeout,        │
│  MutationObs)│    │   setInterval, etc.) │
└──────────────┘    └─────────────────────┘
```

**Priority:** Microtask Queue > Callback Queue

### Task Queue vs Microtask Queue
- **Microtask Queue** (higher priority):
  - Promise callbacks (`.then`, `.catch`, `.finally`)
  - `queueMicrotask()`
  - `MutationObserver`
- **Callback Queue / Task Queue** (lower priority):
  - `setTimeout`, `setInterval`
  - DOM events

```js
console.log("1");
setTimeout(() => console.log("2"), 0); // goes to Task Queue
Promise.resolve().then(() => console.log("3")); // Microtask
console.log("4");
// Output: 1, 4, 3, 2
```

### Event Loop Rules
1. First loop: checks callback queue, picks tasks & puts them in callback queue.
2. While we need callbacks, we put them in the callback queue.
3. That loop checks the callback queue & if any callback, it executes it.
4. It attaches the callback from the callback queue only if the callback queue has something.
5. Event Loop only picks task from callback queue if Call Stack is empty.
6. Only if Call Stack is empty, it checks the callback queue (any) → microtask queue first.

---

## 8. JS Engine Internals

### JS Engine = JIT Compiler (compilation of execution & done 3 things)
1. **Parsing** → reads JS code, does 3 things
2. **Compilation** → combination of compilation & interpretation
3. **Execution**

### JS runs code with the help of JS Runtime Environment (browser/Node)
- **Browser runs JS** — code line by line in environment
- **JS Engine** is not a piece of machine → it is a piece of code (software)
- **JS Engine is a combination** of Compilation + Interpretation

### Memory in JS Engine
- **Memory Heap** — a global object, shared space where functions & variables are stored
- **Call Stack** — space where functions are executed in order (shared)
- **Garbage Collector** — collected & clears unused memory

### Garbage Collector
- Uses **Mark & Sweep** algorithm
- **Inline caching** → used to speed up accessing properties
- **Garbage** → clears unused memory
- `reduce` → used to add/even values on a single value
- After processing, they may return the value back in logic

---

## 9. Higher Order Functions — map / filter / reduce

> A **Higher Order Function** is a function that takes another function as an argument OR returns a function.

### map — transform each element, returns new array
```js
const arr = [5, 1, 3, 2, 6];

function double(x) { return x * 2; }
function triple(x) { return x * 3; }

const doubled = arr.map(double);  // [10, 2, 6, 4, 12]
const tripled = arr.map(triple);  // [15, 3, 9, 6, 18]

// Binary conversion using map
const binary = arr.map(x => x.toString(2)); // ["101","1","11","10","110"]

// Arrow shorthand
const squared = arr.map(x => x * x);
```

### filter — keep elements that pass a test
```js
function isEven(x) {
  return x % 2 === 0;
}

const output = arr.filter(isEven); // [2, 6]

// Arrow shorthand
const odds = arr.filter(x => x % 2 !== 0);
```

### reduce — collapse to a single value
```js
// reduce(callback, initialValue)
// acc = accumulator (running result), curr = current element
const sum = arr.reduce((acc, curr) => acc + curr, 0); // 17
const max = arr.reduce((acc, curr) => acc > curr ? acc : curr, 0); // 6
```

### Chaining (map + filter together)
```js
const users = [
  { firstName: "akshay", lastName: "saini", age: 26 },
  { firstName: "donald", lastName: "trump", age: 75 },
  { firstName: "elon",   lastName: "musk",  age: 50 },
  { firstName: "deepika",lastName: "padukone", age: 26 },
];

// Get first names of users with age < 30
const output = users
  .filter(x => x.age < 30)
  .map(x => x.firstName);
// ["akshay", "deepika"]

// Count users by age using reduce
const ageCount = users.reduce((acc, user) => {
  if (acc[user.age]) acc[user.age]++;
  else acc[user.age] = 1;
  return acc;
}, {});
```

### Polyfill for map (How map works internally)
```js
// Using Array.prototype.calculate (custom map-like method)
Array.prototype.calculate = function(logic) {
  const output = [];
  for (let i = 0; i < this.length; i++) {
    output.push(logic(this[i]));
  }
  return output;
};

console.log(radius.calculate(area));
// same as radius.map(area)
```

---

## 10. Primitive & Reference Types

### Primitive Types (copied by value)
```js
let str  = "hello";      // string
let num  = 42;           // number (int & float)
let bool = true;         // boolean
let empty = null;        // intentionally empty
let undef = undefined;   // declared but not assigned
let sym  = Symbol("id"); // unique identifier
let big  = 9007n;        // BigInt
```

```js
let a = 5;
let b = a; // b is a COPY
b = 10;
console.log(a); // 5 — unchanged
```

### Reference Types (copied by reference)
```js
const person = { name: "Alice", age: 25 };
const fruits = ["apple", "banana"];
function greet() { return "Hello"; }
```

```js
let obj1 = { x: 1 };
let obj2 = obj1; // SAME reference
obj2.x = 99;
console.log(obj1.x); // 99 — both changed!

// Clone properly
const clone1 = Object.assign({}, obj1);  // shallow copy
const clone2 = { ...obj1 };             // spread (shallow)
```

### typeof
```js
typeof "hello"      // "string"
typeof 42           // "number"
typeof true         // "boolean"
typeof undefined    // "undefined"
typeof null         // "object" ← famous JS bug
typeof {}           // "object"
typeof []           // "object" ← arrays are objects
typeof function(){} // "function"

Array.isArray([]);  // true ✅ (better way to check arrays)
```

---

## 11. Operators

```js
// Arithmetic
+ - * / % **  (** = exponent: 2**3 = 8)

// Assignment
= += -= *= /=

// Comparison
>  <  >=  <=
==   // loose (type coercion): "5" == 5 → true
===  // strict (no coercion): "5" === 5 → false ✅

// Ternary
let result = age >= 18 ? "adult" : "minor";

// Logical
&&  // AND
||  // OR
!   // NOT

// Fallback / Short-circuit
let name = user.name || "Guest";  // fallback for all falsy values
let val  = a ?? "default";        // fallback only for null/undefined ✅

// Optional Chaining
const city = user?.address?.city;  // undefined instead of TypeError
const first = arr?.[0];
const result2 = fn?.();
```

---

## 12. Conditions & Loops

```js
// if / else if / else
if (score > 90) {
  console.log("A");
} else if (score > 75) {
  console.log("B");
} else {
  console.log("C");
}

// switch
switch (day) {
  case "Mon": console.log("Monday"); break;
  case "Fri": console.log("Friday"); break;
  default: console.log("Midweek");
}
```

```js
// for
for (let i = 0; i < 5; i++) { }

// while
while (i < 5) { i++; }

// do...while (runs at least once)
do { i++; } while (i < 5);

// for...in (object keys)
for (let key in person) { console.log(key, person[key]); }

// for...of (array values)
for (let fruit of fruits) { console.log(fruit); }

// break / continue
for (let i = 0; i < 10; i++) {
  if (i === 5) break;     // stop loop
  if (i === 3) continue;  // skip this iteration
}
```

---

## 13. Objects & Functions (Deep Dive)

### Objects
```js
// Factory function
function createPerson(name, age) {
  return { name, age }; // shorthand
}

// Constructor function
function Person(name, age) {
  this.name = name;
  this.age = age;
}
const p = new Person("Alice", 25);

// Dynamic properties
p.email = "alice@example.com"; // add
delete p.email;                // remove
```

### Getter & Setter
```js
const circle = {
  radius: 5,
  get area() { return Math.PI * this.radius ** 2; },
  set diameter(d) { this.radius = d / 2; }
};
circle.diameter = 20; // triggers setter
circle.area;          // triggers getter
```

### Built-in — Math & String
```js
Math.round(4.7)   // 5
Math.floor(4.9)   // 4
Math.ceil(4.1)    // 5
Math.random()     // 0 to <1
Math.max(1,2,3)   // 3
Math.min(1,2,3)   // 1

let s = "Hello World";
s.length           // 11
s.toUpperCase()    // "HELLO WORLD"
s.includes("World")// true
s.slice(0, 5)      // "Hello"
s.replace("World","JS") // "Hello JS"
s.split(" ")       // ["Hello","World"]
s.trim()           // removes whitespace
s.startsWith("He") // true

// Template literals
console.log(`Hello, ${name}! Age: ${2024 - 1999}`);
```

---

## 14. Arrays & Array Methods

```js
const arr = [1, 2, 3];

// Add / Remove
arr.push(4);        // add to end
arr.unshift(0);     // add to start
arr.pop();          // remove from end
arr.shift();        // remove from start
arr.splice(1, 1);   // remove at index 1

// Find
arr.indexOf(2);              // index of value
arr.includes(3);             // true/false
arr.find(x => x > 2);       // first match (element)
arr.findIndex(x => x > 2);  // first match (index)

// Transform
arr.concat([4, 5]);  // join arrays
arr.slice(1, 3);     // portion (non-destructive)
arr.join(", ");      // "1, 2, 3"
arr.reverse();       // reverses in place
arr.sort((a,b) => a - b); // numeric sort

// Iteration
arr.forEach(x => console.log(x));
arr.some(x => x > 3);   // true if ANY pass
arr.every(x => x > 0);  // true if ALL pass
arr.flat();              // flatten nested arrays
arr.flatMap(x => [x, x * 2]); // map + flat
```

---

## 15. DOM Manipulation

### Selecting Elements
```js
document.getElementById("myId")
document.querySelector(".myClass")        // first match
document.querySelectorAll(".myClass")     // NodeList (all)
document.getElementsByClassName("cls")    // HTMLCollection
document.getElementsByTagName("div")
```

### Reading / Changing Content
```js
el.textContent = "New text";           // plain text
el.innerHTML = "<strong>Bold</strong>"; // HTML string
el.innerText   // only visible text
el.outerHTML   // element + its HTML
```

### Attributes & Styles
```js
el.getAttribute("href")
el.setAttribute("href", "https://google.com")
el.removeAttribute("disabled")

el.style.color = "red";
el.classList.add("active");
el.classList.remove("active");
el.classList.toggle("active");
el.className = "newClass";
```

### Create / Add / Remove Elements
```js
const div = document.createElement("div");
div.textContent = "I'm new!";
parent.appendChild(div);
parent.removeChild(child);

// insertAdjacentHTML
el.insertAdjacentHTML("beforebegin", "<p>Before element</p>");
el.insertAdjacentHTML("afterbegin",  "<p>Inside at start</p>");
el.insertAdjacentHTML("beforeend",   "<p>Inside at end</p>");
el.insertAdjacentHTML("afterend",    "<p>After element</p>");
```

---

## 16. Events

```js
btn.addEventListener("click", handleClick);

function handleClick(event) {
  console.log(event.target);   // element clicked
  event.preventDefault();      // stop default (form submit, link)
}

// Must pass SAME function reference to remove
btn.removeEventListener("click", handleClick);
```

### Event Phases
1. **Capture** — event travels window → target (top down)
2. **Target** — event is at the element
3. **Bubble** — event travels target → window (bottom up, default)

### Event Delegation (efficient pattern)
```js
// Add ONE listener to parent instead of each child
ul.addEventListener("click", (e) => {
  console.log(e.target.textContent);
});
```

---

## 17. Async JS — Promises & Async/Await

### Promises
```js
const promise = new Promise((resolve, reject) => {
  if (success) resolve("data");
  else reject("error");
});

// 3 States: pending → fulfilled OR rejected
promise
  .then(data => console.log(data))
  .catch(err => console.error(err))
  .finally(() => console.log("Always runs"));

// Parallel
Promise.all([p1, p2, p3]).then(results => console.log(results));
Promise.race([p1, p2]).then(first => console.log(first));
Promise.allSettled([p1, p2]).then(results => console.log(results));
```

### Async / Await (syntactic sugar over Promises)
```js
async function fetchData() {
  try {
    const response = await fetch("https://api.example.com/data");
    const data = await response.json();
    console.log(data);
  } catch (err) {
    console.error(err);
  }
}
```

### Fetch API
```js
// GET
fetch("https://api.example.com/users")
  .then(res => res.json())
  .then(data => console.log(data))
  .catch(err => console.error(err));

// POST
fetch("/api/users", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ name: "Alice" })
});
```

### setTimeout
```js
const id = setTimeout(() => console.log("After 2s"), 2000);
clearTimeout(id); // cancel it

// Tricky output:
console.log("1");
setTimeout(() => console.log("2"), 0); // queue
console.log("3");
// Output: 1, 3, 2
```

---

## 18. Destructuring, Spread & Rest

### Destructuring
```js
// Array destructuring
const [a, b, c] = [1, 2, 3];
const [first, , third] = [1, 2, 3]; // skip index
const [x = 10, y = 20] = [5];       // defaults: x=5, y=20

// Object destructuring
const { name, age } = { name: "Alice", age: 25 };
const { name: fullName } = person;  // rename
const { city = "Unknown" } = person; // default

// Nested
const { address: { street } } = person;

// In function params
function greet({ name, age = 0 }) {
  return `${name} is ${age}`;
}

// Swap variables
[p, q] = [q, p];
```

### Spread & Rest
```js
// Spread — expand iterable
const arr2 = [...arr1, 4, 5];
const obj2 = { ...obj1, b: 2 };
const merged = { ...defaults, ...overrides };

// Copy
const copy = [...original];
const objCopy = { ...original };

// Rest — collect remaining into array
function sum(first, ...rest) {
  return first + rest.reduce((a, b) => a + b, 0);
}

const [head, ...tail] = [1, 2, 3, 4]; // head=1, tail=[2,3,4]
const { a, ...remaining } = obj;
```

---

## 19. ES6 Classes & Inheritance

```js
class Animal {
  constructor(name, sound) {
    this.name = name;
    this.sound = sound;
  }

  speak() {
    return `${this.name} says ${this.sound}`;
  }

  static create(name) {  // called on CLASS, not instance
    return new Animal(name, "...");
  }
}

class Dog extends Animal {
  constructor(name) {
    super(name, "Woof"); // must call super first
    this.tricks = [];
  }

  learn(trick) {
    this.tricks.push(trick);
  }

  speak() {
    return super.speak() + "!"; // override + call parent
  }
}

const dog = new Dog("Rex");
dog.speak();           // "Rex says Woof!"
dog instanceof Dog;    // true
dog instanceof Animal; // true
```

---

## 20. Error Handling

```js
try {
  const data = JSON.parse(invalidJson); // throws SyntaxError
  riskyOperation();
} catch (error) {
  console.error(error.name);    // "SyntaxError"
  console.error(error.message); // description
  console.error(error.stack);   // full trace
} finally {
  cleanup(); // ALWAYS runs
}

// Custom throw
function divide(a, b) {
  if (b === 0) throw new Error("Cannot divide by zero");
  return a / b;
}

// Custom error type
class ValidationError extends Error {
  constructor(message) {
    super(message);
    this.name = "ValidationError";
  }
}

try {
  throw new ValidationError("Email is required");
} catch (e) {
  if (e instanceof ValidationError) console.log("Validation:", e.message);
  else throw e; // re-throw unknown errors
}
```

---

## 21. ES Modules

```js
// Named exports
export const PI = 3.14;
export function add(a, b) { return a + b; }
export class User { }

// Default export (one per file)
export default function greet(name) { return `Hello ${name}`; }

// Import named
import { PI, add } from "./math.js";
import { add as sum } from "./math.js"; // alias

// Import default (any name)
import greet from "./greet.js";

// Import all
import * as MathUtils from "./math.js";
MathUtils.add(1, 2);

// Import both
import greet, { PI, add } from "./module.js";
```

---

## 22. `this`, bind, call, apply

### `this` Rules
```js
// In a method → this = the object
const person = {
  name: "Alice",
  greet() { return `Hi I'm ${this.name}`; }
};

// In regular function → this = window (or undefined in strict mode)
function show() { console.log(this); }

// Arrow functions → NO own 'this', inherits from surrounding scope
const obj = {
  name: "Alice",
  greet: () => console.log(this.name), // this = outer scope (NOT obj) ❌
  hello() {
    const inner = () => console.log(this.name); // this = obj ✅
    inner();
  }
};
```

### call, apply, bind
```js
function greet(greeting, punctuation) {
  return `${greeting}, ${this.name}${punctuation}`;
}
const user = { name: "Alice" };

// call — invoke immediately, spread args
greet.call(user, "Hello", "!");     // "Hello, Alice!"

// apply — invoke immediately, args as array
greet.apply(user, ["Hello", "!"]); // "Hello, Alice!"

// bind — returns new function (doesn't invoke)
const greetAlice = greet.bind(user);
greetAlice("Hey", ".");            // "Hey, Alice."

// Fix 'this' in event handlers / setTimeout
class Timer {
  start() {
    setTimeout(this.tick.bind(this), 1000);
  }
  tick() { console.log("tick"); }
}
```

---

## 23. JSON & localStorage

```js
// JSON
const obj = { name: "Alice", age: 25 };
const jsonStr = JSON.stringify(obj);       // '{"name":"Alice","age":25}'
const parsed  = JSON.parse(jsonStr);       // back to object
JSON.stringify(obj, null, 2);              // pretty print

// localStorage (persists across sessions — string only)
localStorage.setItem("user", JSON.stringify({ name: "Alice" }));
const user = JSON.parse(localStorage.getItem("user"));
localStorage.removeItem("user");
localStorage.clear();

// sessionStorage (cleared when tab closes)
sessionStorage.setItem("token", "abc123");
```

---

## 24. Object Utility Methods

```js
const person = { name: "Alice", age: 25, city: "Delhi" };

Object.keys(person)    // ["name", "age", "city"]
Object.values(person)  // ["Alice", 25, "Delhi"]
Object.entries(person) // [["name","Alice"], ["age",25], ["city","Delhi"]]

// Iterate
Object.entries(person).forEach(([key, val]) => {
  console.log(`${key}: ${val}`);
});

// Check property
"name" in person               // true
person.hasOwnProperty("name")  // true

// Freeze / Seal
Object.freeze(person); // cannot change any property
Object.seal(person);   // can change values, not add/delete

// From entries
const obj = Object.fromEntries([["a", 1], ["b", 2]]); // {a:1, b:2}
```

---

## 🔑 Quick Reference Cheatsheet

| Concept | Key Point |
|---------|-----------|
| `var` | function-scoped, hoisted as `undefined`, avoid |
| `let` | block-scoped, TDZ, can reassign |
| `const` | block-scoped, TDZ, cannot reassign |
| Hoisting | var → `undefined`, functions → full code, let/const → TDZ |
| Closure | function remembers outer scope even after outer fn returns |
| Event Loop | Call Stack empty? → Microtask queue first → Task queue |
| `==` vs `===` | loose vs strict (always use `===`) |
| Arrow fn | no own `this`, shorter syntax |
| Spread `...` | expand / copy arrays & objects |
| Rest `...` | collect remaining args into array |
| `?.` | optional chaining — safe property access |
| `??` | nullish coalescing — fallback for `null`/`undefined` only |
| Promise | 3 states: pending, fulfilled, rejected |
| `async/await` | syntactic sugar over Promises |
| `map` | transform → new array |
| `filter` | keep elements → new array |
| `reduce` | collapse → single value |

---

*Notes based on Namaste JavaScript by Akshay Saini 🙏*
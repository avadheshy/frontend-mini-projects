# JavaScript — Notes

---

## Table of Contents
- [JavaScript — Notes](#javascript--notes)
  - [Table of Contents](#table-of-contents)
  - [1. How JS Works — Execution Context](#1-how-js-works--execution-context)
    - [Two Phases of Context Creation:](#two-phases-of-context-creation)
  - [2. Call Stack \& Hoisting](#2-call-stack--hoisting)
    - [Call Stack](#call-stack)
    - [Hoisting](#hoisting)
  - [3. Variables — var, let, const](#3-variables--var-let-const)
    - [let \& const — Block Scope](#let--const--block-scope)
    - [Temporal Dead Zone (TDZ) / Dead Zone](#temporal-dead-zone-tdz--dead-zone)
    - [Syntax Errors vs Type Errors](#syntax-errors-vs-type-errors)
    - [Shadowing](#shadowing)
  - [4. Scope, Scope Chain \& Lexical Environment](#4-scope-scope-chain--lexical-environment)
    - [Scope Chain](#scope-chain)
    - [Lexical Environment](#lexical-environment)
    - [`undefined` vs `not defined`](#undefined-vs-not-defined)
    - [JS is Loosely Typed](#js-is-loosely-typed)
  - [5. Closures](#5-closures)
    - [Block Scope also gives Closure](#block-scope-also-gives-closure)
    - [setTimeout + Closure Interview Question](#settimeout--closure-interview-question)
    - [Uses of Closures](#uses-of-closures)
  - [6. First Class Functions](#6-first-class-functions)
    - [Types of Functions](#types-of-functions)
    - [Parameters vs Arguments](#parameters-vs-arguments)
    - [Difference: Function Statement vs Expression](#difference-function-statement-vs-expression)
    - [Functions as First Class Citizens](#functions-as-first-class-citizens)
  - [7. Callback Functions \& Event Loop](#7-callback-functions--event-loop)
    - [Callback Function](#callback-function)
    - [Callback Hell](#callback-hell)
    - [Web APIs (provided by browser, not JS)](#web-apis-provided-by-browser-not-js)
    - [Event Loop — How Async Works](#event-loop--how-async-works)
    - [Task Queue vs Microtask Queue](#task-queue-vs-microtask-queue)
  - [8. JS Engine Internals](#8-js-engine-internals)
    - [JS Engine = JIT Compiler](#js-engine--jit-compiler)
    - [Memory in JS Engine](#memory-in-js-engine)
    - [Inline Caching](#inline-caching)
  - [9. Higher Order Functions — map / filter / reduce](#9-higher-order-functions--map--filter--reduce)
    - [map — transform each element, returns new array](#map--transform-each-element-returns-new-array)
    - [filter — keep elements that pass a test](#filter--keep-elements-that-pass-a-test)
    - [reduce — collapse to a single value](#reduce--collapse-to-a-single-value)
    - [Chaining (map + filter together)](#chaining-map--filter-together)
    - [Polyfill for map (How map works internally)](#polyfill-for-map-how-map-works-internally)
  - [10. Primitive \& Reference Types](#10-primitive--reference-types)
    - [Primitive Types (copied by value)](#primitive-types-copied-by-value)
    - [Reference Types (copied by reference)](#reference-types-copied-by-reference)
    - [Shallow Copy vs Deep Copy](#shallow-copy-vs-deep-copy)
    - [typeof](#typeof)
  - [11. Operators](#11-operators)
  - [12. Conditions \& Loops](#12-conditions--loops)
  - [13. Objects \& Functions (Deep Dive)](#13-objects--functions-deep-dive)
    - [Objects](#objects)
    - [Getter \& Setter](#getter--setter)
    - [Built-in — Math \& String](#built-in--math--string)
  - [14. Arrays \& Array Methods](#14-arrays--array-methods)
  - [15. DOM Manipulation](#15-dom-manipulation)
    - [Selecting Elements](#selecting-elements)
    - [Reading / Changing Content](#reading--changing-content)
    - [Attributes \& Styles](#attributes--styles)
    - [Create / Add / Remove Elements](#create--add--remove-elements)
  - [16. Events](#16-events)
    - [Event Phases](#event-phases)
    - [Event Delegation (efficient pattern)](#event-delegation-efficient-pattern)
    - [Prototype Inheritance](#prototype-inheritance)
  - [17. Async JS — Promises \& Async/Await](#17-async-js--promises--asyncawait)
    - [Promises](#promises)
    - [Async / Await](#async--await)
    - [Fetch API](#fetch-api)
    - [setTimeout](#settimeout)
  - [18. Destructuring, Spread \& Rest](#18-destructuring-spread--rest)
    - [Destructuring](#destructuring)
    - [Spread \& Rest](#spread--rest)
  - [19. ES6 Classes \& Inheritance](#19-es6-classes--inheritance)
    - [Constructor](#constructor)
    - [Class](#class)
  - [20. Error Handling](#20-error-handling)
  - [21. ES Modules](#21-es-modules)
  - [22. `this`, bind, call, apply](#22-this-bind-call-apply)
    - [`this` Rules](#this-rules)
    - [call, apply, bind](#call-apply-bind)
  - [23. JSON \& localStorage](#23-json--localstorage)
  - [24. Object Utility Methods](#24-object-utility-methods)
  - [25. Currying](#25-currying)
  - [26. IIFE](#26-iife)
  - [27. Prototype \& Prototype Inheritance](#27-prototype--prototype-inheritance)
  - [28. Memoization](#28-memoization)
  - [29. Polyfills](#29-polyfills)
  - [30. Debouncing](#30-debouncing)
  - [31. Mutation Observer](#31-mutation-observer)
  - [32. Memory Leak](#32-memory-leak)
  - [33. Recursive Functions](#33-recursive-functions)
  - [Quick Reference Cheatsheet](#quick-reference-cheatsheet)

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

> In hoisting, we can access the value before declaration. Only `var` we can use — `let`/`const` give a ReferenceError (Dead Zone).

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

### Temporal Dead Zone (TDZ) / Dead Zone
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
- A variable in a smaller scope **overwrites** (shadows) the one in the larger scope.

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
- Inner functions have access to outer function's variables (**Lexical Scope**).

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

> A **closure** is created when a function is defined inside another function, and the inside function can access the variables of the outside function. It **remembers** variables from its outer (lexical) scope even after the outer function has returned.

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

### setTimeout + Closure Interview Question
```js
// var — all callbacks share the SAME 'i' (prints 6,6,6,6,6)
function x() {
  for (var i = 1; i <= 5; i++) {
    setTimeout(function() {
      console.log(i); // all print 6
    }, i * 1000);
  }
}

// let — each iteration gets its OWN 'i' (prints 1,2,3,4,5)
function x() {
  for (let i = 1; i <= 5; i++) {
    setTimeout(function() {
      console.log(i); // 1, 2, 3, 4, 5
    }, i * 1000);
  }
}

// Fix with var using closure
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
// 1. Function Statement (aka Function Declaration) — hoisted
function a() {
  console.log("a called");
}

// 2. Function Expression — NOT hoisted
var b = function(param1) {
  return function xyz() {};
};

// 3. Anonymous Function — no name, used as a value
var fn = function() { console.log("anonymous"); };
// Often used in callbacks:
setTimeout(function() {
  console.log("Hey");
}, 200);

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

// 6. Named Function — reusable with a specific name
function greet(name) {
  return `Hello, ${name}`;
}
console.log(greet("Satyam"));

// 7. IIFE — see section 26
```

### Parameters vs Arguments
```js
function add(a, b) { }  // a, b → parameters (inside function definition)
add(5, 10);             // 5, 10 → arguments (values passed while calling)
```

### Difference: Function Statement vs Expression
| Feature | Function Statement | Function Expression |
|---------|-------------------|---------------------|
| Hoisted | Yes | No |
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

### Callback Hell
> Occurs when you have **nested callbacks**, making the code difficult to read and maintain.

```js
// Example of callback hell (pyramid of doom)
getData(function(a) {
  getMoreData(a, function(b) {
    getEvenMore(b, function(c) {
      // deeply nested — hard to read & maintain
    });
  });
});
// Solution: use Promises or async/await
```

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

> **Event Loop** is a mechanism that enables JavaScript, being single-threaded, to handle asynchronous operations efficiently.

### Task Queue vs Microtask Queue
- **Microtask Queue** (higher priority):
  - Promise callbacks (`.then`, `.catch`, `.finally`)
  - `queueMicrotask()`
  - `MutationObserver`
  - A special queue for asynchronous callback functions that should be executed immediately after the current task.
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

---

## 8. JS Engine Internals

### JS Engine = JIT Compiler
1. **Parsing** → reads JS code
2. **Compilation** → combination of compilation & interpretation
3. **Execution**

### Memory in JS Engine
- **Memory Heap** — a global object, shared space where functions & variables are stored
- **Call Stack** — space where functions are executed in order (shared)
- **Garbage Collector** — clears unused memory using **Mark & Sweep** algorithm

### Inline Caching
- Used to speed up property access on objects.

---

## 9. Higher Order Functions — map / filter / reduce

> A **Higher Order Function** is a function that takes another function as an argument OR returns a function.

### map — transform each element, returns new array
```js
const arr = [5, 1, 3, 2, 6];

const doubled = arr.map(x => x * 2);  // [10, 2, 6, 4, 12]
const binary  = arr.map(x => x.toString(2)); // binary strings
const squared = arr.map(x => x * x);
```

### filter — keep elements that pass a test
```js
// filter performs the condition on each element of an array
const output = arr.filter(x => x % 2 === 0); // [2, 6]
const odds   = arr.filter(x => x % 2 !== 0);
```

### reduce — collapse to a single value
```js
// reduce reduces the array to a single value — it returns only one single value
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
Array.prototype.calculate = function(logic) {
  const output = [];
  for (let i = 0; i < this.length; i++) {
    output.push(logic(this[i]));
  }
  return output;
};
// radius.calculate(area)  ←→  radius.map(area)
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
let obj1 = { x: 1 };
let obj2 = obj1; // SAME reference
obj2.x = 99;
console.log(obj1.x); // 99 — both changed!
```

### Shallow Copy vs Deep Copy

**Shallow Copy** — creates a new object/array but copies the **reference** for nested objects. If the value changes, the original also changes.

```js
// Shallow copy methods
const clone1 = Object.assign({}, obj1);
const clone2 = { ...obj1 };             // spread (shallow)
const arrCopy = [...originalArr];

// Problem with shallow copy and nested objects:
const obj = { a: 1, nested: { b: 2 } };
const shallow = { ...obj };
shallow.nested.b = 99;
console.log(obj.nested.b); // 99 — original affected!
```

**Deep Copy** — copies the values, not the references. Changing the copy will **not** change the original.

```js
// Deep copy methods
const deep1 = JSON.parse(JSON.stringify(obj)); // simple but loses functions/undefined
const deep2 = structuredClone(obj);            // modern, recommended
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

Array.isArray([]);  // true  (better way to check arrays)
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
===  // strict (no coercion): "5" === 5 → false

// Ternary
let result = age >= 18 ? "adult" : "minor";

// Logical
&&  // AND
||  // OR
!   // NOT

// Fallback / Short-circuit
let name = user.name || "Guest";  // fallback for all falsy values
let val  = a ?? "default";        // fallback only for null/undefined

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
1. **Capture** — event travels window → target (top down). The click event triggers on the root first, then occurs to the target.
2. **Target** — event is at the element.
3. **Bubble** — event travels target → window (bottom up, default). The event first triggers on the target element and then occurs to the root.

### Event Delegation (efficient pattern)
```js
// Add ONE listener to parent instead of each child
// One event listener handles many elements efficiently
ul.addEventListener("click", (e) => {
  console.log(e.target.textContent);
});
```

### Prototype Inheritance
> Allows an **object to inherit properties and methods from another object**.

```js
const animal = {
  speak() { return "Some sound"; }
};

const dog = Object.create(animal); // dog inherits from animal
dog.speak(); // "Some sound"
```

---

## 17. Async JS — Promises & Async/Await

### Promises
> A **Promise** is an object representing the future result of an asynchronous operation.

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

### Async / Await
> `async/await` simply allows us to write Promise-based code as if it were synchronous. An `async` function will **always return a Promise**. `await` is used to wait for the Promise.

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

**Spread Operator** — used to **copy or merge** arrays/objects.

**Rest Operator** — used to **collect multiple elements** into a single array or object passed as function arguments.

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

### Constructor
> A **constructor** is a special method in a class. It is automatically called when a new object is created using `new`. Used to initialize the object's properties.

### Class
> A **class** is a blueprint for creating objects with predefined properties and methods.

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
```

---

## 21. ES Modules

```js
// Named exports — one can have multiple named exports per file
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
  greet: () => console.log(this.name), // this = outer scope (NOT obj)
  hello() {
    const inner = () => console.log(this.name); // this = obj
    inner();
  }
};
```

### call, apply, bind

**call** — immediately invokes the function. Allows passing a single argument.

**apply** — same as `call` but pass the arguments into an array.

**bind** — does **not** immediately call the function. It is used to invoke it in the future.

```js
function greet(greeting, punctuation) {
  return `${greeting}, ${this.name}${punctuation}`;
}
const user = { name: "Alice" };

greet.call(user, "Hello", "!");     // "Hello, Alice!" — immediate
greet.apply(user, ["Hello", "!"]); // "Hello, Alice!" — immediate, args as array
const greetAlice = greet.bind(user); // returns new function — NOT immediate
greetAlice("Hey", ".");            // "Hey, Alice."
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

## 25. Currying

> **Currying** is a technique of converting a function that takes **multiple arguments** into a sequence of functions that each take a **single argument**.

```js
// Normal function
function multiply(a, b) {
  return a * b;
}

// Curried version
function curriedAdd(a) {
  return function(b) {
    return a * b;
  };
}

console.log(curriedAdd(2)(3)); // 6

// Arrow function style
const curry = a => b => a * b;
console.log(curry(2)(3)); // 6
```

**Use cases:** partial application, reusable utility functions, functional composition.

---

## 26. IIFE

> **IIFE** (Immediately Invoked Function Expression) — a function that **executes immediately** after being defined.

```js
(function() {
  console.log("Hello");
})();

// Arrow IIFE
(() => {
  console.log("Arrow IIFE");
})();

// With parameters
(function(name) {
  console.log(`Hello ${name}`);
})("Alice");
```

**Use cases:** avoid polluting global scope, module-like encapsulation.

---

## 27. Prototype & Prototype Inheritance

> **Prototype** — JavaScript's way of **sharing features across objects**.

> **Prototype Inheritance** — allows an object to **inherit properties and methods from another object**.

```js
function Animal(name) {
  this.name = name;
}
Animal.prototype.speak = function() {
  return `${this.name} makes a sound.`;
};

const dog = new Animal("Rex");
dog.speak(); // "Rex makes a sound." — inherited via prototype

// Check prototype chain
dog.__proto__ === Animal.prototype; // true

// Object.create
const proto = {
  greet() { return `Hello, I'm ${this.name}`; }
};
const obj = Object.create(proto);
obj.name = "Alice";
obj.greet(); // "Hello, I'm Alice"
```

Every JS object has a `[[Prototype]]` (accessible via `__proto__`). This forms the **prototype chain** — how JS looks up properties.

---

## 28. Memoization

> **Memoization** is an optimization technique that **stores the results of expensive function calls** so that the same input doesn't need to be recalculated.

```js
function memoize(fn) {
  const cache = {};
  return function(...args) {
    const key = JSON.stringify(args);
    if (cache[key] !== undefined) {
      console.log("From cache");
      return cache[key];
    }
    cache[key] = fn(...args);
    return cache[key];
  };
}

function slowSquare(n) {
  // imagine this is expensive
  return n * n;
}

const fastSquare = memoize(slowSquare);
fastSquare(5); // computed
fastSquare(5); // From cache → 25
```

---

## 29. Polyfills

> A **polyfill** is a piece of code that **provides support for modern features on older browsers** that don't natively support them.

```js
// Polyfill for Array.prototype.map
if (!Array.prototype.myMap) {
  Array.prototype.myMap = function(callback) {
    const result = [];
    for (let i = 0; i < this.length; i++) {
      result.push(callback(this[i], i, this));
    }
    return result;
  };
}

// Polyfill for Array.prototype.filter
if (!Array.prototype.myFilter) {
  Array.prototype.myFilter = function(callback) {
    const result = [];
    for (let i = 0; i < this.length; i++) {
      if (callback(this[i], i, this)) result.push(this[i]);
    }
    return result;
  };
}
```

---

## 30. Debouncing

> **Debouncing** — delays a function from running until the **user stops typing or clicking** for a set amount of time.

```js
function debounce(fn, delay) {
  let timer;
  return function(...args) {
    clearTimeout(timer);
    timer = setTimeout(() => fn.apply(this, args), delay);
  };
}

const handleSearch = debounce((query) => {
  console.log("Searching:", query);
}, 300);

// handleSearch fires only 300ms after user stops typing
input.addEventListener("input", e => handleSearch(e.target.value));
```

**Use cases:** search inputs, resize handlers, button click throttling.

---

## 31. Mutation Observer

> **Mutation Observer** — detects DOM changes dynamically. It **observes and reacts** when nodes are added or removed.

```js
const observer = new MutationObserver((mutations) => {
  mutations.forEach(mutation => {
    console.log("DOM changed:", mutation.type);
    console.log("Added nodes:", mutation.addedNodes);
    console.log("Removed nodes:", mutation.removedNodes);
  });
});

observer.observe(document.body, {
  childList: true,   // watch for added/removed children
  subtree: true      // watch all descendants
});

// Stop observing
observer.disconnect();
```

---

## 32. Memory Leak

> A **memory leak** occurs when **unused data stays in memory** and slows down the app.

**Common causes:**
- Forgotten `setInterval` / `setTimeout` without `clearInterval` / `clearTimeout`
- Event listeners not removed after use
- Closures holding references to large objects
- Global variables accumulating data

```js
// Memory leak example
let arr = [];
setInterval(() => {
  arr.push(new Array(1000).fill("data")); // keeps growing, never cleared
}, 100);

// Fix: clear when done
const id = setInterval(() => { /* ... */ }, 100);
clearInterval(id); // when no longer needed
```

---

## 33. Recursive Functions

> A **recursive function** is a function that **calls itself** to solve problems like factorials, tree traversal, etc.

```js
// Factorial
function factorial(n) {
  if (n <= 1) return 1;         // base case
  return n * factorial(n - 1);  // recursive call
}
factorial(5); // 120

// Sum of array
function sum(arr) {
  if (arr.length === 0) return 0;
  return arr[0] + sum(arr.slice(1));
}
```

Every recursive function needs a **base case** to avoid infinite recursion.

---

## Quick Reference Cheatsheet

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
| Currying | multi-arg fn → sequence of single-arg fns |
| IIFE | executes immediately after definition |
| Prototype | JS way to share features across objects |
| Memoization | cache results of expensive function calls |
| Polyfill | code to support modern features on old browsers |
| Debouncing | delay fn until user stops interacting |
| Shallow Copy | copies reference — nested changes affect original |
| Deep Copy | copies values — nested changes don't affect original |
| Callback Hell | nested callbacks making code unreadable |
| Memory Leak | unused data stays in memory, slows app |
| Recursion | function calls itself; needs a base case |
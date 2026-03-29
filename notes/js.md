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
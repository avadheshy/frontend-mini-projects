# React Notes ⚛️

---

## Table of Contents
- [React Notes ⚛️](#react-notes-️)
  - [Table of Contents](#table-of-contents)
  - [1. Library vs Framework](#1-library-vs-framework)
  - [2. Build Tools — Parcel / Webpack](#2-build-tools--parcel--webpack)
    - [Tree Shaking](#tree-shaking)
    - [Hot Module Replacement (HMR)](#hot-module-replacement-hmr)
    - [`dist` Folder](#dist-folder)
    - [Babel](#babel)
  - [3. Package.json Concepts](#3-packagejson-concepts)
    - [Dependencies vs DevDependencies](#dependencies-vs-devdependencies)
    - [Version Symbols](#version-symbols)
    - [config.js](#configjs)
  - [4. What is React?](#4-what-is-react)
  - [5. Setup](#5-setup)
  - [6. Components](#6-components)
  - [7. JSX Rules](#7-jsx-rules)
  - [8. Props (Parent → Child)](#8-props-parent--child)
  - [9. State — useState](#9-state--usestate)
  - [10. Events](#10-events)
    - [preventDefault](#preventdefault)
  - [11. Controlled vs Uncontrolled Components](#11-controlled-vs-uncontrolled-components)
    - [Controlled Components (Forms)](#controlled-components-forms)
  - [12. useEffect Hook](#12-useeffect-hook)
  - [13. Passing Data Child → Parent (via function props)](#13-passing-data-child--parent-via-function-props)
  - [14. Lists \& Keys](#14-lists--keys)
  - [15. React Router DOM](#15-react-router-dom)
    - [Navigation](#navigation)
  - [16. Context API (Global State)](#16-context-api-global-state)
  - [17. Redux (RTK — Redux Toolkit)](#17-redux-rtk--redux-toolkit)
  - [18. useRef Hook](#18-useref-hook)
  - [19. useReducer Hook](#19-usereducer-hook)
  - [20. useMemo \& useCallback (Performance)](#20-usememo--usecallback-performance)
  - [21. React.memo (Prevent Re-renders)](#21-reactmemo-prevent-re-renders)
  - [22. Custom Hooks](#22-custom-hooks)
  - [23. Data Fetching Pattern](#23-data-fetching-pattern)
  - [24. React.lazy \& Suspense (Code Splitting)](#24-reactlazy--suspense-code-splitting)
  - [25. Lifting State Up](#25-lifting-state-up)
  - [26. Key Prop — Why It Matters](#26-key-prop--why-it-matters)
  - [27. React Internals — Fragment, Reconciliation, Fiber](#27-react-internals--fragment-reconciliation-fiber)
    - [React Fragment](#react-fragment)
    - [Reconciliation](#reconciliation)
    - [React Fiber](#react-fiber)
    - [super(props)](#superprops)
  - [28. Exports — Named vs Default](#28-exports--named-vs-default)
    - [Named Export](#named-export)
    - [Default Export](#default-export)
  - [29. HOC — Higher Order Component](#29-hoc--higher-order-component)
  - [30. SPA, SSR, CSR](#30-spa-ssr-csr)
    - [SPA (Single Page Application)](#spa-single-page-application)
    - [SSR (Server-Side Rendering)](#ssr-server-side-rendering)
    - [CSR (Client-Side Rendering)](#csr-client-side-rendering)
  - [31. Microservices](#31-microservices)
  - [32. State Management — When to Use What?](#32-state-management--when-to-use-what)
  - [Quick Reference Cheatsheet](#quick-reference-cheatsheet)

---

## 1. Library vs Framework

**Library** — a collection of packages that perform specific operations. You are in control; you call the library.

**Framework** — a set of pre-written code that provides a structure for developing software applications. The framework is in control; it calls your code.

> React is a **library**, not a framework.

---

## 2. Build Tools — Parcel / Webpack

**Parcel / Webpack** — types of web application bundlers used for **development and production** purposes with different features.

| Feature | Description |
|---------|-------------|
| Code Splitting | Split code into smaller chunks loaded on demand |
| Hot Module Replacement | Exchange/add/remove modules while app is running without full reload |
| Image Optimization | Compress and optimize assets |
| Cleaning Code | Remove unused/dead code |

### Tree Shaking
> The process of **removing unwanted/dead code** that is not used while developing the application.

### Hot Module Replacement (HMR)
> It **exchanges, adds, or removes modules** while an application is running without a full reload — making development faster.

### `dist` Folder
> Contains the code present in the `dist` folder — this is the actual code **used in production**.

### Babel
> **Babel** is a JavaScript compiler responsible for **transforming modern JS syntax into code that can be understood by older browsers**.

---

## 3. Package.json Concepts

### Dependencies vs DevDependencies
- **Dependencies** — should contain the library and framework in which your app is built on and needs in production.
- **DevDependencies** — should contain modules/packages that a developer needs during development only (e.g., testing tools, bundlers, linters).

### Version Symbols
| Symbol | Meaning |
|--------|---------|
| `~` (Tilde) | Use for **minor version** changes only |
| `^` (Caret) | Use for **minor or big version** changes |

Example: `"react": "^18.2.0"` — allows updates to 18.x.x but not 19.x.x

### config.js
> Serves as a **centralized location to store configuration settings and parameters** that influence the application's behavior.

---

## 4. What is React?

React is a **JavaScript library** for building UIs.

**Imperative (vanilla JS) vs Declarative (React):**
- Imperative → tell the browser *how* to do it step by step
- Declarative → tell React *what* you want, it figures out the how

**Key idea:** React is all about **components** — reusable pieces of UI (custom HTML creators).

---

## 5. Setup

```bash
# Create a new React app
npm create vite@latest my-app -- --template react
cd my-app
npm install
npm run dev
```

`index.js` (or `main.jsx`) is the **entry point** — it mounts the root component into `index.html`.

---

## 6. Components

```jsx
// Functional component (always start with capital letter)
function Greeting() {
  return <h1>Hello, World!</h1>;
}

// Arrow function style
const Greeting = () => {
  return <h1>Hello, World!</h1>;
};

// Export and use
export default Greeting;

// In another file
import Greeting from "./Greeting";
function App() {
  return <Greeting />;
}
```

---

## 7. JSX Rules

```jsx
// 1. Return a single root element (use <> fragment if needed)
return (
  <>
    <h1>Title</h1>
    <p>Paragraph</p>
  </>
);

// 2. JS expressions use {}
return <p>Hello {name.toUpperCase()}</p>;

// 3. class → className
<div className="container">

// 4. Self-close tags
<img src="photo.jpg" />
<br />
```

---

## 8. Props (Parent → Child)

> **Props** are arguments passed into React components. Props are used in React to **pass data from one component to another**.

```jsx
// Parent passes data
function App() {
  return <Card title="React" author="Alice" />;
}

// Child receives via props
function Card({ title, author }) {  // destructuring
  return (
    <div>
      <h2>{title}</h2>
      <p>By {author}</p>
    </div>
  );
}

// Default props
function Card({ title = "Untitled" }) { ... }
```

---

## 9. State — useState

> **useState** is used to contain data about the component and can **change over time**.

```jsx
import { useState } from "react";

function Counter() {
  const [count, setCount] = useState(0);  // [value, updater]

  return (
    <div>
      <p>{count}</p>
      <button onClick={() => setCount(count + 1)}>+</button>
    </div>
  );
}
```

> When state changes, React **re-renders** the component automatically.

---

## 10. Events

Events in React use camelCase and pass a function reference:

```jsx
// Click
<button onClick={handleClick}>Click me</button>
<button onClick={() => doSomething(id)}>Click</button>

// Input
<input onChange={(e) => setName(e.target.value)} />

// Form — preventDefault stops the browser's default behaviour
<form onSubmit={(e) => { e.preventDefault(); handleSubmit(); }}>
```

### preventDefault
> Used within event handlers to **stop the browser's default behaviour** (e.g., stopping a form from reloading the page on submit).

---

## 11. Controlled vs Uncontrolled Components

**Controlled** — the form data is handled by a **React component's state**.

**Uncontrolled** — the form data is handled by the **DOM itself**.

### Controlled Components (Forms)
React manages form state instead of the DOM.

```jsx
function LoginForm() {
  const [form, setForm] = useState({ email: "", password: "" });

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setForm(prev => ({
      ...prev,
      [name]: type === "checkbox" ? checked : value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(form);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input name="email"    value={form.email}    onChange={handleChange} />
      <input name="password" value={form.password} onChange={handleChange} type="password" />

      {/* Checkbox */}
      <input name="remember" type="checkbox" checked={form.remember} onChange={handleChange} />

      {/* Radio */}
      <input name="role" type="radio" value="admin" checked={form.role === "admin"} onChange={handleChange} />

      {/* Dropdown */}
      <select name="country" value={form.country} onChange={handleChange}>
        <option value="in">India</option>
        <option value="us">USA</option>
      </select>

      <button type="submit">Submit</button>
    </form>
  );
}
```

---

## 12. useEffect Hook

> **useEffect** — to manage side effects like API calls.

Runs **after** the component renders. 4 variations:

```jsx
import { useEffect } from "react";

// 1. Runs after EVERY render
useEffect(() => {
  console.log("rendered");
});

// 2. Runs only on FIRST render (mount)
useEffect(() => {
  fetchData();
}, []);

// 3. Runs on first render + when dependency changes
useEffect(() => {
  fetchUser(userId);
}, [userId]);

// 4. Cleanup on UNMOUNT
useEffect(() => {
  const timer = setInterval(() => {}, 1000);
  return () => clearInterval(timer);  // cleanup function
}, []);
```

---

## 13. Passing Data Child → Parent (via function props)

```jsx
function Child({ onSendData }) {
  return <button onClick={() => onSendData("Hello from child!")}>Send</button>;
}

function Parent() {
  const [msg, setMsg] = useState("");
  return (
    <div>
      <Child onSendData={(data) => setMsg(data)} />
      <p>{msg}</p>
    </div>
  );
}
```

---

## 14. Lists & Keys

```jsx
const items = ["Apple", "Banana", "Mango"];

return (
  <ul>
    {items.map((item, index) => (
      <li key={index}>{item}</li>  // key must be unique
    ))}
  </ul>
);
```

---

## 15. React Router DOM

```bash
npm install react-router-dom
```

```jsx
// main.jsx
import { BrowserRouter } from "react-router-dom";
<BrowserRouter><App /></BrowserRouter>

// App.jsx
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <Routes>
      <Route path="/"         element={<Home />} />
      <Route path="/about"    element={<About />} />
      <Route path="/user/:id" element={<UserDetail />} />
      {/* Nested routes */}
      <Route path="/dashboard" element={<Dashboard />}>
        <Route index         element={<DashHome />} />
        <Route path="settings" element={<Settings />} />
      </Route>
    </Routes>
  );
}
```

### Navigation
```jsx
import { NavLink, useNavigate, useParams } from "react-router-dom";

// NavLink (adds 'active' class automatically)
<NavLink to="/about" className={({ isActive }) => isActive ? "active" : ""}>
  About
</NavLink>

// Programmatic navigation
const navigate = useNavigate();
navigate("/home");
navigate(-1); // go back

// URL params
const { id } = useParams();

// Nested route — render child routes here
import { Outlet } from "react-router-dom";
<Outlet />
```

---

## 16. Context API (Global State)

Avoid **prop drilling** (passing props through many levels).

> **Props Drilling** — basically a situation when the same data is being sent at almost every level until the final level.

```jsx
// 1. Create context
import { createContext, useContext, useState } from "react";
export const ThemeContext = createContext();

// 2. Provide it (wrap components that need it)
function App() {
  const [theme, setTheme] = useState("light");
  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      <MyComponent />
    </ThemeContext.Provider>
  );
}

// 3. Consume in any child component
function MyComponent() {
  const { theme, setTheme } = useContext(ThemeContext);
  return <div className={theme}>Current theme: {theme}</div>;
}
```

> **useContext** — to return the current value for a context.

**Prop drilling** = parent→child→grandchild (tedious)  
**Context** = any component can access without passing through every level

---

## 17. Redux (RTK — Redux Toolkit)

```bash
npm install @reduxjs/toolkit react-redux
```

**Core concepts:**
- **Store** — single object holding all app state
- **Slice** — a piece of state + its reducers
- **Action** — a plain JavaScript object that describes what should change in the application state
- **Reducer** — specifies how the state should change in response to the action
- **Dispatch** — used to send actions to the store
- **Selector** — a function that extracts specific pieces of data from the Redux store

```jsx
// counterSlice.js
import { createSlice } from "@reduxjs/toolkit";

const counterSlice = createSlice({
  name: "counter",
  initialState: { value: 0 },
  reducers: {
    increment: (state) => { state.value += 1; },
    decrement: (state) => { state.value -= 1; },
    addBy:     (state, action) => { state.value += action.payload; }
  }
});

export const { increment, decrement, addBy } = counterSlice.actions;
export default counterSlice.reducer;

// store.js
import { configureStore } from "@reduxjs/toolkit";
import counterReducer from "./counterSlice";
export const store = configureStore({ reducer: { counter: counterReducer } });

// main.jsx
import { Provider } from "react-redux";
<Provider store={store}><App /></Provider>

// In component
import { useSelector, useDispatch } from "react-redux";
import { increment } from "./counterSlice";

function Counter() {
  const count = useSelector(state => state.counter.value); // Selector
  const dispatch = useDispatch();
  return (
    <button onClick={() => dispatch(increment())}>
      Count: {count}
    </button>
  );
}
```

---

## 18. useRef Hook

> `useRef` gives you a **mutable box** that doesn't trigger re-renders when changed.

```jsx
import { useRef } from "react";

// 1. Access DOM element directly
function TextInput() {
  const inputRef = useRef(null);
  const focusInput = () => inputRef.current.focus();
  return (
    <>
      <input ref={inputRef} type="text" />
      <button onClick={focusInput}>Focus</button>
    </>
  );
}

// 2. Store a value that persists between renders WITHOUT causing re-render
function Timer() {
  const timerIdRef = useRef(null);
  const start = () => {
    timerIdRef.current = setInterval(() => console.log("tick"), 1000);
  };
  const stop = () => clearInterval(timerIdRef.current);
  return <><button onClick={start}>Start</button><button onClick={stop}>Stop</button></>;
}
```

**`useRef` vs `useState`:**
- `useState` → triggers re-render when value changes
- `useRef` → value persists but does NOT trigger re-render

---

## 19. useReducer Hook

> **useReducer** — a `useState` alternative to help with **complex state management**.

Better than `useState` for complex state logic (multiple sub-values, or next state depends on previous).

```jsx
import { useReducer } from "react";

// 1. Define reducer (pure function)
function reducer(state, action) {
  switch (action.type) {
    case "increment": return { count: state.count + 1 };
    case "decrement": return { count: state.count - 1 };
    case "reset":     return { count: 0 };
    default: return state;
  }
}

// 2. Use in component
function Counter() {
  const [state, dispatch] = useReducer(reducer, { count: 0 });
  return (
    <>
      <p>{state.count}</p>
      <button onClick={() => dispatch({ type: "increment" })}>+</button>
      <button onClick={() => dispatch({ type: "decrement" })}>-</button>
      <button onClick={() => dispatch({ type: "reset" })}>Reset</button>
    </>
  );
}
```

**`useState` vs `useReducer`:**
- `useState` → simple values, independent state
- `useReducer` → complex objects, multiple related state updates, logic-heavy updates

---

## 20. useMemo & useCallback (Performance)

> **useCallback** — returns a **memoized version of a callback** to help a child component not re-render unnecessarily.

> **useMemo** — returns a **memoized value** that helps in performance optimizations.

```jsx
import { useMemo, useCallback, useState } from "react";

function App() {
  const [count, setCount] = useState(0);
  const [text, setText]   = useState("");

  // useMemo — only re-runs when 'count' changes
  const expensiveResult = useMemo(() => {
    return count * 1000;
  }, [count]);

  // useCallback — stable function reference
  const handleClick = useCallback(() => {
    setCount(c => c + 1);
  }, []);

  return <ChildComponent onClick={handleClick} value={expensiveResult} />;
}
```

> Don't overuse these — only add them when you have a **measurable performance problem**.

---

## 21. React.memo (Prevent Re-renders)

Wraps a component so it only re-renders if its props change:

```jsx
import { memo } from "react";

const UserCard = memo(function UserCard({ name }) {
  console.log("UserCard rendered");
  return <div>{name}</div>;
});

// Works best with useCallback for function props:
const handleDelete = useCallback(() => deleteUser(id), [id]);
<UserCard name="Alice" onDelete={handleDelete} />
```

---

## 22. Custom Hooks

Extract reusable stateful logic into a function that starts with `use`:

```jsx
// useFetch.js — reusable data fetching hook
import { useState, useEffect } from "react";

function useFetch(url) {
  const [data, setData]       = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError]     = useState(null);

  useEffect(() => {
    setLoading(true);
    fetch(url)
      .then(res => {
        if (!res.ok) throw new Error("Network error");
        return res.json();
      })
      .then(data => { setData(data); setLoading(false); })
      .catch(err => { setError(err.message); setLoading(false); });
  }, [url]);

  return { data, loading, error };
}

// Usage in any component
function UserList() {
  const { data, loading, error } = useFetch("https://api.example.com/users");
  if (loading) return <p>Loading...</p>;
  if (error)   return <p>Error: {error}</p>;
  return <ul>{data.map(u => <li key={u.id}>{u.name}</li>)}</ul>;
}
```

> **Hooks** — simple JS functions that can be used to reuse part from a functional component. Hooks can be stateful and can manage side-effects.

---

## 23. Data Fetching Pattern

Standard loading/error/data pattern for API calls in React:

```jsx
function ProductList() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading]   = useState(true);
  const [error, setError]       = useState(null);

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const res  = await fetch("/api/products");
        if (!res.ok) throw new Error(`HTTP error! status: ${res.status}`);
        const data = await res.json();
        setProducts(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };
    fetchProducts();
  }, []);

  if (loading) return <div>Loading...</div>;
  if (error)   return <div>Error: {error}</div>;

  return (
    <ul>
      {products.map(p => <li key={p.id}>{p.name}</li>)}
    </ul>
  );
}
```

---

## 24. React.lazy & Suspense (Code Splitting)

> **React.lazy** — used to **dynamically import** a part of code; must get loaded when it is required.

> **Suspense** — allows developers to **display a fallback UI** while waiting for data to load.

Load components only when needed — reduces initial bundle size:

```jsx
import { lazy, Suspense } from "react";

const Dashboard = lazy(() => import("./Dashboard"));
const Settings  = lazy(() => import("./Settings"));

function App() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <Routes>
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/settings"  element={<Settings />} />
      </Routes>
    </Suspense>
  );
}
```

---

## 25. Lifting State Up

When two sibling components need to share state, move it to their **common parent**:

```jsx
function Parent() {
  const [value, setValue] = useState("");
  return (
    <>
      <InputA value={value} onChange={setValue} />
      <InputB value={value} onChange={setValue} />
    </>
  );
}

function InputA({ value, onChange }) {
  return <input value={value} onChange={e => onChange(e.target.value)} />;
}
```

---

## 26. Key Prop — Why It Matters

`key` tells React which item in a list **is which** across renders.

```jsx
// Bad — using index means React can't track items correctly
{items.map((item, index) => <li key={index}>{item.name}</li>)}

// Good — use a stable unique ID
{items.map(item => <li key={item.id}>{item.name}</li>)}

// key is also used to force a component to remount (reset its state)
<UserProfile key={userId} userId={userId} />
```

---

## 27. React Internals — Fragment, Reconciliation, Fiber

### React Fragment
> A feature in React that allows you to **return multiple elements without adding extra nodes to the DOM**.

```jsx
// Both are equivalent
return (
  <React.Fragment>
    <h1>Title</h1>
    <p>Content</p>
  </React.Fragment>
);

// Shorthand
return (
  <>
    <h1>Title</h1>
    <p>Content</p>
  </>
);
```

### Reconciliation
> The process to **update the browser DOM**. React uses a **diff algorithm** so that component updates are fast.

- React creates a Virtual DOM (a lightweight copy of the real DOM).
- On state change, it compares old vs new Virtual DOM (diffing).
- Only the changed parts are updated in the real DOM.

### React Fiber
> A **complete rewrite of React's reconciliation algorithm** to solve some long-standing issues in React. Makes animations, layout, and gestures more capable.

### super(props)
> Used inside the **constructor of a class** to derive the parent's call. Accesses properties inside the class that extended it.

```jsx
class MyComponent extends React.Component {
  constructor(props) {
    super(props); // must be called first
    this.state = { count: 0 };
  }
}
```

---

## 28. Exports — Named vs Default

### Named Export
> One can have **multiple named exports per file**. Then import the specific export.

```jsx
// math.js
export const PI = 3.14;
export function add(a, b) { return a + b; }

// Importing
import { PI, add } from "./math.js";
import { add as sum } from "./math.js"; // alias
```

### Default Export
> One per file — can be imported with any name.

```jsx
// greet.js
export default function greet(name) { return `Hello ${name}`; }

// Importing
import greet from "./greet.js";
import myGreet from "./greet.js"; // any name works
```

---

## 29. HOC — Higher Order Component

> **HOC** is an advanced technique in React for **reusing component logic**. It is a function that takes a component and returns a new component.

```jsx
// HOC — wraps a component with extra functionality
function withLoader(WrappedComponent) {
  return function WithLoaderComponent({ isLoading, ...props }) {
    if (isLoading) return <div>Loading...</div>;
    return <WrappedComponent {...props} />;
  };
}

// Usage
const UserListWithLoader = withLoader(UserList);
<UserListWithLoader isLoading={loading} users={users} />
```

---

## 30. SPA, SSR, CSR

### SPA (Single Page Application)
> A web application that **dynamically updates the webpage with data from the web server without refreshing the entire page**.

### SSR (Server-Side Rendering)
> Means the **server generates the HTML** and sends it to the browser.

### CSR (Client-Side Rendering)
> Means the **browser uses JavaScript to build the page** after it's loaded.

| | SSR | CSR |
|---|---|---|
| Rendering | Server | Browser |
| Initial Load | Faster (HTML ready) | Slower (JS must run first) |
| SEO | Better | Needs extra setup |
| Example | Next.js | Create React App / Vite |

---

## 31. Microservices

> An **organizational approach to software development** where software is composed of **small, independent services** (like a database, UI, of the application). It makes applications easier to scale and faster to develop.

> We are dividing software into **small modules**.

---

## 32. State Management — When to Use What?

| Scenario | Tool |
|----------|------|
| Local UI state (toggle, form) | `useState` |
| Cross-component (theme, auth) | Context API |
| Large app, complex state | Redux (RTK) |
| Server data fetching | React Query / SWR |

---

## Quick Reference Cheatsheet

| Concept | Key Point |
|---------|-----------|
| Library | Collection of packages for specific tasks |
| Framework | Pre-written structure; framework calls your code |
| Tree Shaking | Removes unused code from bundle |
| HMR | Updates modules without full page reload |
| Babel | Compiles modern JS for older browsers |
| Component | Reusable piece of UI; must start with capital letter |
| Props | Data passed from parent to child; read-only |
| State | Data that can change over time; triggers re-render |
| useState | Hook for local component state |
| useEffect | Hook for side effects (API calls, subscriptions) |
| useContext | Hook to read current Context value |
| useReducer | useState alternative for complex state |
| useRef | Mutable ref that doesn't cause re-render |
| useCallback | Memoize a function reference |
| useMemo | Memoize a computed value |
| React.memo | Prevent re-render if props unchanged |
| Fragment | Return multiple elements without extra DOM node |
| Reconciliation | Process of updating the real DOM efficiently |
| React Fiber | Rewrite of reconciliation algorithm |
| Named Export | Multiple per file; imported with `{ }` |
| Default Export | One per file; imported with any name |
| HOC | Function that takes and returns a component |
| Props Drilling | Passing props through many unnecessary levels |
| Context API | Share state without prop drilling |
| Redux | Centralized global state management |
| Dispatch | Send an action to the Redux store |
| Reducer | Pure fn that defines how state changes |
| Selector | Extracts data from Redux store |
| Controlled | Form state managed by React |
| Uncontrolled | Form state managed by DOM |
| SPA | Dynamically updates without full page refresh |
| SSR | Server generates and sends HTML |
| CSR | Browser builds page using JavaScript |
| Lazy | Dynamic import — loads component only when needed |
| Suspense | Shows fallback UI while waiting to load |
| Microservices | App split into small independent services |
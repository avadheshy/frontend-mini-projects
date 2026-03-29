# React Notes ⚛️

---

## What is React?
React is a **JavaScript library** for building UIs. A library = collection of pre-built functionality you plug into your project.

**Key idea:** React is all about **components** — reusable pieces of UI (custom HTML creators).

**Imperative (vanilla JS) vs Declarative (React):**
- Imperative → tell the browser *how* to do it step by step
- Declarative → tell React *what* you want, it figures out the how

---

## Setup

```bash
# Create a new React app
npm create vite@latest my-app -- --template react
cd my-app
npm install
npm run dev
```

`index.js` (or `main.jsx`) is the **entry point** — it mounts the root component into `index.html`.

---

## Components

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

### JSX Rules
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

## Props (Parent → Child)

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

## State — useState

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

## Events

Events in React use camelCase and pass a function reference:

```jsx
// Click
<button onClick={handleClick}>Click me</button>
<button onClick={() => doSomething(id)}>Click</button>

// Input
<input onChange={(e) => setName(e.target.value)} />

// Form
<form onSubmit={(e) => { e.preventDefault(); handleSubmit(); }}>
```

---

## Controlled Components (Forms)

React manages form state instead of the DOM.

```jsx
function LoginForm() {
  const [form, setForm] = useState({ email: "", password: "" });

  // Single handler for all inputs
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

## useEffect Hook

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

## Passing Data Child → Parent (via function props)

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

## Lists & Keys

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

## React Router DOM

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
      <Route path="/"       element={<Home />} />
      <Route path="/about"  element={<About />} />
      <Route path="/user/:id" element={<UserDetail />} />
      {/* Nested routes */}
      <Route path="/dashboard" element={<Dashboard />}>
        <Route index element={<DashHome />} />       {/* default */}
        <Route path="settings" element={<Settings />} />
      </Route>
    </Routes>
  );
}
```

### Navigation
```jsx
import { NavLink, useNavigate, useParams, useLocation } from "react-router-dom";

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

## Context API (Global State)

Avoid **prop drilling** (passing props through many levels).

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

**Prop drilling** = parent→child→grandchild (tedious)
**Context** = any component can access without passing through every level

---

## Redux (RTK — Redux Toolkit)

```bash
npm install @reduxjs/toolkit react-redux
```

**Core concepts:**
- **Store** — single object holding all app state
- **Slice** — a piece of state + its reducers
- **Action** — object describing what happened `{ type: "counter/increment" }`
- **Reducer** — pure function: `(state, action) => newState`
- **Dispatch** — send an action to the store

```jsx
// counterSlice.js
import { createSlice } from "@reduxjs/toolkit";

const counterSlice = createSlice({
  name: "counter",
  initialState: { value: 0 },
  reducers: {
    increment: (state) => { state.value += 1; },  // RTK uses Immer (mutate OK)
    decrement: (state) => { state.value -= 1; },
    addBy: (state, action) => { state.value += action.payload; }
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
  const count = useSelector(state => state.counter.value);
  const dispatch = useDispatch();
  return (
    <button onClick={() => dispatch(increment())}>
      Count: {count}
    </button>
  );
}
```

---

## Quick Reference: Common Patterns

```jsx
// Conditional rendering
{isLoggedIn && <Dashboard />}
{isLoggedIn ? <Dashboard /> : <Login />}

// Render nothing
if (!data) return null;

// Spread props
const props = { name: "Alice", age: 25 };
<Component {...props} />

// Children prop
function Card({ children }) {
  return <div className="card">{children}</div>;
}
<Card><p>Any content here</p></Card>
```

---

## State Management — When to Use What?

| Scenario | Tool |
|----------|------|
| Local UI state (toggle, form) | `useState` |
| Cross-component (theme, auth) | Context API |
| Large app, complex state | Redux (RTK) |
| Server data fetching | React Query / SWR |

---

## useRef Hook

`useRef` gives you a **mutable box** that doesn't trigger re-renders when changed. Two main uses:

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

## useReducer Hook

Better than `useState` for **complex state logic** (multiple sub-values, or next state depends on previous).

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

## useMemo & useCallback (Performance)

Prevent unnecessary re-computations and re-renders:

```jsx
import { useMemo, useCallback, useState } from "react";

function App() {
  const [count, setCount] = useState(0);
  const [text, setText] = useState("");

  // useMemo — memoize expensive calculation
  // Only re-runs when 'count' changes, NOT when 'text' changes
  const expensiveResult = useMemo(() => {
    console.log("Computing...");
    return count * 1000; // imagine this is slow
  }, [count]);

  // useCallback — memoize a function reference
  // Without this, a new function is created on every render
  const handleClick = useCallback(() => {
    setCount(c => c + 1);
  }, []); // stable reference — no dependencies

  return <ChildComponent onClick={handleClick} value={expensiveResult} />;
}
```

> Don't overuse these — only add them when you have a **measurable performance problem**.

---

## React.memo (Prevent Re-renders)

Wraps a component so it only re-renders if its props change:

```jsx
import { memo } from "react";

// Without memo: re-renders every time Parent re-renders
// With memo: only re-renders when 'name' prop changes
const UserCard = memo(function UserCard({ name }) {
  console.log("UserCard rendered");
  return <div>{name}</div>;
});

// Works best with useCallback for function props:
const handleDelete = useCallback(() => deleteUser(id), [id]);
<UserCard name="Alice" onDelete={handleDelete} />
```

---

## Custom Hooks

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

---

## Data Fetching Pattern

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

## React.lazy & Suspense (Code Splitting)

Load components only when needed — reduces initial bundle size:

```jsx
import { lazy, Suspense } from "react";

// Lazy load heavy component
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

## Lifting State Up

When two sibling components need to share state, move it to their **common parent**:

```jsx
// Both inputs need to stay in sync → lift state to parent
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

## Key Prop — Why It Matters

`key` tells React which item in a list **is which** across renders. Using index as key causes bugs when list order changes:

```jsx
// ❌ Bad — using index means React can't track items correctly
{items.map((item, index) => <li key={index}>{item.name}</li>)}

// ✅ Good — use a stable unique ID
{items.map(item => <li key={item.id}>{item.name}</li>)}

// key is also used to force a component to remount (reset its state)
<UserProfile key={userId} userId={userId} />
// Changing userId → new key → component fully resets
```
import './App.css';
import { useState } from 'react';

function App() {

  const [formdata, setFormData] = useState({
    firstName: '',
    lastName: '',
    email: '',
    country: '',
    street: '',
    state: '',
    pincode: '',
    city: '',
    comments: false,
    candidates: false,
    offers: false,
    notification: ''
  });

  function submitHandler(event) {
    event.preventDefault();
    console.log('Submit clicked');
    console.log(formdata);
  }

  function changeHandler(event) {
    const { name, value, checked, type } = event.target;

    setFormData(prev => ({
      ...prev,
      [name]: type === "checkbox" ? checked : value
    }));
  }

  return (
    <div className="h-screen w-screen flex justify-center items-center">
      <form onSubmit={submitHandler} className="flex flex-col gap-3">

        {/* First Name */}
        <label>First Name</label>
        <input
          type="text"
          name="firstName"
          placeholder="Avadhesh"
          value={formdata.firstName}
          onChange={changeHandler}
        />

        {/* Last Name */}
        <label>Last Name</label>
        <input
          type="text"
          name="lastName"
          placeholder="Yadav"
          value={formdata.lastName}
          onChange={changeHandler}
        />

        {/* Email */}
        <label>Email</label>
        <input
          type="email"
          name="email"
          placeholder="email"
          value={formdata.email}
          onChange={changeHandler}
        />

        {/* Country */}
        <label>Country</label>
        <select
          name="country"
          value={formdata.country}
          onChange={changeHandler}
        >
          <option value="">Select Country</option>
          <option value="india">India</option>
          <option value="usa">USA</option>
          <option value="england">England</option>
          <option value="canada">Canada</option>
        </select>

        {/* Address */}
        <label>Street</label>
        <input
          type="text"
          name="street"
          value={formdata.street}
          onChange={changeHandler}
        />

        <label>State</label>
        <input
          type="text"
          name="state"
          value={formdata.state}
          onChange={changeHandler}
        />

        <label>City</label>
        <input
          type="text"
          name="city"
          value={formdata.city}
          onChange={changeHandler}
        />

        <label>Pincode</label>
        <input
          type="text"
          name="pincode"
          value={formdata.pincode}
          onChange={changeHandler}
        />

        {/* Checkboxes */}
        <fieldset>
          <legend>By Email</legend>

          <input
            type="checkbox"
            name="comments"
            checked={formdata.comments}
            onChange={changeHandler}
          />
          <label>Comments</label>

          <br />

          <input
            type="checkbox"
            name="candidates"
            checked={formdata.candidates}
            onChange={changeHandler}
          />
          <label>Candidates</label>

          <br />

          <input
            type="checkbox"
            name="offers"
            checked={formdata.offers}
            onChange={changeHandler}
          />
          <label>Offers</label>
        </fieldset>

        {/* Radio Buttons */}
        <fieldset>
          <legend>Push Notifications</legend>

          <input
            type="radio"
            name="notification"
            value="everything"
            checked={formdata.notification === "everything"}
            onChange={changeHandler}
          />
          <label>Everything</label>

          <br />

          <input
            type="radio"
            name="notification"
            value="email"
            checked={formdata.notification === "email"}
            onChange={changeHandler}
          />
          <label>Email</label>

          <br />

          <input
            type="radio"
            name="notification"
            value="push"
            checked={formdata.notification === "push"}
            onChange={changeHandler}
          />
          <label>Push Notifications</label>
        </fieldset>

        {/* Submit Button */}
        <button type="submit" className="bg-blue-500 text-white p-2 rounded">
          Submit
        </button>

      </form>
    </div>
  );
}

export default App;
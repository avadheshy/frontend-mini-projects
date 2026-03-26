function Nav(props) {
    const { filterData, category, setCategory } = props;
  
    return (
      <div className="flex justify-center items-center gap-10 bg-slate-300 h-[50px]">
        {filterData.map((data) => (
          <button 
            key={data.id} 
            // 1. Put the click handler on the button
            // 2. Pass 'data.title' (the category name) to the setter
            onClick={() => setCategory(data.title)}
            // 3. Optional: Style the active button
            className={`${category === data.title ? "border-2 border-white" : ""}`}
          >
            {data.title}
          </button>
        ))}
      </div>
    );
  }
  
  export default Nav;
  
import { useContext } from "react"
import { AppContext } from "../context/AppContext"


function Pagination() {
    const { page, totalPages, handlePageChange } = useContext(AppContext);
  
    return (
      <div className="w-full flex justify-around h-10  fixed bottom-0 border border-x-black">
        <div className=" flex justify-between items-center gap-10 px-4">
          {page > 1 && (
            <button onClick={() => handlePageChange(page - 1)}>Previous</button>
          )}
  
          {page < totalPages && (
            <button onClick={() => handlePageChange(page + 1)}>Next</button>
          )}
        </div>
  
        <div className=" px-4 flex items-center">
          Page {page} of {totalPages}
        </div>
      </div>
    );
  }

export default Pagination
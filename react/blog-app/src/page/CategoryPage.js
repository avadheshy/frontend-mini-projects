import Blog from "../component/Blog"
import Header from "../component/Header"
import Pagination from "../component/Pagination"

function CategoryPage(){
    return(
        <div>
            <Header/>
            <Blog/>
            <Pagination/>
        </div>
    )
}

export default CategoryPage
import Header from "../component/Header"
import Pagination from "../component/Pagination"
import Blog from "../component/Blog"
import { useContext,useState,useEffect } from "react"
import { useLocation } from "react-router-dom"
import { useNavigate } from "react-router-dom"
import { AppContext } from "../context/AppContext"

function BlogPage(){
    const [blog,setBlog]=useState(null)
    const {loading,setLoading,posts,setPosts}=useContext(AppContext)
    const url='https://codehelp-apis.vercel.app/api/get-blog?blogId='
    const location = useLocation()
    const navigate = useNavigate()
    useEffect(() => {
        async function fetchData() {
            let blogId = location.pathname.split('/').at(-1);
    
            try {
                setLoading(true);
    
                let res = await fetch(`${url}${blogId}`);
                let data = await res.json();   
    
                setBlog(data.blog);
                setPosts(data.relatedBlogs);
    
            } catch (error) {
                setPosts([]);
                setBlog(null);
            } finally {
                setLoading(false);
            }
        }
    
        fetchData();
    }, [location.pathname]);

    if (!blog){

        return
    }
    
    return(
        <div>
            <Header/>
            <div className="flex flex-col items-start mb-10">
                <p className="text-orange-800 font-bold">{blog.title}</p>
                <p className="font-bold">{blog.author}</p>
                <p>{blog.date}</p>
                <p className="font-bold">{blog.category}</p>
                <div>
                {
                blog.tags.map((tag, indx) => (
                    <span className="font-bold" key={indx} onClick={()=>(navigate(`/tags/${tag.replace("-","")}`))}>#{tag} </span>
                ))
                }
                </div>
            <h3 className="font-bold">Related Blog</h3>
            </div>
            <Blog/>
        
        </div>
    )
}

export default BlogPage
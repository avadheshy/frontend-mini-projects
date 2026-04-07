import { useContext } from "react"
import { AppContext } from "../context/AppContext"
import { useNavigate } from "react-router-dom"

function Blog(){
    const {posts}=useContext(AppContext)
    const navigate=useNavigate()
    return(
        <div className="w-full flex flex-col justify-start items-start gap-10">
          {posts.map((post, index) => (
            <div className="w-full flex flex-col  items-start" key={index}>
            <p className="text-red-800 font-bold" onClick={() => navigate(`/blog/${post.id}`)}>{post.title}</p>                
                <div className="flex gap-2">

                    <p className="font-bold">By {post.author} </p>
                    <p className="font-bold" onClick={()=>(navigate(`/categories/${post.category.replace("-","")}`))}>on {post.category}</p>
                </div>
                <p>Posted on <span className="font-bold">{post.date}</span></p>
                <p className="w-full text-start">{post.content}</p>
                <div>
                {
                post.tags.map((tag, indx) => (
                    <span className="font-bold" key={indx} onClick={()=>(navigate(`/tags/${tag.replace("-","")}`))}>#{tag} </span>
                ))
                }
                </div>
            </div>
            ))}
        </div>
    )
}

export default Blog
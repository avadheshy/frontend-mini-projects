import './App.css';
import './index.css'
import { Route,Routes } from 'react-router-dom';

import HomePage from './page/Home'
import TagPage from './page/TagPage'
import CategoryPage from './page/CategoryPage'
import BlogPage from './page/BlogPage'
import { useLocation,useSearchParams } from 'react-router-dom';
import { useContext } from 'react';
import { AppContext } from './context/AppContext';
import { useEffect } from 'react';



function App() {

  const location = useLocation()
  const [search,setSearch]=useSearchParams()
  const {fetchBlogPosts} = useContext(AppContext)
  useEffect(()=>{
        let page = search.get('page') ?? 1;
        if (location.pathname.includes('tags')){
          let tag=location.pathname.split('/').at(-1).replace("-","")
          fetchBlogPosts(Number(page),tag)
        }
        else if (location.pathname.includes('categories')){
          let category = location.pathname.split('/').at(-1).replace('-','')
          fetchBlogPosts(Number(page),null,category)
        }
        else{
          fetchBlogPosts(Number(page))
        }
        
      },
      [location.pathname,location.search]
  )

  return (
    <div className="App">
      <Routes>
        <Route path='/' element={<HomePage/>} />
        <Route path='/tags/:tag' element={<TagPage/>} />
        <Route path='/categories/:category' element={<CategoryPage/>} />
        <Route path='/blog/:blogId' element={<BlogPage/>} />

      </Routes>
    </div>
  );
}

export default App;

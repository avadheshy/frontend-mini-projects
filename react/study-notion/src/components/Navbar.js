import Logo from '../assets/Logo.svg';
import { useNavigate } from 'react-router-dom';

import { useState } from 'react';

function NavBar(){

    const [isLoggin,setLoggin]=useState(false)
    const navigate = useNavigate();


    return (
        <div className='flex justify-around items-center text-white'>
            <div>
                <img src={Logo}/>
            </div>
            <div>
                <ul className='flex justify-between items-center gap-10'>
                    <li onClick={()=>navigate('/')}>Home</li>
                    <li onClick={()=>navigate('/about')}>About</li>
                    <li onClick={()=>navigate('/contact')}>Contact</li>
                </ul>
            </div>
            <div>
            <ul className='flex justify-center items-center gap-10'>
                    { !isLoggin && <li onClick={()=>navigate('/login')}>Login</li>}
                    { !isLoggin && <li onClick={()=>navigate('/signup')}>Sign Up</li>}
                    { isLoggin && <li onClick={()=>navigate('/')}>Logout</li>}
                    {isLoggin &&<li>Dashboard</li>}
                </ul>
            </div>

        </div>
    )

}

export default NavBar
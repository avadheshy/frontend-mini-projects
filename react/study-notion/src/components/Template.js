import frame from '../assets/frame.png'
import LoginForm  from './LoginForm'
import SignupForm from './SignupForm'



function Template({title,desc1,desc2,image,formtype,setIsLoggedIn}){
    console.log(formtype)
    
    return (
        <div className='w-full h-full flex justify-center items-center'>
            <div className='flex justify-between items-start w-[1300px] h-full pt-20'>
            <div className='w-[600px]  h-[600px] flex flex-col justify-around items-center '>
                <div>
                    <div className='font-bold text-3xl text-white'>{title}</div>
                </div>
                <div>
                    <div className='text-xl text-dark-white'>{desc1}</div>
                </div>
                <div>
                    <div className='text-xl text-blue-700'>{desc2}</div>
                </div>
                <div>
                    {formtype=='login'?<LoginForm/>:<SignupForm/>}
                </div>

                <div className="flex items-center gap-2 w-full">
                <div className="flex-1 h-[1px] bg-white"></div>
                <span className="text-white">OR</span>
                <div className="flex-1 h-[1px] bg-white"></div>
                </div>
                <div>
                    <p className='text-white'>Sign up With Google</p>
                </div>

            </div>
            <div className='relative w-[600px] h-[600px]'>
                <img className='absolute top-10 right-5 z-10' src={frame}/>
                <img  className="absolute top-13 right-8 z-20" src={image}/>
            </div>
        </div>
        </div>

    )
}

export default Template

import Template from '../components/Template'
import { useState } from 'react';
import { FaEye, FaEyeSlash } from "react-icons/fa";


function LoginForm(){
    const [showPassword, setShowPassword] = useState(true);

    return (
        <div>
            <form>
               <div className='flex flex-col  w-full h-full gap-10'>
                    <div>
                        <label>
                            <p className='text-white'>Email address <span className="text-red-500">*</span></p> 
                            <input type="email" name="email" placeholder="Enter email here"/>
                        </label>
                    </div>
                    <div>
                        <label>
                        <p className='text-white'>Password <span className="text-red-500">*</span></p> 
                        <div className='absolute'>
                            <input
                            type={showPassword?'text':'password'}
                            name="password"
                            placeholder="Enter password"/>
                            <span className="absolute right-2.5 top-1/3 -translate-y-1/2 cursor-pointer">   {showPassword ? <FaEyeSlash /> : <FaEye />}</span>
                            <p className='absolute right-1 top-7 text-white'>Forgot Password</p>
                        </div>
                        </label>
                    </div>
                    <div>
                        <button className='text-white' >Sing In</button>
                    </div>
               </div>

            </form>
            
        </div>
    )

}

export default LoginForm


// import { useState } from "react";
// import { FaEye, FaEyeSlash } from "react-icons/fa";

// function LoginForm() {
//   const [showPassword, setShowPassword] = useState(false);

//   return (
//     <div className="flex justify-center items-center h-screen">
//       <form className="flex flex-col gap-4 w-80">

//         {/* Email */}
//         <label className="flex flex-col">
//           <p className="mb-1">
//             Email address <span className="text-red-500">*</span>
//           </p>
//           <input
//             type="email"
//             name="email"
//             placeholder="Enter email"
//             className="border p-2 rounded"
//           />
//         </label>

//         {/* Password */}
//         <label className="flex flex-col">
//           <p className="mb-1">
//             Password <span className="text-red-500">*</span>
//           </p>

//           <div className="relative">
//             <input
//               type={showPassword ? "text" : "password"}
//               name="password"
//               placeholder="Enter password"
//               className="border p-2 rounded w-full pr-10"
//             />

//             {/* Eye Icon */}
//             <span
//               onClick={() => setShowPassword(!showPassword)}
//               className="absolute right-2.5 top-1/2 -translate-y-1/2 cursor-pointer"
//             >
//               {showPassword ? <FaEyeSlash /> : <FaEye />}
//             </span>
//           </div>

//           {/* Forgot Password */}
//           <p className="text-sm text-blue-500 mt-1 text-right cursor-pointer">
//             Forgot Password?
//           </p>
//         </label>

//         {/* Button */}
//         <button className="bg-blue-500 text-white p-2 rounded">
//           Sign In
//         </button>

//       </form>
//     </div>
//   );
// }

// export default LoginForm;
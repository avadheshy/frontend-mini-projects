
import { useState } from "react";
import { FaEye, FaEyeSlash } from "react-icons/fa";


function SignupForm(){
    const [showPassword, setShowPassword] = useState(false);
    const [showConfirmPassword, setShowCinfirmPassword] = useState(false);

    return (
        <div className="flex flex-col gap-10 w-full">
             <div className="flex justify-around">
                    <div>Student</div>
                    <div>Instructor</div>
             </div>
            <form className="flex flex-col justify-around items-start">
               
                <div className="flex gap-5">
                    <label>
                        <p className="text-white">First Name</p>
                        <input type="text" name="firstName" placeholder="First Name"/>
                    </label>
                    <label>
                        <p className="text-white">Last Name</p>
                        <input type="text" name="lastName" placeholder="Last Name"/>
                    </label>
                </div>
                <div>
                <label>
                        <p className="text-white">Email</p>
                        <input  type="email" name="email" placeholder="Email"/>
                    </label>
                </div>
                <div className="flex gap-5">
                    <label className="relative">
                           <p>Password <span className="text-red-500">*</span></p>
                            <input type={showPassword ? "text" : "password"} name="password" placeholder="Password"/>
                            <span
                                onClick={() => setShowPassword(!showPassword)}
                                className="absolute right-2.5 top-7  cursor-pointer"
                                >
                                {showPassword ? <FaEyeSlash /> : <FaEye />}
                            </span>
                     </label>
                    <label className="relative">
                            <p>Confirm Password <span className="text-red-500">*</span></p>
                            <input  type={showConfirmPassword ? "text" : "password"} name="confirmPassword" placeholder="Confirm Password"/>
                            <span
                                onClick={() => setShowCinfirmPassword(!showConfirmPassword)}
                                className="absolute right-2.5 top-7  cursor-pointer"
                                >
                                {showPassword ? <FaEyeSlash /> : <FaEye />}
                            </span>
                    </label>
                </div>
                <div>
                    <submit className='text-white' >Create account</submit>
                </div>
            </form>
        </div>
    )

}

export default SignupForm



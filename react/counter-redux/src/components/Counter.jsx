import React from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { increment, decrement } from '../redux/slices/CounterSlice';

const Counter = () => {

    const count = useSelector((state) => state.counter.value );
    const dispatch = useDispatch();

  return (
    // <div>
    //   <button
    //   onClick={() => dispatch(increment())}
    //   >
    //     Increment
    //   </button>
    //   <br/>
    //   <br/>

    //   <div>{count}</div>

    //   <br/>
    //   <br/>

    //   <button
    //   onClick={() => dispatch(decrement())}
    //   >
    //     Decrement
    //   </button>
    // </div>
    <div className="flex w-[1200px] h-[1200px]">
    <div class="flex">
        <div>
            <div>
                a
            </div>
            <div>
                <div>
                    c
                </div>
                <div>
                    d
                </div>
            </div>

        </div>
        <div>
            <div>
                b
            </div>
            <div>
                e
            </div>
        </div>

    </div>
    <div class="box6">
        f
    </div>
</div>
  )
}

export default Counter

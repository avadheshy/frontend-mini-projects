function Date(props){
    const day = props.date
    const month = props.month
    const year = props.year
    console.log(props)
    return (
        <div className="bg-green-900 m-[25px] p-[10px]">
        <span>{day}</span>
        <span>{month}</span>
        <span>{year}</span>

    </div>
    )
  
}
export default Date
function ItemDate({date,month,year}){

    return (
        <div className="bg-green-900 text-white m-4 p-4 rounded-lg shadow-md">
        <span>{date}</span>
        <span>{month}</span>
        <span>{year}</span>

    </div>
    )
  
}
export default ItemDate
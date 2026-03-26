import ItemName from "./ItemName"

function ItemDate({date}){

    const d = new Date(date);

    const day = d.getDate();
    const year = d.getFullYear();
  
    const month = d.toLocaleString('en-US', {
      month: 'long'
    });
    return (
        <div>
            <div>{month}</div>
            <div>{year}</div>
            <div>{day}</div>
        </div>
    )
}

export default ItemDate
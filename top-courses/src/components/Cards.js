import Card from "./Card"

function Cards(props) {
    let data = props.data;
    if (!data) return null; 

    return (
        <div className="flex  flex-row flex-wrap justify-center items-center  gap-4 w-[1200px]">
            {data.map((card) => {
                return <Card key={card.id} card={card} />; 
            })}
        </div>
    )
}

export default Cards;

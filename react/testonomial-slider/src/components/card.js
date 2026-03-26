function Card(props){

    const name = props.name
    const job = props.job
    const image = props.image
    const text = props.text
    return(
        <div className="flex flex-col justify-evenly  gap-5">
            <img src={image}></img>
            <h1 className="font-bold">{name}</h1>
            <h2 className="text-blue-500">{job}</h2>
            <p>{text}</p>

        </div>
    )

}

export default Card
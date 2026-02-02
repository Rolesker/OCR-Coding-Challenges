function create_semaphore(){
    const container=document.getElementById("images");
    container.innerHTML="";
    const endpoint=document.createElement("div");
    container.appendChild(endpoint)
    const sentence=document.getElementById("sentence-content").value;
    const words=sentence.split(" ");
    for(let i=0;i<words.length;i++){
        const newDiv=document.createElement("div");
        newDiv.style.display="inline-block";
        for(let j=0;j<words[i].length;j++){
            const newImg=document.createElement("img")
            newImg.src=get_image(words[i][j]);
            newDiv.appendChild(newImg);
        }
        container.insertBefore(newDiv,endpoint);
        container.insertBefore(document.createElement("br"),endpoint);
    }
}

function get_image(char){
    return "68 - semaphore images/"+char.toLowerCase()+".png";
}
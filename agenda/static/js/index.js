const campoBusca = document.querySelector("#campoBusca");
const cards = document.querySelectorAll(".card")
const mensagem = document.querySelector("#no-event")

campoBusca.addEventListener("input", () => {
    const texto = campoBusca.value.toLowerCase()
    let encontrados = 0

    cards.forEach((card) => {
        const titulo = card.querySelector(".card-title")
        const textoTitulo = titulo.textContent.toLowerCase()

        const encontrou = textoTitulo.includes(texto)
    
        if (encontrou){
            card.style.display = ""
            encontrados++
        } else{
            card.style.display = "none"
        }
        
    })
    if (encontrados == 0){
        mensagem.style.display = ""
    } else {
        mensagem.style.display = "none"
    }   
    
})




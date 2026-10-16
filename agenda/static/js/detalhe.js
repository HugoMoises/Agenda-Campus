const buttonAtividades = document.querySelector("#button-atividades")
const atividades = document.querySelectorAll(".atividades")

buttonAtividades.addEventListener("click", () => {
    let textoButton = buttonAtividades.textContent.toLowerCase() 

        if (textoButton === "mostrar atividades"){
            buttonAtividades.textContent = "Ocultar Atividades"
            atividades.forEach((atividade) => {
                atividade.style.display = ""
            })
    
        } else{
            buttonAtividades.textContent = "Mostrar Atividades"
            atividades.forEach((atividade) => {
                atividade.style.display = "none"
            })
        }
})
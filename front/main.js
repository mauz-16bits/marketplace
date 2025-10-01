const cadastro = document.getElementById('cadastro')
const login = document.getElementById('login')
const cart = document.getElementById('cart')

let total = 0
let qtd = 0

function addCart(cost) {
    total += cost
    qtd++
    cart.innerHTML = `🛒 ${qtd} itens | R$ ${total.toFixed(2)}`
}

function formCadastro() {
    cadastro.showModal()
}

cadastro.querySelector("form").addEventListener("submit", async (event) => {
    event.preventDefault()

    const nome = document.getElementById("nomeNewUser").value
    const email = document.getElementById("emailNewUser").value
    const senha = document.getElementById("senhaNewUser").value

    const response = await fetch("http://127.0.0.1:5000/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name: nome, username: email, password: senha })
    })

    const data = await response.json()
    alert(data.message || data.error)
    cadastro.close()
})

function formLogin() {
    login.showModal()
}

login.querySelector("form").addEventListener("submit", async (event) => {
    event.preventDefault()

    const email = document.getElementById("emailUser").value
    const senha = document.getElementById("senhaUser").value

    const response = await fetch("http://127.0.0.1:5000/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username: email, password: senha })
    })

    const data = await response.json()
    alert(data.message || data.error)
    login.close()
})

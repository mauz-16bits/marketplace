const cadastro = document.getElementById('cadastro')
const login = document.getElementById('login')
const cart = document.getElementById('cart')

function formCadastro() {
    
    cadastro.showModal()

}

function formLogin() {
    
    login.showModal()

}

function addCart(cost) {

    cart.innerHTML = cost

}
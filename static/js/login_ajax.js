document.getElementById('loginForm').addEventListener('submit', function(event) {
    // 1. Previne o envio padrão do formulário (que causaria recarregamento)
    event.preventDefault();

    const form = event.target;
    const formData = new FormData(form);
    
    const email = formData.get('email');
    const password = formData.get('password');
    
    const statusDiv = document.getElementById('statusMessage');
    const submitButton = document.getElementById('submitButton');

    // Desabilita o botão para evitar cliques duplos
    submitButton.disabled = true;
    statusDiv.innerHTML = 'Aguarde...';

    // 2. Constrói o objeto JSON para enviar ao Flask
    const dataToSend = {
        email: email,
        password: password
    };

    // 3. Envia a requisição POST usando Fetch API
    fetch(form.action || '/login', { // Usa a action do form ou '/login'
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(dataToSend)
    })
    .then(response => response.json().then(data => ({ status: response.status, body: data })))
    .then(obj => {
        // 4. Manipula a resposta JSON
        const data = obj.body;
        
        submitButton.disabled = false; // Reabilita o botão

        if (data.success) {
            statusDiv.style.color = 'green';
            statusDiv.innerHTML = data.message;
            
            // Redireciona após um pequeno delay para o usuário ver a mensagem
            setTimeout(() => {
                window.location.href = data.redirect_url;
            }, 1000); 

        } else {
            statusDiv.style.color = 'red';
            statusDiv.innerHTML = data.message || 'Ocorreu um erro no servidor.';
        }
    })
    .catch(error => {
        // Lidar com falha de rede ou servidor
        submitButton.disabled = false;
        statusDiv.style.color = 'red';
        statusDiv.innerHTML = 'Erro de conexão: Verifique sua rede.';
        console.error('Fetch error:', error);
    });
});
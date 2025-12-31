const chatWindow = document.getElementById('chat-window');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');

function appendMessage(text, sender)
{
    const msg = document.createElement('div');
    msg.classList.add('message', sender);
    msg.textContent = text;
    chatWindow.appendChild(msg);

    chatWindow.scrollTop = chatWindow.scrollHeight;
}

sendBtn.addEventListener('click', sendMessage);

userInput.addEventListener('keydown', function (event)
{
    if (event.key === 'Enter')
    {
        sendMessage();
    }
});

function sendMessage()
{
    const text = userInput.value.trim();

    if (text === '')
    {
        return;
    }

    // 1. Nachricht sofort im Chat anzeigen
    appendMessage(text, 'user');
    userInput.value = '';

    // 2. Nachricht an Django senden (fetch)
    fetch('/chat-api/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: text }) // Wir senden den Text als JSON
    })
    .then(response => response.json()) // Wir wandeln die Antwort von Django in JSON um
    .then(data => {
        // 3. Die Antwort von Django im Chat anzeigen
        appendMessage(data.reply, 'bot');
    })
    .catch(error => {
        console.error('Fehler:', error);
        appendMessage('Fehler: Konnte Server nicht erreichen.', 'bot');
    });
}

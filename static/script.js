function sendMessage() {
    let userInput = document.getElementById("user-input").value;
    document.getElementById("user-input").value = "";

    let chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += `<p><strong>You:</strong> ${userInput}</p>`;

    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userInput }),
    })
        .then(response => response.json())
        .then(data => {
            chatBox.innerHTML += `<p><strong>Bot:</strong> ${data.response} (Sentiment: ${data.sentiment})</p>`;
            chatBox.scrollTop = chatBox.scrollHeight;
        });
}

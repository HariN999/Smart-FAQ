document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("chatbot").addEventListener("click", function () {
        let userQuery = prompt("Ask me anything:");
        if (userQuery) {
            fetch("/chatbot", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ query: userQuery }),
            })
            .then(response => response.json())
            .then(data => alert("Chatbot: " + data.answer));
        }
    });
});

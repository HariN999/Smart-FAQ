document.addEventListener("DOMContentLoaded", function() {
    // Handle domain click to fetch FAQs
    document.querySelectorAll(".nav-link").forEach(link => {
        link.addEventListener("click", function() {
            let domain = this.getAttribute("data-domain");

            fetch(`/faq/${domain}`)
            .then(response => response.json())
            .then(data => {
                let faqContainer = document.getElementById("faq-container");
                faqContainer.innerHTML = `<h3>FAQs for ${domain}</h3>`;
                data.faqs.forEach(faq => {
                    faqContainer.innerHTML += `<p><strong>Q:</strong> ${faq.question} <br><strong>A:</strong> ${faq.answer}</p>`;
                });
            });
        });
    });

    // Chatbot functionality
    document.getElementById("chatbot").addEventListener("click", function() {
        let userQuery = prompt("Ask me a question:");
        if (userQuery) {
            fetch("/chatbot", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ query: userQuery })
            })
            .then(response => response.json())
            .then(data => {
                alert(`Q: ${data.question}\nA: ${data.answer}`);
            });
        }
    });
});

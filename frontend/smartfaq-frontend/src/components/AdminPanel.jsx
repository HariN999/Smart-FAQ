import { useEffect, useState } from "react";
import { getProtected, fetchFaqs, addFaq, deleteFaq } from "../api/adminApi";

export default function AdminPanel({ token }) {
  const [message, setMessage] = useState("");
  const [faqs, setFaqs] = useState([]);
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  async function loadFaqs() {
    const data = await fetchFaqs(token);
    setFaqs(data);
  }

  useEffect(() => {
    async function load() {
      const data = await getProtected(token);
      setMessage(data.message);
      loadFaqs();
    }
    load();
  }, [token]);

  async function handleAdd() {
    if (!question || !answer) return;
    await addFaq(token, { question, answer });
    setQuestion("");
    setAnswer("");
    loadFaqs();
  }

  async function handleDelete(id) {
    await deleteFaq(token, id);
    loadFaqs();
  }

  return (
    <div
      style={{
        marginTop: "20px",
        padding: "20px",
        borderRadius: "12px",
        background: "#1e1e1e",
        border: "1px solid #333",
      }}
    >
      <h2>Admin Dashboard</h2>
      <p>{message}</p>

      <hr style={{ margin: "20px 0", opacity: 0.2 }} />

      <h3>Add FAQ</h3>

      <input
        placeholder="Question"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        style={{ marginRight: "10px" }}
      />

      <input
        placeholder="Answer"
        value={answer}
        onChange={(e) => setAnswer(e.target.value)}
      />

      <button onClick={handleAdd} style={{ marginLeft: "10px" }}>
        Add
      </button>

      <h3 style={{ marginTop: "20px" }}>Existing FAQs</h3>

      <ul>
        {faqs.map((faq) => (
          <li key={faq._id}>
            {faq.question}
            <button
              onClick={() => handleDelete(faq._id)}
              style={{ marginLeft: "10px" }}
            >
              Delete
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

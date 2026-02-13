import { useEffect, useState } from "react";
import { getProtected, fetchFaqs, addFaq, deleteFaq } from "../api/adminApi";

export default function AdminPanel({ token, onLogout }) {
  const [message, setMessage] = useState("");
  const [faqs, setFaqs] = useState([]);
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  async function loadFaqs() {
    try {
      const data = await fetchFaqs(token);
      setFaqs(data);
    } catch (error) {
      console.error("Error loading FAQs:", error);
    }
  }

  useEffect(() => {
    async function load() {
      try {
        const data = await getProtected(token);
        setMessage(data.message);
        loadFaqs();
      } catch (error) {
        console.error("Error loading protected data:", error);
      }
    }
    load();
  }, [token]);

  async function handleAdd() {
    if (!question.trim() || !answer.trim()) {
      alert("Please fill in both question and answer");
      return;
    }

    setLoading(true);
    try {
      await addFaq(token, { question: question.trim(), answer: answer.trim() });
      setQuestion("");
      setAnswer("");
      loadFaqs();
    } catch (error) {
      console.error("Error adding FAQ:", error);
      alert("Failed to add FAQ. Please try again.");
    } finally {
      setLoading(false);
    }
  }

  async function handleDelete(id) {
    if (!confirm("Are you sure you want to delete this FAQ?")) return;
    
    try {
      await deleteFaq(token, id);
      loadFaqs();
    } catch (error) {
      console.error("Error deleting FAQ:", error);
      alert("Failed to delete FAQ. Please try again.");
    }
  }

  return (
    <div className="card">
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "24px" }}>
        <div>
          <h2>Admin Dashboard</h2>
          {message && <p style={{ color: "var(--text-secondary)", marginTop: "4px" }}>{message}</p>}
        </div>
        <button 
          className="button" 
          onClick={onLogout}
          style={{ background: "var(--bg-tertiary)", color: "var(--text-primary)" }}
        >
          🚪 Logout
        </button>
      </div>

      <hr className="divider" />

      <h3>➕ Add New FAQ</h3>

      <div style={{ display: "flex", flexDirection: "column", gap: "12px", marginBottom: "24px" }}>
        <input
          className="input"
          style={{ 
            background: "var(--bg-secondary)", 
            padding: "14px 16px",
            borderRadius: "var(--radius-md)",
            border: "1px solid var(--border)"
          }}
          placeholder="Question"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
        />

        <textarea
          className="input"
          style={{ 
            background: "var(--bg-secondary)", 
            padding: "14px 16px",
            borderRadius: "var(--radius-md)",
            border: "1px solid var(--border)",
            minHeight: "100px",
            fontFamily: "inherit",
            resize: "vertical"
          }}
          placeholder="Answer"
          value={answer}
          onChange={(e) => setAnswer(e.target.value)}
        />

        <button 
          className="button" 
          onClick={handleAdd}
          disabled={loading || !question.trim() || !answer.trim()}
          style={{ alignSelf: "flex-start" }}
        >
          {loading ? "Adding..." : "✅ Add FAQ"}
        </button>
      </div>

      <h3 style={{ marginTop: "40px", marginBottom: "16px" }}>
        📚 Existing FAQs ({faqs.length})
      </h3>

      {faqs.length === 0 ? (
        <div className="empty-state">
          <div className="empty-state-icon">📭</div>
          <p>No FAQs yet. Add your first one above!</p>
        </div>
      ) : (
        <ul className="faq-list">
          {faqs.map((faq) => (
            <li key={faq._id} className="faq-item">
              <div>
                <div className="faq-question">{faq.question}</div>
                <div style={{ 
                  fontSize: "14px", 
                  color: "var(--text-tertiary)", 
                  marginTop: "4px" 
                }}>
                  {faq.answer}
                </div>
              </div>

              <button
                className="button button-danger"
                onClick={() => handleDelete(faq._id)}
              >
                🗑️ Delete
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
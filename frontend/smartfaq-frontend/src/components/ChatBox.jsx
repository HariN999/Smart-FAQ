import { useState } from "react";
import { askQuestion } from "../api/faqApi";
import AnswerCard from "./AnswerCard";

export default function ChatBox() {
  const [question, setQuestion] = useState("");
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!question.trim()) return;

    setLoading(true);
    setResponse(null);
    
    try {
      const data = await askQuestion(question);
      setResponse(data);
    } catch (error) {
      console.error("Error asking question:", error);
      setResponse({
        answer: "Sorry, there was an error processing your question. Please try again.",
        confidence: null
      });
    } finally {
      setLoading(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSubmit();
    }
  };

  return (
    <div className="ai-surface">
      <div className="input-row">
        <input
          className="input"
          type="text"
          placeholder="Ask me anything..."
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          onKeyDown={handleKeyPress}
          disabled={loading}
          aria-label="Question input"
        />

        <button 
          className="button" 
          onClick={handleSubmit}
          disabled={loading || !question.trim()}
          aria-label="Submit question"
        >
          {loading ? "⏳ Thinking..." : "Ask"}
        </button>
      </div>

      {loading && (
        <div className="loading-container">
          <div className="loading-spinner"></div>
          <p>Processing your question...</p>
        </div>
      )}

      {response && !loading && <AnswerCard data={response} />}
    </div>
  );
}
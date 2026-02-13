import { useState } from "react";
import { askQuestion } from "../api/faqApi";
import AnswerCard from "./AnswerCard";

export default function ChatBox() {
  const [question, setQuestion] = useState("");
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!question) return;

    setLoading(true);
    const data = await askQuestion(question);
    setResponse(data);
    setLoading(false);
  };

  return (
    <div>
      <input
  type="text"
  placeholder="Ask something..."
  value={question}
  onChange={(e) => setQuestion(e.target.value)}
  onKeyDown={(e) => e.key === "Enter" && handleSubmit()}
/>

      <button onClick={handleSubmit}>Ask</button>

      {loading && <p>Loading...</p>}

      {response && <AnswerCard data={response} />}
    </div>
  );
}

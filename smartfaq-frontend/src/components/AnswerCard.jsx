export default function AnswerCard({ data }) {
  const percent = data.confidence ? (data.confidence * 100).toFixed(1) : 0;

  return (
    <div style={{ marginTop: "20px" }}>
      <h3>Answer:</h3>
      <p>{data.answer}</p>

      {data.confidence !== null && (
        <>
          <p style={{ color: data.confidence < 0.5 ? "red" : "green" }}>Confidence: {percent}%</p>

          <div style={{
            width: "300px",
            height: "10px",
            background: "#333",
            borderRadius: "6px",
            overflow: "hidden"
          }}>
            <div style={{
              width: `${percent}%`,
              height: "100%",
              background: percent < 40 ? "#ff4d4f" : "#4caf50"
            }} />
          </div>
        </>
      )}
    </div>
  );
}

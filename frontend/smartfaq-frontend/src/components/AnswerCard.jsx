export default function AnswerCard({ data }) {
  const percent = data.confidence ? (data.confidence * 100).toFixed(1) : 0;
  const isHighConfidence = data.confidence >= 0.5;

  return (
    <div className="answer-container">
      <div className="answer-label">
        Answer
      </div>
      
      <p className="answer-text">{data.answer}</p>

      {data.confidence !== null && (
        <div className="confidence-section">
          <div className="confidence-label">
            <span>Confidence Score</span>
            <span className={`confidence-value ${isHighConfidence ? 'high' : 'low'}`}>
              {percent}%
            </span>
          </div>

          <div className="confidence-bar">
            <div 
              className={`confidence-fill ${isHighConfidence ? 'high' : 'low'}`}
              style={{ width: `${percent}%` }}
              role="progressbar"
              aria-valuenow={percent}
              aria-valuemin="0"
              aria-valuemax="100"
            />
          </div>
        </div>
      )}
    </div>
  );
}
import { useState } from "react";
import ProgressBar from "./ProgressBar";

const confidenceOptions = ["Low", "Medium", "High"];

export default function QuestionScreen({ student, question, onSubmit, onCancel }) {
  const [answer, setAnswer] = useState("");
  const [confidence, setConfidence] = useState("Medium");
  const questionNumber = (student.learning_history?.length || 0) + 1;
  const masteryEstimate = Math.min(100, Math.max(0, Math.round(student.overall_mastery_score || 0)));

  const handleSubmit = () => {
    onSubmit({
      name: student.name,
      topic: question.topic,
      level: question.level,
      question_id: question.id,
      question_text: question.question,
      options: question.options,
      answer,
      confidence,
      expected_answer: question.answer || "",
    });
  };

  return (
    <div className="space-y-6">
      <button className="text-cyan-400 hover:text-cyan-300" onClick={onCancel}>
        &larr; Return to dashboard
      </button>
      <div className="rounded-3xl border border-slate-700 bg-slate-950 p-6">
        <h2 className="text-3xl font-semibold">{question.topic}</h2>
        <div className="mt-3 flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
          <p className="text-slate-400">Question {questionNumber}</p>
          <div className="sm:w-1/3">
            <ProgressBar label="Estimated Mastery" value={masteryEstimate} />
          </div>
        </div>
        <p className="mt-4 text-slate-300">{question.question}</p>
        {question.options.length > 0 && (
          <div className="mt-4 grid gap-3">
            {question.options.map((option) => (
              <button
                key={option}
                className={`rounded-2xl border px-4 py-3 text-left ${answer === option ? "border-cyan-500 bg-slate-800" : "border-slate-700 bg-slate-900"}`}
                onClick={() => setAnswer(option)}
                type="button"
              >
                {option}
              </button>
            ))}
          </div>
        )}
        {!question.options.length && (
          <textarea
            rows="5"
            className="mt-4 w-full"
            placeholder="Write your answer here"
            value={answer}
            onChange={(event) => setAnswer(event.target.value)}
          />
        )}
        <div className="mt-6 rounded-3xl border border-slate-700 bg-slate-900 p-4">
          <p className="font-semibold">Select your confidence level</p>
          <div className="mt-3 flex flex-wrap gap-2">
            {confidenceOptions.map((level) => (
              <button
                key={level}
                className={`rounded-full px-4 py-2 ${confidence === level ? "bg-cyan-500 text-slate-950" : "bg-slate-800 text-slate-200"}`}
                onClick={() => setConfidence(level)}
                type="button"
              >
                {level}
              </button>
            ))}
          </div>
        </div>
        <button
          className="mt-6 rounded-2xl bg-cyan-500 px-6 py-3 font-semibold text-slate-950 hover:bg-cyan-400"
          onClick={handleSubmit}
          disabled={!answer.trim()}
        >
          Submit Answer
        </button>
      </div>
    </div>
  );
}

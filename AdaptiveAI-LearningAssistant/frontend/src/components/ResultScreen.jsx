import { useState } from "react";

export default function ResultScreen({ result, onContinue, onDashboard }) {
  const [hintStep, setHintStep] = useState(0);
  const hintLevels = result.hint_levels;
  const hintLabel = hintStep === 0 ? "Show Hint 1" : hintStep === 1 ? "Show Hint 2" : "Show Hint 3";
  const headingText = result.correct
    ? "Great job! Keep building on that momentum."
    : "Nice effort. Let's learn from this one.";

  const revealNextHint = () => {
    setHintStep((current) => Math.min(3, current + 1));
  };

  return (
    <div className="space-y-6">
      <div className="rounded-3xl border border-slate-700 bg-slate-950 p-6">
        <h2 className="text-3xl font-semibold">Result</h2>
        <p className="mt-4 text-slate-300">{headingText}</p>
        <div className="mt-6 space-y-4">
          {!hintLevels && result.hint && (
            <div className="rounded-2xl border border-amber-500 bg-amber-500/10 p-4">
              <h3 className="font-semibold text-amber-200">Hint</h3>
              <p className="mt-2 text-slate-200">{result.hint}</p>
            </div>
          )}
          {result.explanation && (
            <div className="rounded-2xl border border-cyan-500 bg-cyan-500/10 p-4">
              <h3 className="font-semibold text-cyan-200">Explanation</h3>
              <p className="mt-2 text-slate-200">{result.explanation}</p>
            </div>
          )}
          {result.misconception && (
            <div className="rounded-2xl border border-amber-500 bg-amber-500/10 p-4">
              <h3 className="font-semibold text-amber-200">Common Misconception Detected</h3>
              <p className="mt-2 text-slate-200">{result.misconception}</p>
            </div>
          )}
          {hintLevels && (
            <div className="rounded-2xl border border-slate-700 bg-slate-900 p-4">
              <div className="flex items-center justify-between">
                <h3 className="font-semibold text-slate-100">Hints</h3>
                {hintStep < 3 && (
                  <button
                    type="button"
                    className="rounded-full bg-cyan-500 px-4 py-2 text-sm font-semibold text-slate-950 hover:bg-cyan-400"
                    onClick={revealNextHint}
                  >
                    {hintLabel}
                  </button>
                )}
              </div>
              <div className="mt-3 space-y-3 text-slate-200">
                {hintStep >= 1 && hintLevels.hint1 && (
                  <div>
                    <strong>Hint 1:</strong> {hintLevels.hint1}
                  </div>
                )}
                {hintStep >= 2 && hintLevels.hint2 && (
                  <div>
                    <strong>Hint 2:</strong> {hintLevels.hint2}
                  </div>
                )}
                {hintStep >= 3 && hintLevels.hint3 && (
                  <div>
                    <strong>Hint 3:</strong> {hintLevels.hint3}
                  </div>
                )}
                {hintStep === 0 && (
                  <p className="text-slate-400">Request a hint to get a guided clue step-by-step.</p>
                )}
              </div>
            </div>
          )}
          {result.adaptive_explanation && (
            <div className="rounded-2xl border border-slate-700 bg-slate-800 p-4">
              <h3 className="font-semibold text-slate-100">Adaptive Feedback</h3>
              <p className="mt-2 text-slate-300">{result.adaptive_explanation}</p>
            </div>
          )}
        </div>
        <div className="mt-6 space-y-4">
          {result.evaluation && (
            <div className="rounded-2xl border border-slate-700 bg-slate-900 p-4">
              <h3 className="font-semibold text-slate-100">Evaluation Summary</h3>
              <p className="mt-2 text-slate-300">Status: {result.evaluation.label}</p>
              <p className="text-slate-300">Confidence Score: {result.evaluation.confidence_score}%</p>
              <p className="text-slate-300">Reason: {result.evaluation.reason}</p>
            </div>
          )}
          <div className="flex gap-4 flex-wrap">
            <button className="rounded-2xl bg-cyan-500 px-5 py-3 font-semibold text-slate-950 hover:bg-cyan-400" onClick={onContinue}>
              Continue
            </button>
            <button className="rounded-2xl border border-slate-700 px-5 py-3 text-slate-200 hover:border-cyan-500" onClick={onDashboard}>
              Back to Dashboard
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default function ResultScreen({ result, onContinue, onDashboard }) {
  return (
    <div className="space-y-6">
      <div className="rounded-3xl border border-slate-700 bg-slate-950 p-6">
        <h2 className="text-3xl font-semibold">Result</h2>
        <p className="mt-4 text-slate-300">{result.correct ? "Well done!" : "Keep going, learning is an iterative process."}</p>
        <div className="mt-6 space-y-4">
          {result.hint && (
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
          {result.adaptive_explanation && (
            <div className="rounded-2xl border border-slate-700 bg-slate-800 p-4">
              <h3 className="font-semibold text-slate-100">Adaptive Feedback</h3>
              <p className="mt-2 text-slate-300">{result.adaptive_explanation}</p>
            </div>
          )}
        </div>
        <div className="mt-6 flex gap-4 flex-wrap">
          <button className="rounded-2xl bg-cyan-500 px-5 py-3 font-semibold text-slate-950 hover:bg-cyan-400" onClick={onContinue}>
            Continue
          </button>
          <button className="rounded-2xl border border-slate-700 px-5 py-3 text-slate-200 hover:border-cyan-500" onClick={onDashboard}>
            Back to Dashboard
          </button>
        </div>
      </div>
    </div>
  );
}

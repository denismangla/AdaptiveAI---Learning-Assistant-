export default function TopicSelectionPage({ topic, onBack, onStartTopic }) {
  return (
    <div className="space-y-6">
      <button className="text-cyan-400 hover:text-cyan-300" onClick={onBack}>
        &larr; Back to dashboard
      </button>
      <div className="rounded-3xl border border-slate-700 bg-slate-950 p-6">
        <h2 className="text-3xl font-semibold">{topic}</h2>
        <p className="mt-3 text-slate-400">Start an adaptive practice cycle for this topic. The next question will be selected internally based on your progress.</p>
        <div className="mt-6">
          <button
            className="rounded-3xl border border-slate-700 bg-cyan-600 px-6 py-5 text-left font-semibold text-slate-950 transition hover:bg-cyan-500"
            onClick={() => onStartTopic(topic)}
          >
            Start Practice
          </button>
        </div>
      </div>
    </div>
  );
}

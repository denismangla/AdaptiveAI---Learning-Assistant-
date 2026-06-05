export default function TopicSelectionPage({ topic, onBack, onStartTopic }) {
  const levels = ["Recognition", "Understanding", "Application", "Debugging"];
  return (
    <div className="space-y-6">
      <button className="text-cyan-400 hover:text-cyan-300" onClick={onBack}>
        &larr; Back to dashboard
      </button>
      <div className="rounded-3xl border border-slate-700 bg-slate-950 p-6">
        <h2 className="text-3xl font-semibold">{topic}</h2>
        <p className="mt-3 text-slate-400">Select a hierarchical level to begin practice for this topic.</p>
        <div className="mt-6 grid gap-4 sm:grid-cols-2">
          {levels.map((level) => (
            <button
              key={level}
              className="rounded-3xl border border-slate-700 bg-slate-800 px-5 py-6 text-left transition hover:border-cyan-500"
              onClick={() => onStartTopic(topic, level)}
            >
              <h3 className="text-xl font-semibold">{level}</h3>
              <p className="mt-2 text-slate-400">Practice {level} level questions and improve adaptive mastery.</p>
            </button>
          ))}
        </div>
      </div>
    </div>
  );
}

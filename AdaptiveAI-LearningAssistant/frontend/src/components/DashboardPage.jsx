export default function DashboardPage({ student, topics, onSelectTopic, onViewAnalytics }) {
  return (
    <div className="space-y-6">
      <div className="grid gap-4 md:grid-cols-2">
        <div className="rounded-3xl border border-slate-700 bg-slate-950 p-6">
          <h2 className="text-2xl font-semibold">Welcome back, {student.name}</h2>
          <p className="mt-3 text-slate-400">Topics attempted: {student.topics_attempted.length}</p>
          <p className="mt-2 text-slate-400">Average Confidence: {student.average_confidence}</p>
          <div className="mt-4 space-y-2">
            <h3 className="text-lg font-medium">Recommendations</h3>
            <div className="flex flex-wrap gap-2">
              {student.recommended_topics?.map((topic) => (
                <span key={topic} className="rounded-full bg-slate-800 px-3 py-1 text-sm text-slate-200">
                  {topic}
                </span>
              ))}
            </div>
          </div>
        </div>
        <div className="rounded-3xl border border-slate-700 bg-slate-950 p-6">
          <h3 className="text-2xl font-semibold">Weak Topics</h3>
          <p className="mt-3 text-slate-400">Strengthen the areas with lower mastery scores.</p>
          <div className="mt-4 flex flex-wrap gap-2">
            {(student.weak_topics.length ? student.weak_topics : ["None yet"]).map((topic) => (
              <span key={topic} className="rounded-full bg-slate-800 px-3 py-1 text-sm text-slate-200">
                {topic}
              </span>
            ))}
          </div>
          <button
            className="mt-6 rounded-2xl bg-cyan-500 px-5 py-3 font-semibold text-slate-950 hover:bg-cyan-400"
            onClick={onViewAnalytics}
          >
            View Analytics
          </button>
        </div>
      </div>
      <div className="rounded-3xl border border-slate-700 bg-slate-950 p-6">
        <h3 className="text-2xl font-semibold">Choose a Topic</h3>
        <div className="mt-5 grid gap-4 md:grid-cols-2">
          {topics.map((topic) => (
            <button
              key={topic.name}
              className="rounded-3xl border border-slate-700 bg-slate-800 p-5 text-left transition hover:border-cyan-500"
              onClick={() => onSelectTopic(topic.name)}
            >
              <h4 className="text-xl font-semibold">{topic.name}</h4>
              <p className="mt-2 text-slate-400">Levels: {topic.levels.join(", ")}</p>
            </button>
          ))}
        </div>
      </div>
    </div>
  );
}

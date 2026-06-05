import MasteryChart from "./MasteryChart";
import ProgressBar from "./ProgressBar";

export default function AnalyticsPage({ analytics, onBack }) {
  const masteryPercent = analytics.mastery || 0;
  return (
    <div className="space-y-6">
      <button className="text-cyan-400 hover:text-cyan-300" onClick={onBack}>
        &larr; Back to dashboard
      </button>
      <div className="rounded-3xl border border-slate-700 bg-slate-950 p-6">
        <h2 className="text-3xl font-semibold">Analytics Summary</h2>
        <div className="mt-5 grid gap-4 md:grid-cols-2">
          <div className="rounded-3xl border border-slate-800 bg-slate-900 p-5">
            <h3 className="text-xl font-semibold">Mastery</h3>
            <ProgressBar label="Overall Mastery" value={masteryPercent} />
          </div>
          <div className="rounded-3xl border border-slate-800 bg-slate-900 p-5">
            <h3 className="text-xl font-semibold">Attempts</h3>
            <p className="mt-3 text-slate-400">{analytics.total_attempts} total question attempts.</p>
          </div>
        </div>
        <div className="mt-5 grid gap-4 md:grid-cols-2">
          <div className="rounded-3xl border border-slate-800 bg-slate-900 p-5">
            <h3 className="text-xl font-semibold">Confidence</h3>
            <ProgressBar label="Average Confidence" value={analytics.average_confidence_score || 0} />
            <div className="mt-4 space-y-2 text-slate-400">
              <p>Low: {analytics.confidence_counts?.Low ?? 0}</p>
              <p>Medium: {analytics.confidence_counts?.Medium ?? 0}</p>
              <p>High: {analytics.confidence_counts?.High ?? 0}</p>
            </div>
          </div>
          <div className="rounded-3xl border border-slate-800 bg-slate-900 p-5">
            <h3 className="text-xl font-semibold">Weak Topics</h3>
            <div className="mt-3 flex flex-wrap gap-2">
              {(analytics.weak_topics.length ? analytics.weak_topics : ["None"]).map((topic) => (
                <span key={topic} className="rounded-full bg-slate-800 px-3 py-1 text-sm text-slate-200">{topic}</span>
              ))}
            </div>
          </div>
        </div>
        <div className="mt-5 space-y-4">
          <div className="rounded-3xl border border-slate-800 bg-slate-900 p-5">
            <h3 className="text-xl font-semibold">Learning Path</h3>
            {analytics.learning_path.length ? (
              <ol className="mt-3 list-decimal space-y-2 pl-5 text-slate-200">
                {analytics.learning_path.map((step, index) => (
                  <li key={`${step}-${index}`}>{step}</li>
                ))}
              </ol>
            ) : (
              <p className="mt-3 text-slate-400">No learning path has been generated yet.</p>
            )}
          </div>
          <div className="rounded-3xl border border-slate-800 bg-slate-900 p-5">
            <h3 className="text-xl font-semibold">Misconceptions</h3>
            <div className="mt-3 space-y-2 text-slate-200">
              {(analytics.misconceptions.length ? analytics.misconceptions : ["None detected yet."]).map((misconception) => (
                <p key={misconception} className="rounded-2xl bg-slate-800 px-3 py-2">{misconception}</p>
              ))}
            </div>
          </div>
          <div className="rounded-3xl border border-slate-800 bg-slate-900 p-5">
            <MasteryChart scores={analytics.scores || {}} />
          </div>
        </div>
        <div className="mt-5 rounded-3xl border border-slate-800 bg-slate-900 p-5">
          <h3 className="text-xl font-semibold">Knowledge Dependencies</h3>
          <div className="mt-3 space-y-2 text-slate-200">
            {(analytics.dependency_summary.length ? analytics.dependency_summary : ["No dependency information available."]).map((item) => (
              <p key={item}>{item}</p>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}

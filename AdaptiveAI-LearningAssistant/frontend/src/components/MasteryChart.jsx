export default function MasteryChart({ scores }) {
  return (
    <div className="space-y-4">
      <h3 className="text-xl font-semibold">Mastery Chart</h3>
      <div className="space-y-3">
        {Object.entries(scores).map(([level, score]) => (
          <div key={level} className="rounded-3xl border border-slate-800 bg-slate-900 p-4">
            <div className="flex items-center justify-between text-sm text-slate-300">
              <span>{level}</span>
              <span>{score}%</span>
            </div>
            <div className="mt-3 h-3 rounded-full bg-slate-800">
              <div className="h-full rounded-full bg-cyan-500" style={{ width: `${score}%` }} />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

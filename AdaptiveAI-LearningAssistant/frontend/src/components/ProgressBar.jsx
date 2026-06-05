export default function ProgressBar({ label, value }) {
  return (
    <div className="space-y-2">
      <div className="flex items-center justify-between text-sm text-slate-300">
        <span>{label}</span>
        <span>{value}%</span>
      </div>
      <div className="h-3 rounded-full bg-slate-800">
        <div className="h-full rounded-full bg-cyan-500" style={{ width: `${value}%` }} />
      </div>
    </div>
  );
}

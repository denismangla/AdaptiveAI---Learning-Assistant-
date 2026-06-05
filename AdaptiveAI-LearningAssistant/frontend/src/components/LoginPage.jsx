import { useState } from "react";

export default function LoginPage({ onLogin }) {
  const [name, setName] = useState("");

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-4xl font-semibold">Adaptive AI Learning Assistant</h1>
        <p className="mt-3 text-slate-400">Choose a topic, answer a question, select your confidence, and let the system personalize your learning path.</p>
      </div>
      <div className="rounded-3xl border border-slate-700 bg-slate-950 p-6">
        <label className="block text-sm text-slate-300">Student Name</label>
        <input
          className="mt-2 w-full"
          value={name}
          onChange={(event) => setName(event.target.value)}
          placeholder="Enter your name"
          autoFocus
        />
        <button
          className="mt-4 rounded-2xl bg-cyan-500 px-5 py-3 font-semibold text-slate-950 hover:bg-cyan-400"
          onClick={() => onLogin(name)}
          disabled={!name.trim()}
        >
          Start Learning
        </button>
      </div>
    </div>
  );
}

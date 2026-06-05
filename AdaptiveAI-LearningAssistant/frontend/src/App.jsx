import { useEffect, useState } from "react";
import { loginUser, fetchTopics, fetchProfile, fetchAnalytics, requestQuestion, submitAnswer } from "./api/apiClient";
import LoginPage from "./components/LoginPage";
import DashboardPage from "./components/DashboardPage";
import TopicSelectionPage from "./components/TopicSelectionPage";
import QuestionScreen from "./components/QuestionScreen";
import ResultScreen from "./components/ResultScreen";
import AnalyticsPage from "./components/AnalyticsPage";

const VIEWS = {
  LOGIN: "login",
  DASHBOARD: "dashboard",
  TOPIC_SELECTION: "topicSelection",
  QUESTION: "question",
  RESULT: "result",
  ANALYTICS: "analytics",
};

function App() {
  const [view, setView] = useState(VIEWS.LOGIN);
  const [student, setStudent] = useState(null);
  const [topics, setTopics] = useState([]);
  const [selectedTopic, setSelectedTopic] = useState(null);
  const [questionPayload, setQuestionPayload] = useState(null);
  const [resultData, setResultData] = useState(null);
  const [analytics, setAnalytics] = useState(null);

  useEffect(() => {
    if (student) {
      fetchProfile(student.name).then(setStudent).catch(console.error);
    }
  }, [student?.name]);

  const handleLogin = async (name) => {
    const profile = await loginUser(name);
    setStudent(profile);
    setView(VIEWS.DASHBOARD);
    const loadedTopics = await fetchTopics();
    setTopics(loadedTopics.topics || []);
  };

  const handleTopicSelect = (topic) => {
    setSelectedTopic(topic);
    setView(VIEWS.TOPIC_SELECTION);
  };

  const handleBeginTopic = async (topic) => {
    const next = await requestQuestion({ name: student.name, topic, level: "Recognition", difficulty: "medium" });
    setQuestionPayload(next);
    setView(VIEWS.QUESTION);
  };

  const handleSubmitAnswer = async (answerData) => {
    const result = await submitAnswer(answerData);
    setResultData(result);
    setStudent(await fetchProfile(student.name));
    setView(VIEWS.RESULT);
  };

  const loadAnalytics = async () => {
    const summary = await fetchAnalytics(student.name);
    setAnalytics(summary);
    setView(VIEWS.ANALYTICS);
  };

  return (
    <div className="min-h-screen px-4 py-6">
      <div className="mx-auto max-w-5xl rounded-3xl border border-slate-800 bg-slate-900/90 p-6 shadow-2xl shadow-slate-900/50">
        {view === VIEWS.LOGIN && <LoginPage onLogin={handleLogin} />}
        {view === VIEWS.DASHBOARD && student && (
          <DashboardPage
            student={student}
            topics={topics}
            onSelectTopic={handleTopicSelect}
            onViewAnalytics={loadAnalytics}
          />
        )}
        {view === VIEWS.TOPIC_SELECTION && selectedTopic && (
          <TopicSelectionPage
            topic={selectedTopic}
            onBack={() => setView(VIEWS.DASHBOARD)}
            onStartTopic={handleBeginTopic}
          />
        )}
        {view === VIEWS.QUESTION && questionPayload && (
          <QuestionScreen
            student={student}
            question={questionPayload}
            onSubmit={handleSubmitAnswer}
            onCancel={() => setView(VIEWS.DASHBOARD)}
          />
        )}
        {view === VIEWS.RESULT && resultData && (
          <ResultScreen
            result={resultData}
            onContinue={() => {
              if (resultData.next_question) {
                setQuestionPayload(resultData.next_question);
                setView(VIEWS.QUESTION);
              } else {
                setView(VIEWS.DASHBOARD);
              }
            }}
            onDashboard={() => setView(VIEWS.DASHBOARD)}
          />
        )}
        {view === VIEWS.ANALYTICS && analytics && (
          <AnalyticsPage analytics={analytics} onBack={() => setView(VIEWS.DASHBOARD)} />
        )}
      </div>
    </div>
  );
}

export default App;

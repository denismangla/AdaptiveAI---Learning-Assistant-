const API_BASE = "http://localhost:8000/api";

async function apiRequest(path, method = "GET", body = null) {
  const options = {
    method,
    headers: { "Content-Type": "application/json" },
  };
  if (body) options.body = JSON.stringify(body);
  const response = await fetch(`${API_BASE}${path}`, options);
  if (!response.ok) {
    const error = await response.json().catch(() => ({}));
    throw new Error(error.detail || "API request failed");
  }
  return response.json();
}

export const loginUser = (name) => apiRequest("/login", "POST", { name });
export const fetchTopics = () => apiRequest("/topics");
export const fetchProfile = (name) => apiRequest(`/profile/${encodeURIComponent(name)}`);
export const fetchAnalytics = (name) => apiRequest(`/analytics/${encodeURIComponent(name)}`);
export const requestQuestion = (payload) => apiRequest("/question", "POST", payload);
export const submitAnswer = (payload) => apiRequest("/answer", "POST", payload);

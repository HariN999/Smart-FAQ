import { useState } from "react";
import ChatBox from "./components/ChatBox";
import AdminLogin from "./components/AdminLogin";
import AdminPanel from "./components/AdminPanel";

function App() {
  const [token, setToken] = useState(localStorage.getItem("token"));
  const [view, setView] = useState("chat");

  return (
    <div className="app-container">
      <header className="app-header">
        <h1>Smart FAQ</h1>
        <p className="app-subtitle">
          Intelligent question answering powered by AI
        </p>
      </header>

      <div className="mode-switch">
        <button
          className={`button ${view === "chat" ? "active-mode" : ""}`}
          onClick={() => setView("chat")}
          aria-label="Switch to user mode"
        >
          💬 User Mode
        </button>

        <button
          className={`button ${view === "admin" ? "active-mode" : ""}`}
          onClick={() => setView("admin")}
          aria-label="Switch to admin mode"
        >
          ⚙️ Admin Mode
        </button>
      </div>

      <div className="view-container">
        {view === "chat" && <ChatBox />}

        {view === "admin" && (
          <>
            {!token ? (
              <AdminLogin onLogin={setToken} />
            ) : (
              <AdminPanel token={token} onLogout={() => {
                localStorage.removeItem("token");
                setToken(null);
              }} />
            )}
          </>
        )}
      </div>
    </div>
  );
}

export default App;
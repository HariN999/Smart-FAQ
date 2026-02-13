import { useState } from "react";
import ChatBox from "./components/ChatBox";
import AdminLogin from "./components/AdminLogin";
import AdminPanel from "./components/AdminPanel";

function App() {
  const [token, setToken] = useState(localStorage.getItem("token"));
  const [view, setView] = useState("chat"); // chat | admin

  return (
    <div
  style={{
    maxWidth: "800px",
    margin: "0 auto",
    padding: "40px",
    fontFamily: "sans-serif"
  }}
>

      <h1>Smart-FAQ</h1>

<div style={{ marginBottom: "20px" }}>
  <button onClick={() => setView("chat")}>User Mode</button>
  <button onClick={() => setView("admin")} style={{ marginLeft: "10px" }}>
    Admin Mode
  </button>
</div>

{view === "chat" && <ChatBox />}

{view === "admin" && (
  <>
    {!token ? (
      <AdminLogin onLogin={setToken} />
    ) : (
      <AdminPanel token={token} />
    )}
  </>
)}

    </div>
  );
}

export default App;

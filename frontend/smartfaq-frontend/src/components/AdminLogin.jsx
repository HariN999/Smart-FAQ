import { useState } from "react";
import { adminLogin } from "../api/adminApi";

export default function AdminLogin({ onLogin }) {
  const [loading, setLoading] = useState(false);

  const handleLogin = async () => {
    setLoading(true);
    const data = await adminLogin();

    localStorage.setItem("token", data.access_token);
    onLogin(data.access_token);

    setLoading(false);
  };

  return (
  <div
    style={{
      marginTop: "20px",
      padding: "20px",
      borderRadius: "12px",
      background: "#1e1e1e",
      border: "1px solid #333"
    }}
  >
    <h2>Admin Login</h2>

    <button
      onClick={handleLogin}
      style={{
        padding: "10px 18px",
        borderRadius: "8px",
        background: "#4caf50",
        border: "none",
        cursor: "pointer",
        color: "#fff",
        fontWeight: "bold"
      }}
    >
      {loading ? "Logging in..." : "Login as Admin"}
    </button>
  </div>
);

}

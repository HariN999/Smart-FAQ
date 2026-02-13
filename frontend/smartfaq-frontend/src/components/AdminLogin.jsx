import { useState } from "react";
import { adminLogin } from "../api/adminApi";

export default function AdminLogin({ onLogin }) {
  const [loading, setLoading] = useState(false);

  const handleLogin = async () => {
    setLoading(true);
    try {
      const data = await adminLogin();
      localStorage.setItem("token", data.access_token);
      onLogin(data.access_token);
    } catch (error) {
      console.error("Login failed:", error);
      alert("Login failed. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card admin-login">
      <div style={{ marginBottom: "24px" }}>
        <div style={{ 
          fontSize: "48px", 
          marginBottom: "16px",
          filter: "grayscale(1) opacity(0.6)"
        }}>
          🔐
        </div>
        <h2>Admin Access</h2>
        <p style={{ color: "var(--text-secondary)", marginTop: "8px" }}>
          Authenticate to manage FAQ content
        </p>
      </div>

      <button
        onClick={handleLogin}
        className="button"
        disabled={loading}
        style={{ minWidth: "200px" }}
      >
        {loading ? "Authenticating..." : "🔑 Login as Admin"}
      </button>
    </div>
  );
}
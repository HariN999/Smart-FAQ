const API = "http://127.0.0.1:8000";

export async function adminLogin() {
  const res = await fetch(`${API}/admin/login`, {
    method: "POST",
  });

  return res.json();
}

export async function getProtected(token) {
  const res = await fetch(`${API}/admin/protected`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  return res.json();
}
export async function fetchFaqs(token) {
  const res = await fetch(`${API}/admin/faqs`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
  return res.json();
}

export async function addFaq(token, faq) {
  const res = await fetch(`${API}/admin/faqs`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify(faq),
  });
  return res.json();
}

export async function deleteFaq(token, id) {
  await fetch(`${API}/admin/faqs/${id}`, {
    method: "DELETE",
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
}
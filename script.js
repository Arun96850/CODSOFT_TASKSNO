function login() {
  const username = document.getElementById("username").value.trim();
  const password = document.getElementById("password").value.trim();

  const result = document.getElementById("result");

  if (username === "admin" && password === "admin123") {
    result.textContent = "✅ Login Successful!";
  } else {
    result.textContent = "❌ Invalid username or password.";
  }
}

  
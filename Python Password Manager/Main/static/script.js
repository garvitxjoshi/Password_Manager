// Password suggestion algorithm
function suggestStrongPassword(length = 16) {
  const chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+[]{}<>?/|";
  let groups = [
    chars[Math.floor(Math.random() * 26)],
    chars[26 + Math.floor(Math.random() * 26)],
    chars[52 + Math.floor(Math.random() * 10)],
    chars[62 + Math.floor(Math.random() * (chars.length - 62))]
  ];
  let remaining = '';
  for (let i = 0; i < length - groups.length; i++) {
    remaining += chars[Math.floor(Math.random() * chars.length)];
  }
  let passwordArr = groups.concat(remaining.split(''));
  for (let i = passwordArr.length - 1; i > 0; i--) {
    let j = Math.floor(Math.random() * (i + 1));
    [passwordArr[i], passwordArr[j]] = [passwordArr[j], passwordArr[i]];
  }
  return passwordArr.join('');
}

// Show/hide register/login panels
document.getElementById('registerPrompt').onclick = function() {
  document.getElementById('loginContainer').style.display = "none";
  document.getElementById('registerContainer').style.display = "";
};
document.getElementById('goToLogin').onclick = function() {
  document.getElementById('registerContainer').style.display = "none";
  document.getElementById('loginContainer').style.display = "";
};

// Password suggestion for registration
document.getElementById('suggestPwdBtn').onclick = function() {
  const pwd = suggestStrongPassword();
  document.getElementById('suggestedPassword').value = pwd;
  document.getElementById('registerPassword').value = pwd;
};

// Registration feedback (frontend only, integrate backend as needed)
document.getElementById('registerBtn').onclick = function() {
  let user = document.getElementById('registerUsername').value,
      pwd = document.getElementById('registerPassword').value,
      mpwd = document.getElementById('registerMasterPassword').value;
  if (user && pwd && mpwd) {
    document.getElementById('registerMsgText').textContent = "Registration successful!";
    document.getElementById('tickIcon').style.display = "";
  } else {
    document.getElementById('registerMsgText').textContent = "Enter all fields.";
    document.getElementById('tickIcon').style.display = "none";
  }
};

document.getElementById('loginBtn').onclick = function() {
  let user = document.getElementById('loginUsername').value,
      pwd = document.getElementById('loginPassword').value,
      mpwd = document.getElementById('loginMasterPassword').value;
  if (user && pwd && mpwd) {
    document.getElementById('loginMessage').textContent = "Login successful!";
    document.getElementById('welcomeMsg').textContent = `👋 Welcome, ${user}!`;
    document.getElementById('loginContainer').style.display = "none";
    document.getElementById('manager').style.display = "";
  } else {
    document.getElementById('loginMessage').textContent = "Invalid credentials or missing fields.";
  }
};

document.getElementById('logoutBtn').onclick = function() {
  document.getElementById('manager').style.display = "none";
  document.getElementById('loginContainer').style.display = "";
};

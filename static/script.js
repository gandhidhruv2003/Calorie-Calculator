document.getElementById("signupBtn").addEventListener("click", function() {
  window.location.href = "/signup";
});

document.getElementById("loginBtn").addEventListener("click", function() {
  window.location.href = "/login";
});


document.getElementById("loginForm").addEventListener("submit", function(event) {
  event.preventDefault();
  window.location.href = "/homepage"; 
});

document.getElementById("signupForm").addEventListener("submit", function(event) {
  event.preventDefault();    
  window.location.href = "/homepage"; 
});

document.getElementById("calculate").addEventListener("submit", function(event) {
  event.preventDefault();    
  window.location.href = "/result"; 
});

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

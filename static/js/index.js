document.addEventListener('DOMContentLoaded', function() {
    const signInForm = document.getElementById('signInForm');
    const message = document.getElementById('message');
    const passwordInput = document.getElementById('password');
    const passwordStrength = document.getElementById('password-strength');
  
    signInForm.addEventListener('submit', function(event) {
      event.preventDefault();
      const name = signInForm.name.value;
      const email = signInForm.email.value;
      const password = signInForm.password.value;
  
      if (!name || !email || !password) {
        message.textContent = 'Please fill in all fields.';
        message.style.color = 'red';
        return;
      }
  
      if (!isValidEmail(email)) {
        message.textContent = 'Please enter a valid email address.';
        message.style.color = 'red';
        return;
      }
  
      if (calculatePasswordStrength(password) < 2) {
        message.textContent = 'Password must be at least moderately strong.';
        message.style.color = 'red';
        return;
      }
  
      // Mock verification process - replace this with your actual verification logic
      message.textContent = 'Sign in successful!';
      message.style.color = 'green';
      window.location.href = 'calculator.html';
    });
  
    function isValidEmail(email) {
      // basic email validation
      return /\S+@\S+\.\S+/.test(email);
    }
  
    function calculatePasswordStrength(password) {
      // basic password strength calculation
      // You can implement more sophisticated algorithms for better accuracy
      if (password.length < 6) {
        return 0; // Weak
      }
      if (password.length < 10) {
        return 1; // Moderately strong
      }
      return 2; // Strong
    }
  
    passwordInput.addEventListener('input', function() {
      const strength = calculatePasswordStrength(passwordInput.value);
      switch (strength) {
        case 0:
          passwordStrength.textContent = 'Weak';
          passwordStrength.style.color = 'red';
          break;
        case 1:
          passwordStrength.textContent = 'Moderate';
          passwordStrength.style.color = 'orange';
          break;
        case 2:
          passwordStrength.textContent = 'Strong';
          passwordStrength.style.color = 'green';
          break;
      }
    });
  });

  
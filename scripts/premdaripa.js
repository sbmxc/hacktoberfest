function validatePassword(password) {
    // Define the regular expressions for various password criteria
    const minLength = 8; // Minimum password length
    const hasUppercase = /[A-Z]/;
    const hasLowercase = /[a-z]/;
    const hasDigit = /[0-9]/;
    const hasSpecialChar = /[!@#$%^&*()_+{}\[\]:;<>,.?~\\/-]/; // You can customize this list of special characters
  
    // Check the minimum length
    if (password.length < minLength) {
      return false;
    }
  
    // Check for uppercase letters
    if (!hasUppercase.test(password)) {
      return false;
    }
  
    // Check for lowercase letters
    if (!hasLowercase.test(password)) {
      return false;
    }
  
    // Check for at least one digit
    if (!hasDigit.test(password)) {
      return false;
    }
  
    // Check for at least one special character
    if (!hasSpecialChar.test(password)) {
      return false;
    }
  
    // If all criteria are met, the password is valid
    return true;
  }
  
  // Example usage:
  const password = "MyP@ssw0rd";
  const isValid = validatePassword(password);
  
  if (isValid) {
    console.log("Password is valid.");
  } else {
    console.log("Password is invalid.");
  }
  
document.addEventListener("DOMContentLoaded", () => {
  const computerNumber = Math.floor(Math.random() * 100) + 1; // Generating random number
  const submitButton = document.getElementById("submit"); // Access Submit button
  const guessInput = document.getElementById("guess"); // Guess input
  const messageElement = document.getElementById("message"); // Message
  const chanceCountElement = document.getElementById("chance-count"); // Count number
  let chancesTaken = 0; // by default use 0
  // ------------------------------------------ Party Popor style ----------------------------------------------
  const triggerConfetti = () => {
    const duration = 5000; // Duration of the confetti effect
    const animationEnd = Date.now() + duration;
    const defaults = {
      startVelocity: 50,
      spread: 360,
      ticks: 60,
      zIndex: 0,
      scalar: 2,
    };

    function randomInRange(min, max) {
      return Math.random() * (max - min) + min;
    }

    const interval = setInterval(() => {
      const timeLeft = animationEnd - Date.now();

      if (timeLeft <= 0) {
        return clearInterval(interval);
      }

      const particleCount = 100 * (timeLeft / duration); // Increased particle count

      // Since particles fall down, start a bit higher than random
      confetti(
        Object.assign({}, defaults, {
          particleCount,
          origin: { x: randomInRange(0.1, 0.3), y: Math.random() - 0.2 },
        })
      );
      confetti(
        Object.assign({}, defaults, {
          particleCount,
          origin: { x: randomInRange(0.7, 0.9), y: Math.random() - 0.2 },
        })
      );
    }, 250);
  };

  // --------------------------------------------------------------------------------------------------------
  const handleGuess = () => {
    const userGuess = parseInt(guessInput.value);

    if (isNaN(userGuess) || userGuess < 1 || userGuess > 100) {
      // isNaN (is not a number ) to check i/o is number or not
      messageElement.textContent = "Please enter a number between 1 and 100.";
      return;
    }

    chancesTaken++;
    chanceCountElement.textContent = chancesTaken; // Challan bad gayi

    if (userGuess < computerNumber) {
      messageElement.textContent = "Too low! Try again.";
    } else if (userGuess > computerNumber) {
      messageElement.textContent = "Too high! Try again.";
    } else {
      messageElement.textContent = `Congratulations! You guessed the right number: ${computerNumber}.`;
      submitButton.disabled = true;
      triggerConfetti(); // Trigger confetti effect when the user wins
    }

    guessInput.value = "";
  };

  // Event listener for button click
  submitButton.addEventListener("click", handleGuess);

  // Event listener for Enter key press
  guessInput.addEventListener("keypress", (event) => {
    if (event.key === "Enter") {
      event.preventDefault();
      handleGuess();
    }
  });
});

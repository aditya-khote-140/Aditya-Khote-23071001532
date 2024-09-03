document.addEventListener('DOMContentLoaded', () => {
    const computerNumber = Math.floor(Math.random() * 100) + 1;
    const submitButton = document.getElementById('submit');
    const guessInput = document.getElementById('guess');
    const messageElement = document.getElementById('message');
    const chanceCountElement = document.getElementById('chance-count');
    let chancesTaken = 0;

    const handleGuess = () => {
        const userGuess = parseInt(guessInput.value, 10);

        if (isNaN(userGuess) || userGuess < 1 || userGuess > 100) {
            messageElement.textContent = 'Please enter a number between 1 and 100.';
            return;
        }

        chancesTaken++;
        chanceCountElement.textContent = chancesTaken;

        if (userGuess < computerNumber) {
            messageElement.textContent = 'Too low! Try again.';
        } else if (userGuess > computerNumber) {
            messageElement.textContent = 'Too high! Try again.';
        } else {
            messageElement.textContent = `Congratulations! You guessed the number ${computerNumber}.`;
            submitButton.disabled = true;  
        }

        guessInput.value = '';
    };

    // Event listener for button click
    submitButton.addEventListener('click', handleGuess);

    // Event listener for Enter key press
    guessInput.addEventListener('keypress', (event) => {
        if (event.key === 'Enter') {
            event.preventDefault(); 
            handleGuess();
        }
    });
});
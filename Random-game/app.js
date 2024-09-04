// First html load then js work : that we use DOMContentLoaded ;
document.addEventListener('DOMContentLoaded', () => {
    
    const computerNumber = Math.floor(Math.random() * 100) + 1; //to Generating randome number
    const submitButton = document.getElementById('submit'); // Access Submit button
    const guessInput = document.getElementById('guess'); // Guess input
    const messageElement = document.getElementById('message'); // Message
    const chanceCountElement = document.getElementById('chance-count'); // Count number
    let chancesTaken = 0; // by default use 0

    const handleGuess = () => {
        const userGuess = parseInt(guessInput.value);

        if (isNaN(userGuess) || userGuess < 1 || userGuess > 100) { // isNaN (is not a number ) to check i/o is number or not
            messageElement.textContent = 'Please enter a number between 1 and 100.';
            return;
        }

        chancesTaken++;
        chanceCountElement.textContent = chancesTaken; // challa bad gayi 

        if (userGuess < computerNumber) {
            messageElement.textContent = 'Too low! Try again.';
        } else if (userGuess > computerNumber) {
            messageElement.textContent = 'Too high! Try again.';
        } else {
            messageElement.textContent = `Congratulations! You Guess the  Right number ${computerNumber}.`;
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
function startListening() {
    const output = document.getElementById("output");

    // Check for browser support
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SpeechRecognition) {
        alert("Your browser does not support speech recognition.");
        return;
    }

    const recognition = new SpeechRecognition();
    recognition.lang = "en-US";

    recognition.onresult = function(event) {
        const transcript = event.results[0][0].transcript;
        output.innerHTML = "You said: " + transcript;

        // Send to backend
        fetch('/ask', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({message: transcript})
        })
        .then(res => res.json())
        .then(data => {
            const reply = data.reply;
            output.innerHTML += "<br>Eli says: " + reply;

            // Speak response
            const synth = window.speechSynthesis;
            const utter = new SpeechSynthesisUtterance(reply);
            synth.speak(utter);
        });
    }

    recognition.start();
}


document.getElementById("submit-button").addEventListener("click", function() {
    var article = document.getElementById("news-article").value;
    
    if (article.trim() === "") {
        alert("Please enter an article!");
        return;
    }
    
    // Show loading spinner
    document.getElementById("loading-spinner").style.display = "block";
    
    // Send the article to the backend for prediction
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ article: article }),
    })
    .then(response => response.json())
    .then(data => {
        // Hide loading spinner
        document.getElementById("loading-spinner").style.display = "none";
        
        // Display the result
        document.getElementById("result").textContent = "Prediction: " + data.prediction;
    })
    .catch(error => {
        document.getElementById("loading-spinner").style.display = "none";
        console.error("Error:", error);
    });
});

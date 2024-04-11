// Function to open the chat box
function openChat() {
    document.getElementById("chatBox").style.display = "block";
  }
  
  // Function to close the chat box
  function closeChat() {
    document.getElementById("chatBox").style.display = "none";
  }
  
  // Function to send message
  function sendMessage() {
    var messageInput = document.getElementById("messageInput");
    var message = messageInput.value;
    
    if (message.trim() === "") return; // Do not send empty messages
    
    // Display user message in chat
    var chatMessages = document.getElementById("chatMessages");
    chatMessages.innerHTML += "<p>You: " + message + "</p>";
    
    // Clear message input
    messageInput.value = "";
    
    // Send message to Flask server
    fetch('/action_page.php', {
      method: 'POST',
      body: new URLSearchParams({
        msg: message
      }),
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      }
    })
    .then(response => response.text())
    .then(data => {
      // Display server response in chat
      chatMessages.innerHTML += "<p>Server: " + data + "</p>";
    })
    .catch(error => console.error('Error:', error));
  }
  